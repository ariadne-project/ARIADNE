# Explicit arrays and assay context — candidate review proposal

**Status: proposed, design-rehearsal review guide only.** C-06-1 proposes this text for manager consideration; it is not an actual user decision, a change to Issue format 0.10, implemented software, a current Stage 1 assurance guarantee or a new approval condition. Existing source authority and scientific/approval rules remain unchanged.

## Scope

I limit this guide to a source that explicitly supplies a time list and a data list intended for one series, and to a stated or missing relationship between that series, an assay and a parameter group. It does not require a general scientific plausibility checker, infer a new rate model, supply missing measurements or make arbitrary files usable by Stage 1 XPath contracts.

### Candidate disclosure requirement for a future review contract

When those explicit lists are offered as a reusable paired series, show the two counts and the basis for their assay relationship: **source-stated**, **human-stated** or **not established**. Keep “copied faithfully”, “evidence-entry format checked”, “citation checked”, “EnzymeML checked”, “scientifically reviewed” and “approved” separate. Report only checks actually run, on the files and relationships they cover. Matching counts are necessary for this ordinary one-to-one representation, not sufficient proof of pairing or scientific validity. A source may deliberately represent missing observations differently; this guide does not redefine such a representation as erroneous.

If the counts differ or the assay relation is not established, preserve the lists and source wording and disclose the exact limitation. Do not offer that material as an established paired assay series. That is a claim-scope rule, not a new run state, blocking issue kind, authority, mandatory specialist sign-off or prohibition on retaining useful source material. A named person may review the limitation using the existing human-review/structural-edit path where applicable. If the issue definitions do not fit, do not invent a registered issue or force an inquiry turn; keep an explicitly scoped review note instead. This proposal specifies no new storage schema or automated detector.

**Example: unequal lists**

> S1 contains times [0,10,20,30] s and concentrations [0.20,0.16,0.12] mmol/L. I copied every number. There are four times and three concentrations; the unpaired observation is unresolved. I have not trimmed, padded, interpolated or approved it as a paired series.

**Example: equal lists, absent context**

> S1 has three times and three concentrations, but the source does not assign it to assay A at pH 7 or assay B at pH 8. The fit parameters are explicitly from assay A. I will not infer that S1 belongs with those parameters.

**Example: clean control**

> S1 has three times and three concentrations. The source explicitly pairs them in order and assigns them to assay A. The listed numeric citations and evidence-entry format were checked in this fixture. This is not full-record, model or scientific approval.

### Candidate review scope after changes

A prior review applies only to what it reviewed. If a later proposed edit changes time/data membership or order, assay association, parameter grouping, model-argument assignment, unit scale or quantity role, show that concrete change before reusing the corresponding review claim. Do not withdraw unrelated source citations or require a full review of unchanged facts. This is a proposed disclosure/review practice; no semantic invalidation engine or new product status is defined here.

- Moving only kcat from assay A to B leaves valid ids but breaks an A/A parameter group. Existing rate-law one-context checks apply; do not silently select a different group.
- Moving the whole group to B can restore internal consistency but cannot turn the source's assay-A fit into source evidence for B. A human statement stays human-stated, with its basis.
- Binding a parameter in s^-1 to Km does not become acceptable merely because the parameter unit parses. Existing model-role dimensions apply.
- Changing concentration data to a rate role does not change mmol/L into mmol/L/s or establish that the copied numbers are rates.
- Changing substrate units from mmol/L to mol/L can preserve dimensions but invalidate a previously compatible Km + S scale. Preserve stated values; do not rescale automatically.
- Dropping the final time 30 from the proposed record can make the lengths equal, but omits a source value from that record; the stored input remains unchanged. Any permitted edit needs its basis; existing anonymous-list binding/hold rules and approval invalidation still apply.

The existing design already distinguishes source evidence from a human statement and voids approval on changed approved files. It does not automatically repeat verification-agent scientific review after an edit. Therefore a later clean mechanical check is not a renewed scientific review of the changed relationship.

## Original contracts and authority retained

References below identify the reviewed pre-consolidation snapshot retained in the separate rehearsal evidence archive; use the named sections in the current design.

- `ISSUE_FORMAT.md` §3:54–59: field roles govern emptiness; wrong/conflicting/uncited values can still be issues.
- §3.1:75–86: human-confirmed model bindings, one context, dimensions, scale and no automatic unit conversion; starter-model incompatibility alone need not invalidate the source units or record.
- §4.1:181–195 and §4.2:208: narrow issue definitions, faithfully copied implausibility out of Stage 1 scope, and unregistered concerns passed as human-review notes.
- §6.2:325–338: named-person edits and their source/statement basis; a person's explanation is never source evidence.
- §7.1:350–375 and §7.2:397–403: deterministic rechecks, no automatic verification-agent rerun, live binding holds and changed-file approval invalidation; numerical suitability is separate.
- §8:405–415, §8.1:423–436, §8.2:440–454 and §9:456–470: schema/reference/unit/citation checks and per-element evidence do not amount to a general scientific coherence guarantee.
- `design/HANDOFFS.md` §2.12:437 and `design/WORKFLOW.md` §4.3:304: the existing approval summary is built from stored files and logs; it is not permission to infer a missing relationship, detect every scientific anomaly or certify content. Changes and their basis are shown under an existing design rule, not a newly accepted issue-format rule.
- `design/HANDOFFS.md` §2.3–2.4:145–155 and §7.3:768–778: Stage 1 uses STRENDA Export XML; non-XML locator/parser contracts are future Stage 2 proposals. The same disclosure aim should inform varied future inputs, not imply current support.

## No-change and simpler alternatives

Current Stage 1 can remain unchanged: preserve faithful source material and use existing review/edit/provenance controls. That is the right default if manager integration would otherwise expand scope or imply an automated coherence check. The smaller documentation alternative is one sentence: **“A checked copy is not necessarily a coherent paired assay series; inspect any disclosed list-length or context limitation before reuse.”**

I propose the bounded examples above only because counts, relationships and changed review scope can otherwise be collapsed into a single misleading “validated” label. I make no claim that the current source actually applies such a blanket label, or that this document reduces measured scientist effort. Any adoption remains a candidate proposal, not a scientific or data-owner approval.
