# iEnergy & iData for iPhone

iPhone application for https://ienergy-idata.com using SwiftUI and WKWebView. Website content stays current without repackaging the app. Includes Home, Back, Reload, pull-to-refresh, sharing and a connection error screen. External links open through iOS. WebKit uses its standard persistent website data store.

## Identity
- App Store Connect app: 6831976341
- Bundle ID: com.ienergyidata.ios
- Target and scheme: iEnergyIData
- Minimum iOS: 17
- Internal TestFlight group: iEnergy Internal Testing

## Build
Install XcodeGen on a Mac, then run:
```sh
xcodegen generate
xcodebuild -project iEnergyIData.xcodeproj -scheme iEnergyIData -sdk iphonesimulator -destination 'generic/platform=iOS Simulator' CODE_SIGNING_ALLOWED=NO build
```

GitHub Actions generates the app icon and asset catalog before generating the Xcode project. Pushes to main build the simulator app. Simulator compilation succeeded with Xcode 26.3.

## TestFlight
Manually run the iEnergy iOS Build and TestFlight workflow with upload_testflight enabled. The workflow archives without development signing, then uses automatic App Store distribution signing at export.

Repository variables:
- APPLE_TEAM_ID
- APPSTORE_ISSUER_ID
- APPSTORE_API_KEY_ID

Repository secret:
- APPSTORE_API_PRIVATE_KEY

Never commit API private keys or signing credentials. The API key is stored as an encrypted repository secret and the temporary runner file is removed after every run.

App Store Connect processing, an installable TestFlight build, device testing and App Review are separate milestones. Check the current workflow result and App Store Connect before claiming a build is available. Public release also needs final metadata, privacy answers, screenshots, age rating and review.
