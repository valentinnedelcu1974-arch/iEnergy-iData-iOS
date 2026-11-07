# iEnergy & iData — iPhone

This independent iOS application loads https://ienergy-idata.com directly using WKWebView. The website supplies the content, design, services and navigation. It includes Home, Back, Reload, pull-to-refresh, sharing and a connection error screen. External links open through iOS. Website cookies persist in the standard WebKit store.

Bundle ID: com.ienergyidata.ios
Target: iEnergyIData
Minimum: iOS 17

## Build
Install XcodeGen on a Mac, run xcodegen generate, then:
xcodebuild -project iEnergyIData.xcodeproj -scheme iEnergyIData -sdk iphonesimulator -destination 'generic/platform=iOS Simulator' CODE_SIGNING_ALLOWED=NO build

The GitHub Actions workflow builds on push to main. A manual run with upload_testflight=true attempts signing and upload, using APPLE_TEAM_ID, APPSTORE_API_KEY_ID and APPSTORE_ISSUER_ID repository variables, and APPSTORE_API_PRIVATE_KEY as a secret. A matching app record and signing setup in the existing Apple account are required.

Status: source prepared; Xcode compilation and device testing have not been performed in this Linux workspace. No TestFlight upload has been completed. App icon, website privacy declarations and final distribution review remain required before release.
