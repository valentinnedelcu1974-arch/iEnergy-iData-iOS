# iReview43 1.0 (8) — App Review response draft

NOT SENT. Do not resubmit while any release gate is open.

Existing app: iEnergy & iData, Apple ID 6831976341; Bundle ID com.ienergyidata.ios; Team F3639777XM. Identity verified in TestFlight Build 6 metadata on 10 November 2026. This is an update of that app, not a duplicate App Store record.

1. Purpose: Build 8 introduces a native local workspace. Users draft project enquiries with project, technology and details; save, delete and explicitly share summaries. An offline educational power-balance lab combines a fixed 70 MW PV capacity with battery dispatch and SOC endpoint constraints. A persistent nine-item commissioning checklist supports status sharing and reset. Theme preferences are local. The official website is a secondary network-dependent view. No automatic enquiry submission, live telemetry, SOC integration or equipment control is claimed.

2. Audience: iEnergy & iData service clients, electrical engineers, project coordinators and commissioning personnel organizing enquiries and checklist status before sharing them. Core local features do not require an account or network connection.

3. Need: The intended benefit is preparing enquiries and checklist status offline in one service-client workspace, with an educational hybrid-energy scenario. Individual calculators and checklists are not claimed to be unique. Evidence that this combination addresses a sufficiently distinct customer need remains to be collected through beta testing; no unsupported market exclusivity claim should be sent.

4. Testing: GitHub Actions run 42839228055, source commit e2ffe0be39066d3400ebc645ed8fb7abeaec441e, passed the macOS 15 Intel/Xcode 26.3 toolchain checks, source syntax/icon checks, deterministic energy-model checks, Xcode simulator build and NativeFlowTests/testNativeFlows with 0 failures (173.139 seconds). The UI test covered creating a request, persistence after app relaunch, the irradiance slider, checklist toggle/reset, scrolling to the free-app notice and clearing local requests. Four original iPhone 16 Pro simulator screenshots (1206 x 2622) were exported. Signing profile identity/expiry checks and IPA archive/export passed. Build 1.0 (8) appeared in App Store Connect as Processing on 10 November 2026. The account holder was added to the internal testing group; this is not proof of installation or device testing. No external Build 8 beta feedback, physical-iPhone results, website login/network-failure tests, accessibility audit or evidence of feedback applied to production is yet available. Do not claim those checks have passed.

5. Product relationship: This update is intended as a standalone client workspace for iEnergy & iData. It does not depend on another app. An evidence-based comparison with other apps in the developer account, including iStar and GRID MANAGEMENT PRO, is still required. Product positioning alone does not establish functional separation.

6. Consolidation: The native functionality could technically be incorporated into another app. The rationale for separate packaging must be supported by actual user needs and an account-wide functionality comparison. Updating the existing iEnergy & iData record avoids creating an additional Bundle ID. The app remains free; no IAP or subscriptions are implemented.

7. Shared account components: Candidate source imports Apple SwiftUI, Foundation and WebKit. The iStar repository README describes offline commissioning handover dossiers, asset/test records, punch items, milestones and JSON/report export. This differs in stated scope from the service-enquiry and energy-learning workspace here, but a README comparison is not a verified account-wide source/binary audit. A complete comparison of source, assets and shipped binaries across the account has not been performed. Disclose verified shared components before claiming an independent implementation. Existing signing credentials identify the same app; they do not prove code or content originality.

8. Third-party reuse: The candidate project declares no third-party package dependencies or commercial-template configuration. This does not establish provenance of every source file, icon or website component. Implementation is AI-assisted. Complete the reuse and licence inventory before certifying originality.

9. Content provider: The official platform is https://ienergy-idata.com/. The account holder previously confirmed content rights. Document the exact relationship between the submitting account and the content provider and whether a client, partner or other entity supplied branding or concept. Do not invent legal entities or claim exclusive manual authorship.

## Remaining release gates
- Xcode simulator build and UI tests passed for source commit e2ffe0be39066d3400ebc645ed8fb7abeaec441e; any later source changes require revalidation.
- Privacy manifest included in actual binary; dedicated published privacy policy and portal data audit.
- Valid certificate/profile identity, expiry and signed archive; TestFlight processing.
- Genuine device tests and beta feedback; accessible layouts and portal authentication/network failure handling.
- Actual App Store screenshots at accepted resolutions; original screen recording if needed.
- Verified account-wide comparison and provenance/licence inventory.
- App Store name, metadata, price zero, age rating, rights and privacy declarations consistent with final binary.

No App Review submission or message is authorized by the existence of this draft. User requested preparation and prohibited review before mandatory verification is complete.
