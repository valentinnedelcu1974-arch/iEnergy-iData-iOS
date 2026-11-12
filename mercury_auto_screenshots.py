import shutil,os,json,base64,tempfile,subprocess,urllib.request,zipfile,io,plistlib,datetime,time
from pathlib import Path
import jwt
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
assets=json.loads(os.environ['ASSETS'])
print('::add-mask::'+assets['password'])
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
 def run(*args,**kwargs):
  result=subprocess.run(args,**kwargs)
  if result.returncode: raise RuntimeError('Simulator command failed: '+args[0])
 run('python3','build_assets.py',cwd=project)
 run('xcodegen','generate',cwd=project)
 derived=root/'DerivedData'
 run('xcodebuild','-project','MercuryAuto.xcodeproj','-scheme','MercuryAuto','-configuration','Debug','-sdk','iphonesimulator','-destination','generic/platform=iOS Simulator','-derivedDataPath',str(derived),'CODE_SIGNING_ALLOWED=NO','build',cwd=project)
 devices=json.loads(subprocess.check_output(['xcrun','simctl','list','devices','available','--json']))['devices']
 available=[d for runtime,items in devices.items() if 'iOS' in runtime for d in items if d.get('isAvailable')]
 phones=[d for d in available if 'iPhone' in d['name'] and 'Pro' in d['name'] and 'Max' not in d['name']]
 tablets=[d for d in available if 'iPad Pro' in d['name'] and '13-inch' in d['name']]
 assert phones and tablets,'Required large iPhone/iPad simulators not available'
 output=Path.cwd()/'mercury_auto_screenshots';output.mkdir(exist_ok=True)
 manifest=[]
 chosen=[('iPhone',phones[-1]),('iPad',tablets[-1])]
 mode=os.environ.get('CAPTURE_DEVICES','all')
 if mode=='iphone': chosen=chosen[:1]
 elif mode=='ipad': chosen=chosen[1:]
 for kind,device in chosen:
  uid=device['udid']
  if device['state']!='Booted': run('xcrun','simctl','boot',uid)
  run('xcrun','simctl','bootstatus',uid,'-b')
  run('xcrun','simctl','status_bar',uid,'override','--time','9:41','--dataNetwork','wifi','--wifiMode','active','--wifiBars','3','--batteryState','charged','--batteryLevel','100')
  run('xcrun','simctl','install',uid,str(derived/'Build/Products/Debug-iphonesimulator/MercuryAuto.app'))
  run('xcrun','simctl','launch',uid,'com.ienergyidata.MercuryAuto','--demo')
  time.sleep(3)
  filename=kind+'-Home-Demo.png'
  run('xcrun','simctl','io',uid,'screenshot',str(output/filename))
  manifest.append({'file':filename,'device':device['name'],'content':'Genuine simulator screenshot, clearly labelled demo, no vehicle connected'})
  run('xcrun','simctl','shutdown',uid)
 (output/'manifest.json').write_text(json.dumps(manifest,indent=2))
 print('Real iPhone and iPad screenshots captured; no IPA or source is included.')
