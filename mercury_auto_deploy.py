import shutil,os,json,base64,tempfile,subprocess,urllib.request,zipfile,io,plistlib,datetime,time
from pathlib import Path
import jwt
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
assets=json.loads(os.environ['ASSETS'])
key,cert,_=pkcs12.load_key_and_certificates(base64.b64decode(assets['p12']),assets['password'].encode())
sealed=json.loads(Path('mercury_auto_source.sealed.json').read_text())
aes=key.decrypt(base64.b64decode(sealed['key']),padding.OAEP(mgf=padding.MGF1(hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
source=AESGCM(aes).decrypt(base64.b64decode(sealed['nonce']),base64.b64decode(sealed['data']),b'MercuryAuto-v1')
with tempfile.TemporaryDirectory(prefix='mercury-auto-') as directory:
 root=Path(directory); project=root/'project';project.mkdir()
 with zipfile.ZipFile(io.BytesIO(source)) as archive:
  for entry in archive.infolist():
   assert not Path(entry.filename).is_absolute() and '..' not in Path(entry.filename).parts
  archive.extractall(project)
 now=int(time.time())
 token=jwt.encode({'iss':os.environ['ISSUER_ID'],'iat':now,'exp':now+900,'aud':'appstoreconnect-v1'},os.environ['API_KEY'],algorithm='ES256',headers={'kid':os.environ['KEY_ID'],'typ':'JWT'})
 def get(path):
  request=urllib.request.Request('https://api.appstoreconnect.apple.com'+path,headers={'Authorization':'Bearer '+token})
  with urllib.request.urlopen(request,timeout=60) as response:return json.load(response)
 profiles=get('/v1/profiles?limit=200')['data']
 match=[p for p in profiles if p['attributes']['name']=='MercuryAuto_AppStore_iReview43_Cert']
 assert len(match)==1,'Mercury Auto profile not found or ambiguous'
 info=match[0]['attributes'];profile=base64.b64decode(info['profileContent'])
 profilefile=root/'profile.mobileprovision';profilefile.write_bytes(profile)
 decoded=subprocess.run(['security','cms','-D','-i',str(profilefile)],capture_output=True,check=True)
 details=plistlib.loads(decoded.stdout)
 assert details['Entitlements']['application-identifier']=='F3639777XM.com.ienergyidata.MercuryAuto'
 assert not details['Entitlements'].get('get-task-allow',False)
 assert details['TeamIdentifier']==['F3639777XM']
 assert details['ExpirationDate']>datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
 from cryptography import x509
 assert any(x509.load_der_x509_certificate(c).fingerprint(hashes.SHA256())==cert.fingerprint(hashes.SHA256()) for c in details['DeveloperCertificates']),'Certificate/profile mismatch'
 profileuuid=details['UUID']; installed=[]; keychain=root/'signing.keychain-db'; keypass=base64.b64encode(os.urandom(32)).decode()
 def run(*args,**kwargs):subprocess.run(args,check=True,**kwargs)
 try:
  for folder in [Path.home()/'Library/MobileDevice/Provisioning Profiles',Path.home()/'Library/Developer/Xcode/UserData/Provisioning Profiles']:
   folder.mkdir(parents=True,exist_ok=True);target=folder/(profileuuid+'.mobileprovision')
   assert not target.exists(),'Profile already exists on runner'
   target.write_bytes(profile);installed.append(target)
  p12=root/'distribution.p12';p12.write_bytes(base64.b64decode(assets['p12']));p12.chmod(0o600)
  run('security','create-keychain','-p',keypass,str(keychain),stdout=subprocess.DEVNULL)
  run('security','unlock-keychain','-p',keypass,str(keychain),stdout=subprocess.DEVNULL)
  run('security','set-keychain-settings','-lut','21600',str(keychain),stdout=subprocess.DEVNULL)
  run('security','import',str(p12),'-k',str(keychain),'-P',assets['password'],'-T','/usr/bin/codesign','-T','/usr/bin/security',stdout=subprocess.DEVNULL)
  run('security','set-key-partition-list','-S','apple-tool:,apple:,codesign:','-s','-k',keypass,str(keychain),stdout=subprocess.DEVNULL)
  run('security','list-keychains','-d','user','-s',str(keychain))
  run('python3','build_assets.py',cwd=project);run('xcodegen','generate',cwd=project)
  archivepath=root/'MercuryAuto.xcarchive';export=root/'export'
  run('xcodebuild','-project','MercuryAuto.xcodeproj','-scheme','MercuryAuto','-configuration','Release','-destination','generic/platform=iOS','-archivePath',str(archivepath),'DEVELOPMENT_TEAM=F3639777XM','CODE_SIGN_STYLE=Manual','CODE_SIGN_IDENTITY=Apple Distribution','PROVISIONING_PROFILE_SPECIFIER='+profileuuid,'CURRENT_PROJECT_VERSION='+os.environ['BUILD_NUMBER'],'MARKETING_VERSION=0.3','archive',cwd=project)
  options=root/'ExportOptions.plist';options.write_bytes(plistlib.dumps({'method':'app-store-connect','destination':'export','signingStyle':'manual','teamID':'F3639777XM','signingCertificate':'Apple Distribution','provisioningProfiles':{'com.ienergyidata.MercuryAuto':profileuuid}}))
  run('xcodebuild','-exportArchive','-archivePath',str(archivepath),'-exportPath',str(export),'-exportOptionsPlist',str(options),cwd=project)
  ipa=list(export.glob('*.ipa'));assert len(ipa)==1,'IPA missing'
  out=Path.cwd()/'mercury_auto_output';out.mkdir(exist_ok=True);shutil.copy2(ipa[0],out/'MercuryAuto.ipa')
  apiFolder=root/'private_keys';apiFolder.mkdir();apiPath=apiFolder/('AuthKey_'+os.environ['KEY_ID']+'.p8');apiPath.write_text(os.environ['API_KEY']);apiPath.chmod(0o600)
  run('xcrun','altool','--upload-app','--type','ios','--file',str(ipa[0]),'--apiKey',os.environ['KEY_ID'],'--apiIssuer',os.environ['ISSUER_ID'],cwd=root)
  print('Mercury Auto signed IPA uploaded. Apple processing still required.')
 finally:
  subprocess.run(['security','delete-keychain',str(keychain)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  for file in installed:file.unlink(missing_ok=True)
