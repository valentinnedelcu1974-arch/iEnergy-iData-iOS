# iReview43 Build 9 — verified progress, 13 November 2026

App Store Connect: 6831976341. Bundle ID: com.ienergyidata.ios. Branch: fix/ireview43-apple-review. Source archive commit: 9abedca698e302e2510e9c25e2605b4280b8b42e. Main/Mercury Auto unchanged.

## Implemented

- Native one-hour-step, 24-hour PV/BESS dispatch study with integrated stored energy, AC battery rating, one-way efficiency and export cap.
- Storage/no-storage comparison, import/export/curtailment totals, stored-energy chart and exact hourly results.
- Scenario save/restore and CSV export.
- Dedicated native privacy explanation and local deletion controls for requests, saved study and checklist.
- Runtime app version display. Embedded WebKit portal removed; website opens separately through a system Link.
- Synthetic profile, constant load, initial/final energy comparison and model limitations stated in the app.

## Validation evidence

GitHub Actions run: https://github.com/valentinnedelcu1974-arch/iEnergy-iData-iOS/actions/runs/43317855812

macOS 15 Intel, Xcode 26.3. Source/icon checks passed. Energy-balance and dispatch-model tests passed, including hourly AC balance, stored-energy balance, zero/full/empty capacity cases, AC power rating, export cap, disabled storage, nonfinite input handling and CSV row count. Xcode iOS simulator build passed.

NativeFlowTests/testNativeFlows passed with 0 failures in 74.875 seconds. The UI flow exercised request creation, saved-request persistence after app relaunch, Energy Lab/Dispatch Study navigation and PV slider response, checklist toggle/reset, free-app notice, request deletion and screenshot attachments. This does not constitute physical-iPhone or external beta testing, and does not exhaustively test CSV destination handling or study save/restore.

Run 43317372163 compiled the earlier source and passed model checks; it was intentionally cancelled after source replacement. It is not the final validation run.

## Verified comparison with iStar source

The current iStar-iOS main source package was inspected read-only. Both projects use Apple SwiftUI/Foundation/UniformTypeIdentifiers and native sharing/file-export mechanisms. iReview43 additionally uses Apple Charts. No external package dependency is declared in the inspected XcodeGen projects. Eight Swift source files were compared in each package: no byte-identical Swift file. Icons differ by SHA-256 and visual design. This does not prove that no common boilerplate or snippets exist.

iStar's concrete models concern dossiers, tagged assets, test status, evidence notes, punch items, dated milestones and JSON archive/report exchange. iReview43's concrete model added here concerns hourly PV, load, battery power, stored MWh, grid exchange and curtailment. The generic project/checklist areas still overlap in broad domain. No certification of a complete account-wide binary/code audit is made. GRID MANAGEMENT PRO source was not found among the currently accessible repositories; its support repository alone is insufficient for code comparison.

## Apple's nine questions — response preparation status

| Question | Verified basis | Remaining evidence |
|---|---|---|
| 1. App purpose/problem | Offline draft preparation, checklist and now integrated PV/BESS scenario calculations | Final device demonstration |
| 2. Intended users | Engineering/project coordination workflows implemented in source | Actual intended-user beta evidence |
| 3. Market need/difference | Demonstrable 24-hour model, constrained dispatch and CSV workflow | Avoid market exclusivity claims; evidence from real users and comparison with GRID MANAGEMENT PRO |
| 4. Beta testing and applied feedback | Model tests and successful simulator/UI flow; Apple TestFlight Build 8 shows one installation | Actual feedback from tester(s), devices/iOS and any changes prompted by that feedback; new Build 9 device tests |
| 5. Relation to developer's apps | Standalone runtime; concrete iStar source comparison above | Account-wide scope comparison remains incomplete |
| 6. Consolidation rationale | Existing app record retained; functionality could technically be consolidated elsewhere | Fact-based reason for maintaining a separate product |
| 7. Shared account components | Shared standard Apple frameworks/native controls; no byte-identical file in inspected iStar packages | Remaining account source/assets/binaries and any shared snippets |
| 8. Third-party provenance | AI-assisted source; no declared external package in inspected project | Confirm legacy icon/content provenance before claiming ownership/licensing certainty |
| 9. Content provider | App refers to the account holder's iEnergy & iData platform in project context | Exact account-holder/content-provider relationship and any client-supplied branding/concept must be confirmed |

Do not send invented beta feedback, market claims, authorship claims or a claim of zero shared code. The new study is a substantive change; Apple alone decides whether it sufficiently resolves 4.3/4.2.6.

## Distribution state

Build 9 is not signed/uploaded/submitted by this session. Existing TestFlight Build 8 was observed with one installation and no recorded sessions/crashes/feedback values. A separate Build 9 signing/upload workflow was prepared locally with exact-source validation, matching-team/profile checks, temporary credential handling and cleanup. Its browser upload was blocked by automatic approval review because browser-based source upload authorization did not explicitly cover credential-backed TestFlight distribution. It was NOT committed or run; no signing credentials were changed or certificates revoked.

The App Store Connect TestFlight page loaded; the Distribution page remained without its main content. No App Review message or metadata was changed. Remaining steps: approve use of existing iReview43 signing credentials and TestFlight upload; upload/process Build 9; test on a physical iPhone and collect factual feedback; complete the outstanding ownership/comparison evidence; update final store assets/metadata and reply to all nine questions before the chosen review route.
