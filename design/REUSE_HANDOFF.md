# Reuse handoff — future-contract candidate proposal

**Status:** Proposed by the C-08-1 design rehearsal, 2026-10-29; Candidate-only future proposal, NOT an original user decision, implemented format or service. All examples, people, utterances, values, permissions and approvals are **SYNTHETIC**. I use “should” below for a proposed future contract, not an existing Stage 1 obligation.

## 1. Boundary and source authority

Stage 1 remains public STRENDA Export XML → EnzymeML, evidence file and not-mapped report. It does not become a mixed-file parser or a thermal-data standard. The current locator is XPath 1.0 into input XML, not a worksheet/page locator. This proposal adds no parser, agent, runtime, UI, exchange service, mandatory signature or new approval role.

| Source clause (immutable baseline line anchors) | Standing preserved here |
|---|---|
| `OPEN_QUESTIONS.md` Q1, lines 9–14 | Decided source/split; arbitrary-file support is not established by Stage 1 results. |
| `ARCHITECTURE.md` Principles, lines 35–40 | Human-centered and standards-aware principles; linked companions are outside the EnzymeML-only initial pilot. Architecture describes a proposed, unimplemented system (Status, lines 3–5). |
| `ISSUE_FORMAT.md` §2, line 30; §8.1, line 434; §8.2, lines 442–454 | Decided v0.10 locator/evidence rules. Retention is possible; complete mapping or complete omission detection is NOT guaranteed. |
| `ISSUE_FORMAT.md` §6, line 308; §7.2, lines 386–403 | Decided: no curator/maintainer approval role or second sign-off; eligible scientist approves exact deliverable, changes invalidate approval, sharing separately needs the owner, approval does not establish numerical suitability. |
| `design/ROLES.md` §4.1, lines 192–197; §4.2, line 203; §4.3, lines 230–234 | Preliminary Stage 1 design follows scientist authorship/actions and separate owner exchange authority. Technical preparation confers neither authority. |
| `design/HANDOFFS.md` §7.8, line 838 | Proposed Stage 2 exchange; Stage 1 specifies no exchange handoff format. |
| `design/WORKFLOW.md` §9.7, lines 828–837 | Proposed Stage 2, “if ever”: internal revocation/history, not recipient awareness or remote recall. |
| `OPEN_QUESTIONS.md` Q6–Q7, lines 48–58 | Owner conditions/researcher review remain open; identity checking, review interface and several sign-offs are proposed Stage 2. |

The immutable provenance ledger outranks design documents (`design/PACKAGE_ADOPTION.md` §3, lines 25–35). This document neither edits it nor upgrades proposed/open clauses. Any future companion mapping or handoff still needs its own design disposition; there is no chosen companion schema here.

## 2. Minimum useful packet, scoped to an allowed use

The existing named person doing technical maintenance/preparation should assemble the following **small description**, using the scientist's and owner's original statements. “Technical maintainer” below describes that task, not a new record-action or approval role. If nobody can prepare it, identify that missing producer and use the retention fallback, not an implied completed handoff.

1. **Identity and coverage:** package/revision, exact member versions or byte fingerprints where available, intended recipient/use, included/mapped/retained/unavailable items, and explicit limits on completeness. Identify the EnzymeML document/evidence/not-mapped set separately from unstandardized supplements. A fingerprint proves identity only.
2. **Source and access per claim:** source/member identity, locator in its actual representation, exact excerpt or attributed human statement, what the recipient can actually open, what is absent/restricted, and an authorized way to request more (or “none known”). State whether comparison with the original was performed, by whom and against which supplied original; otherwise **not independently verified against original**. No invented hash for inaccessible bytes. Links and excerpts are not access to their originals.
3. **Scientific and representation status:** extracted vs human-stated, draft vs approval of a named exact deliverable vs historical/corrected status; coverage of that status; companion mapping/validation absent, pending or evidenced. No whole-bundle approval from one slice. Approval and formula validity do not authorize a numerical target.
4. **Permission and status cut-off:** the owner's attributed grant, exact covered material, recipient/purpose/exclusions and applicability as of the stated exchange; separate science and rights notices known as of an explicit event/cut-off. Unknown later status stays unknown. Record notice destination and preparation/delivery evidence separately. No receipt, reading or acknowledgment without evidence.
5. **Useful outcome and next step:** say what this packet permits the recipient to do now, what it cannot support and the smallest authorized request for a stronger claim. Do not demand every original or a chosen companion schema to discuss a clearly labelled synthetic teaching example.

**Adequate for which use?** A packet may support conceptual teaching about a synthetic claim with internal quotations and explicit missing originals. It is inadequate for independent original-source verification when the originals are absent. A source-unavailable label does not make a source verified, false, scientifically invalid, or automatically unusable for teaching. If the user asks specifically to audit the original or fit an empirical model, the missing original or missing observations/methods can become blocking for that purpose. Changing purpose also requires applicable owner permission; numerical readiness is a separate, still-open integration question.

## 3. Producers and no-schema fallback

| Existing responsibility | Proposed minimal future task; authority not added |
|---|---|
| Scientist / named person working on the record | Supply assay identity or intended scientific interpretation only if genuinely missing; author scientific corrections and their basis; approve a changed EnzymeML deliverable only through the existing review/re-check route. Do not ask the scientist to learn a schema to retain known thermal context. |
| Data owner | Decide access/exchange scope and later rights changes. The scientist's interpretation does not grant sharing rights. Status notices themselves must respect applicable disclosure permission. No implicit permission to expose restricted evidence. |
| Person doing technical maintenance/preparation | Inventory members, preserve source/access/status and exact original messages; offer a documented mapping/validation proposal if a future representation is pursued; assemble a permitted packet or permitted notice for known recipients. They cannot select scientific truth, approve science or grant rights, and cannot assert delivery or reading without evidence. |

**Fallback when no companion is selected:** “I can keep the kinetic draft and retain the thermal excerpt with its assay context. No companion mapping is selected or validated; the thermal result is not an interoperable kinetic record. You do not need to choose a schema to keep this material.” If a future mapping is proposed, its preparer should supply candidate schema/version, mapped meaning, losses and evidence of any actual validation; “none identified” is a valid outcome. This is optional subsequent design work, not a prerequisite to retaining an independent kinetic slice. No implemented capability is inferred from a proposal.

Future source coordinates such as “thermal note, line 2” are descriptive references, **not valid Stage 1 XPath evidence entries**. Under the existing XML-only contract use its actual XML locators/not-mapped entries; do not relabel CSV, PDF or workbook coordinates as XPath. No claim that every source fact was retained follows from an inventory.

## 4. New downstream interaction: partial bundle, no chosen companion

The following is a **single-author scripted role-play**, not a blind reuser test. No XML/CSV/workbook/vendor bytes are parsed, no validated EnzymeML is generated and nothing is exchanged. `PX08` is independent of K08-01, K08-03 and the teaching adjudication: their values, permissions and ledger are unchanged.

**SYNTHETIC reuser:** “Can I use PX08-v1 to explain why turnover and unfolding are different? I also want to check the original fit.”

**Technical preparation, proposed packet (not an EnzymeML instance):**

```json
{
  "package": "PX08-v1",
  "use": "conceptual teaching to SYNTHETIC Reuser R only",
  "coverage": "partial; no whole-bundle completeness claim",
  "kinetics": {
    "claim": "kcat 9 s^-1; assay K, pH 7.1, 25 °C",
    "source": "fit-summary-v1.csv, row 2",
    "quote": "K,kcat,9,s^-1,7.1,25",
    "access": "quote supplied; original CSV absent",
    "original_comparison": "not performed in this rehearsal",
    "status": "draft; no scientific approval"
  },
  "thermal": {
    "claim": "unfolding midpoint 52.6 °C; not kinetics",
    "source": "thermal-note-v1.txt, line 2",
    "quote": "Unfolding midpoint 52.6 °C; fluorescence; no kinetic fit.",
    "access": "attributed excerpt supplied; full note absent",
    "original_comparison": "not performed in this rehearsal",
    "companion_schema": null,
    "validation": "none; retained source context only"
  },
  "raw_fit": {
    "source": "raw-fit-v1.vendor",
    "access": "restricted and not supplied",
    "content_hash": null,
    "scientific_content": "unknown"
  },
  "rights_ref": "SYN-PX08-G1",
  "status_as_of": "PX08-E04; no later status known",
  "science_notice": null,
  "rights_notice": null,
  "source_verification": "not independently verified against originals"
}
```

**SYNTHETIC owner G1 (fixture assumption, no real permission):** “For this independent fictional example, I permit conceptual discussion of PX08-v1's draft claims and quoted excerpts with SYNTHETIC Reuser R only, retaining all labels and limits. I do not permit publication, redistribution, original-source disclosure or numerical execution. I permit minimal status-only notices about PX08-v1 to R without restricted content. No real exchange is authorized.” This grants no authority over any other bundle; it does not make the draft an approved Stage 1 exchange.

**Preparer:** “You can discuss these labelled draft claims within that fictional teaching scope. You cannot independently check the original fit from these quotations. The thermal item has no companion representation. Please request an authorized readable fit summary and its provenance from the owner via the existing agreed contact, if one exists; do not send credentials. Until obtained, mark the original-source check unavailable, not verified.”

**SYNTHETIC reuser:** “I will describe two attributed draft claims, not validated measurements or an approved kinetic record. I can explain the distinction, but cannot audit the original fit or run a model. I am not required to choose a thermal schema.” This readback is authored, not measured user success.

The same packet with `source_verification: "verified"` would be a concrete overclaim: it changes no access or verification evidence. Conversely, refusing the narrowly allowed conceptual discussion solely because the original CSV is absent imposes a stronger, unrequested source-audit gate. If R asks for **original-source verification**, the very same absence now blocks that expanded request; the permitted teaching scope is not silently widened.

## 5. Two later notices, two different consequences

Each notice should name affected package/version/claims, original author/message, scientific **or** rights scope, event/effective order, replacement reference or “none supplied,” permitted destination and known delivery evidence. The preparer records an attempted or prepared message as such, not as received. If no authorized recipient route is known, record “not sent; route/permission unavailable,” preserve the warning locally and identify the unresolved next contact. Do not invent a new notification service, recipient acknowledgment requirement or remote recall.

### A. Scientific correction first; rights unchanged

**SYNTHETIC scientist C1:** “In PX08-v1 the kcat 9 s^-1 was attached to the wrong fit. Do not treat it as a reviewed current kinetic value. I have not supplied a replacement. This correction does not concern the separate thermal excerpt and does not change sharing permission.”

**Preparer's proposed status-only notice to R:** “PX08-v1 / kinetics: scientist C1 reports the wrong fit association. No replacement supplied; original fit still unavailable. The existing teaching permission is unchanged by this scientific message. Thermal context remains unvalidated, not newly approved.”

**Scripted consequence:** the held v1 bytes still contain 9; known scientific status now warns against using that as a reviewed current result. A replacement draft needs evidence and the existing re-check/review route; no v2 value or approval is invented. No notice was actually sent or read in this rehearsal.

### B. Separate owner withdrawal; no scientific correction inferred

**SYNTHETIC owner W1:** “Effective PX08-E10, I withdraw G1 for new handouts, redistribution or new teaching use of PX08-v1 and its quoted excerpts. The limited permission for status-only notices to R remains. This does not delete an existing copy, retract the scientist's correction, or prescribe what happened before this message.”

**Preparer's proposed separate notice to R:** “Do not make new uses covered by the withdrawn permission or new deliveries under G1. Keep the rights warning separate from C1's scientific warning. No claim is made that your stored copy was erased or that you read this message.” Do not infer legal retroactivity or deletion obligations; resolve actual conditions with the owner if needed.

**Scripted consequence:** new teaching/redistribution under G1 is no longer allowed within this fiction; local content identity and the C1 scientific status do not change. In a **rights-only branch** without C1, W1 still stops the scoped new uses but supplies no evidence that 9 is scientifically wrong. In a **science-only branch**, C1 withdraws reliance on the kinetic claim without withdrawing G1. Both branches keep recipient knowledge unknown absent evidence.

The producer may know C1 and W1 while a recipient holding the old packet knows neither. “Notice prepared” or “delivery unknown” is not “recipient informed.” A later permitted receipt could establish receipt, not reading, agreement, erasure or acknowledgment of a replacement. There is no pretend recall or freshness service.

## 6. Basis and limits of this proposal

Accepted verification records F-K08-02 and F-K08-04 as **future requirements**, not current-stage verified defects (`execution/tasks/V-K08/1/assessment.md`, lines 7–16; detailed sources/traces in its `findings.json`). Their existing cases supplied no enacted recipient notice sequence. This script fills a design-witness gap, not that behavioral evidence gap.

The separate reuser adjudication explicitly distinguishes internally traceable quotations from inaccessible originals (`execution/tasks/V-ADJ-02/1/reuser_interaction.json`, Q03, lines 87–92) and accepts the bounded conceptual teaching purpose without a universal original-source gate (Q07, lines 227–232). Its original fictional recipient/material/purpose and exclusions remain untouched. This proposal does not repair that teaching packet, authorize actual distribution, certify schema validity, or establish empirical/numerical readiness.
