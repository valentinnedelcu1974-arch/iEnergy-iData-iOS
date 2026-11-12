# iReview43 for iPhone — Build 9 candidate

Native offline energy-project enquiries, a commissioning checklist, and a 24-hour PV/BESS dispatch study with SOC integration, one-way efficiency, AC battery rating, an export cap, storage/no-storage comparison, hourly results, local scenario retention and CSV export.

## Active source and identity

- Active source package on this branch: `iReview43_Build9_Source_Candidate.zip`.
- App Store Connect: 6831976341.
- Bundle ID: `com.ienergyidata.ios`.
- XcodeGen project / scheme: `iReview43`.
- Platform: iPhone, iOS 17+.
- Version: 1.0 (9), free.

Extract the source archive, enter `iReview43/`, and generate the project with `xcodegen generate`. The root `.github/workflows/ireview43-validation.yml` performs this extraction, compiles on macOS 15 Intel / Xcode 26.3, runs model and native UI checks, and exports genuine simulator screenshots. Its validation job has read-only repository permissions and no signing/upload step.

## Validation

Run 43317855812 passed compilation, source/model checks and NativeFlowTests/testNativeFlows (0 failures, 74.875 seconds) for the privacy/version-corrected source at 9abedca. A Home header clipping fix was then made at a8775f7. Final run 43319968694 passed compilation, model checks and the native UI flow (0 failures, 396.110 seconds), with automation idle delays noted for physical-device follow-up. Genuine screenshots are retained in the run artifacts.

See `iReview43_Build9_Validation.md` and `iReview43_Build9_Apple_Response_DRAFT.md` for the evidence inventory and the outstanding App Review questions. Drafts are internal preparation, not messages already sent to Apple.

## Distribution

Build 9 signing/TestFlight upload requires approval to use the existing iReview43 Apple Distribution material and App Store Connect credentials. No signing workflow has been committed or executed for Build 9. Successful simulator validation, signed IPA export, TestFlight processing, physical-device beta feedback and App Review are separate milestones.

The repository main branch is used for Mercury Auto with a separate Bundle ID. Keep iReview43 changes isolated on `fix/ireview43-apple-review`; deploy from its active source archive.

## User data and assumptions

Drafts, checklist, appearance and one saved scenario remain in local app preferences until explicit sharing/export. The native app includes privacy information and local deletion controls. The optional service website opens in the system browser. The study uses a synthetic clear-day PV curve and constant demand; it is educational, not equipment control or grid-code certification. Initial stored energy can be consumed, and final SOC is not forced to equal the initial value; the comparison is not an economic-savings claim.
