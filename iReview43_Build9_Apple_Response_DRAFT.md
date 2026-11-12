# iReview43 — factual App Review response preparation

NOT SENT. Complete the evidence gaps below before using this as a final response. This draft covers Guidelines 4.3(a), 4.3(b) and 4.2.6. Do not assert guaranteed originality, market exclusivity or approval.

## 1. What the app does and the problem it solves

iReview43 is a native offline workspace for preparing energy-project enquiries and examining illustrative PV/battery dispatch scenarios. In the Build 9 candidate, a user sets PV rating, constant demand, battery energy capacity, battery AC power rating, initial SOC, one-way efficiency and a grid export cap. The app computes 24 hourly AC power balances and integrates battery stored energy. It constrains storage energy and battery power, calculates imports, exports and curtailed PV, compares the case with a no-storage baseline, displays the stored-energy curve and hourly results, and exports a CSV. A scenario can be saved locally and restored. Project enquiries can be drafted, saved and explicitly shared; a local commissioning checklist can be maintained and shared.

The calculation is a reproducible educational screening exercise. It does not use live telemetry, control equipment, forecast weather, perform grid-code certification or certify commissioning. The website is an optional external browser link, not an embedded replacement for native features. Native records are not automatically submitted to a server.

## 2. Intended audience

The intended users are electrical/renewable-energy engineers, commissioning and project coordinators, and users preparing a technical enquiry for iEnergy & iData. The implemented workflow is for exploring how PV surplus, demand, storage limits and an export cap interact, then retaining or sharing the numerical results. The app requires no account or other installed app for its local functions. This describes intended use, not a claim that user demand has already been measured.

## 3. Need and differences

The concrete workflow added in Build 9 combines constrained 24-hour storage calculations, an explicit no-storage comparison, accessible hourly values, local scenario retention and CSV output in the existing app. This replaces the earlier Energy Lab's static instantaneous power sliders. All assumptions and comparison limits are visible, including the effect of initial stored energy and the absence of an equal-final-SOC requirement.

EVIDENCE GAP: provide the final-device demonstration and actual user feedback on this workflow. Do not claim no competing app offers similar calculations. Comparison with GRID MANAGEMENT PRO remains incomplete because its application source is not currently available in the accessible repositories. Apple may still consider consolidation appropriate.

## 4. Beta testing and applied feedback

Build 9 source/icon checks, model checks, Xcode simulator build and one native UI flow passed in run 43317855812 for source commit 9abedca. The UI flow passed in 74.875 seconds with zero failures. It exercised request persistence across relaunch, study navigation/PV slider interaction, checklist toggle/reset and request deletion, and exported genuine iPhone 16 Pro simulator screenshots. Mathematical tests verify AC and stored-energy balances, SOC/power/export bounds and edge cases. A later Home layout fix is being revalidated separately; cite its final run and actual result before submission.

App Store Connect showed one installation of TestFlight Build 8, with no recorded feedback values. An installation count is not qualitative feedback. No external tester quote or feedback-driven production change is claimed. Removing embedded web content, correcting the displayed version/privacy controls and correcting a clipped Home subtitle were source/visual audit findings, not external beta feedback.

EVIDENCE GAP: install the final Build 9 candidate on a physical iPhone, record device/iOS, tested flows, observed results and actual feedback, then document the corrections prompted by that feedback. Do not invent tester numbers or feedback examples.

## 5. Standalone product and related apps

The app operates independently and uses its existing App Store record (6831976341 / com.ienergyidata.ios). It is associated with the developer's iEnergy & iData platform. A source comparison with iStar shows a different principal data model: iStar records commissioning dossiers, tagged assets, evidence notes, punch items, milestones and JSON/report exchange; the new iReview43 study models hourly PV, load, battery power, stored MWh, grid exchange and curtailment. Generic project/checklist concepts still overlap in domain.

EVIDENCE GAP: complete comparison with the rest of the developer account before claiming every related product is sufficiently distinct.

## 6. Why functionality is separate

The functionality could technically be incorporated into another energy application. Updating the existing app record avoids creating another record simply to resubmit rejected content. The intended separation is scenario exploration/enquiry preparation here versus evidence/handover dossier management in iStar. That rationale must be supported by actual audience/workflow evidence and the remaining account comparison; a different name, icon or data model alone is not a complete justification.

## 7. Shared components within the account

In the two inspected source packages, iReview43 and iStar use standard Apple SwiftUI, Foundation and UniformTypeIdentifiers, plus native sharing/file export mechanisms. iReview43 also uses Apple Charts. Each inspected package contains eight Swift files; there are no byte-identical Swift files between them, and the inspected app icons differ by image hash and visual design. This result does not exclude shared boilerplate or smaller snippets. Generic Apple UI patterns are not presented as proof of product originality.

EVIDENCE GAP: finish the broader source/assets/binary inventory before asserting the absence or exact extent of shared nonstandard components throughout the account.

## 8. Third-party code, templates and provenance

The inspected Build 9 XcodeGen project declares no external package dependencies, app-generation SDK or vendor content library. It uses Apple frameworks. Implementation is AI-assisted; do not claim exclusive manual authorship. The existing iReview43 record and source history were retained, rather than creating a new app identity to avoid rejection. Historical wrapper code remains in repository history but is not the candidate's entry point; the native project builds from iReview43/Sources.

EVIDENCE GAP: verify provenance/licences for the legacy icon and any supplied content before making ownership/licence certifications. No assertion about every third-party app or every historical website asset is supported by this source inspection.

## 9. Content provider and submitting account

The application refers to iEnergy & iData and its official website. The submitting account is IULIAN VALENTIN NEDELCU. Prior project context states the account holder confirmed content rights, but that does not establish the exact legal/provider relationship or whether a client supplied content, concept or branding.

EVIDENCE GAP: obtain the account holder's factual statement of ownership/permission, whether any client or partner supplied concept/branding/content, and the reason the app is submitted from this account. If a separate client is the content provider, explain the actual relationship and comply with Apple's requested submission route. Do not invent an entity or deny third-party involvement without confirmation.
