# ARIADNE issue format

**Version:** 0.10, the preliminary Stage 1 issue format: version 0.5 decided on 2026-10-20 under interim authority, amended on 2026-10-22 (changes C01 to C11; see the [provenance ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)), on 2026-10-27 (decisions AD-D01 and AD-D04; see the [provenance ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)) and on 2026-10-28 (rate-law unit dimensions, and how `closed_by` and `not_available` are written; see the [provenance ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)) and again on 2026-10-28 (unit-scale compatibility of rate-law bindings; see the [provenance ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)) and once more that day (the boundary for numerical use of rate laws; see the [provenance ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)).\
**Status:** This describes a proposed format for a system that is not implemented. Later versions will be recorded in the ledger. The [changes from version 0.9](#changes-from-version-09), the [changes from version 0.8](#changes-from-version-08), the [changes from version 0.7](#changes-from-version-07), the [changes from version 0.6](#changes-from-version-06), the [changes from version 0.5](#changes-from-version-05) and the [changes from version 0.4](#changes-from-version-04) are listed near the end.\
**Target:** EnzymeML V2.0 at enzymeml-specifications commit bf9321f ([Open questions, Q3](OPEN_QUESTIONS.md#q3---which-enzymeml-target-should-be-tested)), with one documented deviation (section 9).

## 1. Purpose and scope

One issue format is shared by everyone who works on a record:

| Who | What they do with issues |
|---|---|
| Deterministic verifier (software) | Raises issues by checking the record |
| Verification agent | Judges the verifier's issues and adds its own; never edits the record |
| Inquiry agent | Turns open issues into questions, tagged with the issue IDs they address |
| Scientist | Answers questions; one named scientist approves the record |
| Named person working on the record | Handles review items: overrides mechanical issues and makes structural edits (section 6) |

There is no separate curator role. The named person working on a record is normally the scientist, who may answer, correct and approve without switching roles (section 6).

**Guiding question:** which empty fields are asked depends on what makes an approved record **reusable by someone else**, not on what a particular input format happens to supply. The role table (section 3) is an EnzymeML-level policy. It does not depend on the input format.

**A record** is the EnzymeML document plus its evidence file and not-mapped report (Q2.4). Anything EnzymeML cannot hold goes into the evidence file: citations, software rules, "not available" declarations, overrides, approval.

## 2. Basic terms

- **Field:** a property of an EnzymeML object, e.g. `Measurement.ph`.
- **Pointer:** a JSON Pointer into the document, e.g. `/measurements/0/ph`. The one exception is the pointer of a parameter-link issue, which ends in the parameter's link entry (4.1 note 5). Pointers are for software only; scientists never see them (section 5.3).
- **Live pointer:** a pointer that software still uses: in the `fields` of an issue that is not closed, in an evidence entry of the current record, or in a parameter link (4.1 note 5). Each live pointer is bound to the `id` of its nearest ancestor with an `id`, plus the path below that ancestor; a pointer with no such ancestor (a document-level pointer) binds to the document root and its path from the root. Software keeps these bindings per round in the run log. Software also keeps the bindings of closed issues, for re-check matching only (7.1, "On re-check"); they are never used to write. Pointers in stored snapshots, stored questions and answers, and the xpaths of locators are historical, not live, and are never rewritten (7.1, "Live pointers").
- **Locator:** a pair `{xpath, quote}` that points into the input. The `xpath` is an absolute XPath 1.0 location path from the input's root element, for example `/experiment/datasets/dataset[1]/@name`, and must select exactly one node; the `quote` must be a verbatim part of that node's string value (an attribute's value, or all the text inside an element). This holds for every locator: in evidence entries, in not-mapped entries and in an issue's `source_locators`.
- **Empty:** a field is empty if it is absent, `null`, a whitespace-only string, an empty list `[]`, or a unit with neither a name nor base units. `0`, `0.0` and `false` are values, not empty.
- **Omit, don't null:** drafts leave empty fields out. A `null`, `""` or `{}` placeholder in a draft is itself an issue (`wrong_type`).
- **Round:** one pass of checks, questions and answers. Round 1 starts from the extraction agent's draft.
- **Unit companion:** the unit field that belongs to a number field:

  | Number field | Unit companion |
  |---|---|
  | `Parameter.value` | `Parameter.unit` |
  | `Measurement.temperature` | `Measurement.temperature_unit` |
  | `MeasurementData.prepared`, `initial`, `data` | `MeasurementData.data_unit` |
  | `MeasurementData.time` | `MeasurementData.time_unit` |
  | `Vessel.volume` | `Vessel.unit` |

## 3. Field roles

| Role | Asked? | Blocks approval until |
|---|---|---|
| **SOFTWARE** | Never | Not applicable; filled by software |
| **ASK-REQ** | If empty | Filled |
| **ASK** | If empty | Filled, or declared not available with a reason |
| **ASK-IF** | If empty and its rule applies | Same as ASK. If the rule does not apply, the field counts as LIST for that object. |
| **LIST** | Never | Never; an empty LIST field is shown in the report only |

**Rules for all roles**

1. Roles are evaluated per object. Example: the time-unit rule is checked separately for each measured species.
2. Roles govern emptiness only. A wrong, conflicting or uncited value is an issue in any field, LIST fields included, and blocks until resolved.
3. A unit closes only with a value, never with "not available". It is asked only when its number is present.
4. An OR-rule raises one issue that lists all the alternative fields. A value for any one of them closes it, and the remaining alternatives count as LIST.

### 3.1 SOFTWARE fields

A deterministic assembly step fills these. It is part of ARIADNE but separate from the deterministic verifier, which only checks. The assembly step never reads the input. Each software value is recorded in the evidence file with `filled_by: software` and the rule that produced it.

| Rule | Field(s) | What software does |
|---|---|---|
| `S-VERSION` | `/version` | Writes `"2.0"` |
| `S-ID` | Every `id` field | Writes an id string only. Identical unit definitions may share an id. |
| `S-DATES` | `created`, `modified` | Set by the final generation step, before approval |
| `S-UNIT` | Unit internals (`UnitDefinition` name and base units; `BaseUnit` kind, exponent, scale, multiplier) | Built from the unit spelling in the draft or the answer. An extracted spelling keeps the extraction agent's citation, which gets the full citation check (8.2) with letter case kept. A stated unit it cannot derive is never guessed: it is written as the stated spelling, as the unit's name with no base units, keeping its citation, and `C-UNIT` then raises `wrong_unit` at the unit field, not at its internals. |
| `S-VESSEL` | `vessel_id` on Protein, SmallMolecule, Complex | Filled only when the document has exactly one vessel; re-applied after answers. With several vessels the field is LIST. |
| `S-SYMBOL` | `Parameter.symbol` | The parameter's name, when it is a valid symbol (a letter, then letters, digits or underscores) that no other parameter in the record uses; otherwise the parameter's `id` (T9HQ4X states "kcat" twice). Never asked. |
| `S-RATELAW` | The `Equation` in `Reaction.kinetic_law` | Built only from a confirmed rate model with its bindings (below; rule `R-CTX-LAW`, 5.1 rule 3): `equation_type` `rateLaw`, the model's formula with the symbols of the bound parameters and the ids of the bound species as its variables, and `species_id` set to the rate label `v_<reaction id>` (section 9). A species is never replaced by a number, such as one assay concentration. If the bindings fail a check below, nothing is built. |

**Rate-law bindings.** `S-RATELAW` builds an equation only from one confirmed, fully bound option: a model from the starter list (5.1 rule 3) with, for one target reaction, the measurement (dataset) whose context applies; the parameter of the record bound to each parameter argument of the model (for example kcat and Km); and the species bound to each species variable (for example the substrate S and the enzyme E). The inquiry agent proposes which parameter fills which argument; software never assigns these scientific roles, for example from parameter names. The scientist confirms the whole option by answering the rate-law question (5.1 rule 3), or a named person gives it by a structural edit (6.2). Before building, software checks:
1. **Complete:** every argument and variable of the model has exactly one binding, and no parameter is bound to two arguments.
2. **Resolved:** every bound id resolves to exactly one object of the right type: the target reaction, a measurement, a parameter for each parameter argument, and for each species variable a species that takes part in the target reaction. The link entry (8.1, "Parameter links") of no bound parameter is `held` (7.1, "Live pointers"); a held evidence entry elsewhere, for example of a reaction element after its list changed, does not stop the build, but it blocks approval until a named person maps or disposes of it (7.2 condition 5; 6.2).
3. **One context:** the link (8.1, "Parameter links") of every bound parameter names the bound measurement and the species bound as the substrate. A link that names another measurement or species, or that does not name one, fails this check: a binding that no link supports, like a combination across measurements or substrates, is never inferred; it is built only from a structural edit whose basis includes a statement (6.2).
4. **Dimensions:** the unit of each bound parameter, and the data unit of each bound species in the bound measurement, have the dimension the starter list gives, so that the formula has the dimension of the rate. A unit that is missing or cannot be read fails this check, and so does a bound species without a data unit in the bound measurement. A quantity whose stated unit does not fit the starter list, such as a mass concentration (mg/mL) or an activity per enzyme mass (µmol/min/mg), also fails it: its stated value is kept, nothing converts it from mass to amount, and the record is not thereby invalid. A compatible representation that the record states, or an equation that a named person writes by a structural edit (6.2), can resolve the case.
5. **Scale:** where the model adds, subtracts or compares terms, as in Km + S, those terms have the same unit, not only the same dimension, so that the stated numbers can be combined as they are. The starter list names, for each model, the bound quantities that must therefore share one unit (5.1 rule 3, column "Scale"); their stated units, as `S-UNIT` derives them, must have the same base units with the same exponents and the same overall scale. Units that differ only in spelling, such as mM and mmol/L, pass. Quantities that the formula only multiplies or divides need not share a unit, so neither quantities of different dimensions, such as kcat in s⁻¹ and Km in mmol/L, nor the enzyme in µmol/L with the substrate in mmol/L fail this check. If quantities that must share a unit are stated in units of different scale, for example Km in mmol/L and the substrate's data in mol/L, or if the scale of such a unit cannot be read, the check fails: compatibility is never assumed. An exponent is a pure number, so the unit of the Hill exponent n, which check 4 requires to be dimensionless, must also have the overall scale exactly 1 as `S-UNIT` derives it; a dimensionless unit of any other scale, such as %, fails this check, so n = 200 % never becomes the raw exponent 200, while n = 2 with a dimensionless unit of scale 1 passes. A missing or unreadable unit of n already fails check 4. This check is separate from check 4, because units of different scale can have the same dimension.

**Units in the equation.** `S-RATELAW` writes the model's formula with the bound symbols and species ids; it converts no stated value, writes no conversion factor or other number into the equation, and relies on no later software to convert units. The numbers stated for the bound quantities are therefore combined as they are, which is correct only when check 5 passes; the evidence keeps every bound unit, and the approval summary shows them. When check 5 fails, for example for Km = 0.082 mM with the substrate's data in M, or for a Hill n stated as 200 %, no equation is built from that binding: every stated value and unit stays as it is; the units are not thereby wrong, so no `wrong_unit` issue is raised because a starter model cannot combine a unit that `S-UNIT` derives; the record is not marked invalid; and the rate-law issue goes to human review (5.1 rule 3; 6.2). It is resolved by a representation in matching units that the record supports, for example a value that the source also states in the substrate's unit, bound by a confirmed option or a structural edit with its basis, or by an equation that a named person writes by a structural edit and that handles the conversion explicitly (6.2); nothing normalises the stated values. Software never equates the numbers of quantities in units of different scale, such as 0.082 mM and 0.082 M. This adds no automatic conversion of stated values, no conversion factor written by software and no model family (decided on 2026-10-28, [provenance ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)).

**Numerical use.** Checks 4 and 5 establish compatibility inside the formula only: the formula has the dimension of a rate, and the numbers it adds, or uses as an exponent, can be combined as stated. They do not establish that the equation suits a numerical use outside the record. An equation is built, recorded and scientifically reviewed without any claim that it is ready for numerical use in a particular tool. Before it is represented as suitable for a specified numerical use, in particular as the derivative of a species, the unit and scale of the rate it gives are checked against that use: a rate in µmol/L per second is never used as if it were in mmol/L per second for dS/dt. Where no numerical target is specified, no numerical-compatibility claim is made, and the equation is still recorded. Where a specified target does not match, the equation is not passed to that use and nothing converts it; the unresolved compatibility question goes to review by a named person. Approval of the record (7.2) is no evidence of numerical compatibility. How a numerical target and its unit are determined, how an equation is passed to a downstream tool, and any conversion for that use are left to a later decision (section 11; decided on 2026-10-28, [provenance ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)).

These checks show only that the option is well formed. They are no evidence that the model suits the data, or that the binding is the only plausible one: Km, Ki and K₀.₅ have the same dimension, and which parameter plays which role stays the inquiry agent's proposal as the scientist confirmed it. Software builds exactly the confirmed option; it never selects, completes or substitutes a binding. If a check fails, `S-RATELAW` builds nothing, the run log records the option and the failed check, and the rate-law issue goes to human review (5.1 rule 3). The checks first run when the confirming answer or structural edit is applied to the working copy (7.1, step 6, and "Working copy"); a failure then is this case: nothing is built, the issue does not close, and it goes to human review. Re-validation repeats them at each later commit (7.1 step 7).

**Re-validation.** Each time `S-RATELAW` is applied again (7.1 step 7), software repeats the checks and compares each bound object with the record as it stood when the option was confirmed (for an answer, the round snapshot its question was asked on; for a structural edit, the working-copy version the edit produced, 7.1 "Working copy"): its id; for a bound parameter, its name (`Parameter.name`) and any other description of it that the option's label showed; the context its link names; its value and unit; and each bound species' part in the reaction. This compares what was shown with what the record now holds and never reads a name as a role. If any of these changed, or a check fails, the option no longer stands for the confirmed choice: software removes the equation it built from it (a held evidence entry of that equation stays held until a named person disposes of it, 6.2), builds nothing and never rebinds, and the rate-law issue, found again on re-check, is asked again (7.1, "On re-check"). A pointer that moved while its object's id and content stayed the same needs no new confirmation. The evidence keeps the model, the bindings and the answer or edit that confirmed them, so whether each binding rests on a cited link or on a human statement stays visible (8.1).

**Not software:** which species something refers to is an extracted fact with a citation. This covers `species_id` in ReactionElement, ModifierElement and MeasurementData, and `Complex.participants`. If an empty reference is required (`species_id`), it is ASK-REQ and is asked as a choice among the record's species; an empty `Complex.participants` is LIST (3.5).

### 3.2 ASK-REQ fields

All fields the schema requires that are not SOFTWARE fields:

| Object | Fields |
|---|---|
| Document | `name`, `creators` (at least one), `vessels` (at least one) |
| Creator | `given_name`, `family_name`, `mail` |
| Vessel | `name`, `volume`, `unit`, `constant` |
| Protein, SmallMolecule, Complex | `name`, `constant` |
| Reaction | `name`, `reversible` |
| ReactionElement | `species_id`, `stoichiometry` |
| ModifierElement | `species_id`, `role` |
| Measurement | `name` |
| MeasurementData | `species_id` |
| Parameter | `name` |
| Equation, Variable | All required fields, only if such an object exists and was not built by software |

**Added by ARIADNE policy** (the schema does not require it): `Reaction.reactants` must have at least one entry.

**Creators** are the people who prepared and approve this record, including the answering scientist. The authors of the underlying paper stay reachable through the DOI in `references`. `Creator.mail` may be a functional address, such as a group mailbox, because names and e-mail addresses are personal data released with every record.

### 3.3 ASK fields (always asked if empty)

| # | Field | Rule |
|---|---|---|
| A1 | `Parameter.value` | `R-REC` |
| A2 | `Parameter.stderr` (not available is expected often) | `R-REC` |
| A3 | `Measurement.ph` | `R-REC` |
| A4 | `Measurement.temperature` | `R-REC` |
| A5 | `Measurement.species_data` (at least one entry; ARIADNE policy) | `R-REC` |
| A6 | `MeasurementData.prepared` | `R-REC` |

### 3.4 ASK-IF fields (asked if empty while the rule applies)

| Rule | Field(s) | Applies when | Notes |
|---|---|---|---|
| `R-ID-PROTEIN` | Protein `references` OR `sequence` | Both are empty | OR-rule: one issue |
| `R-ID-MOLECULE` | SmallMolecule `references` OR `inchi` OR `inchikey` OR `canonical_smiles` | All are empty | OR-rule: one issue |
| `R-CTX-UNIT` | Unit companion of a number field (section 2) | Its number is present | Closes only with a value |
| `R-CTX-DATA` | `MeasurementData.data_type` | `data` is present | |
| `R-CTX-LAW` | `Reaction.kinetic_law` | The document has parameters | One issue per reaction, asked together in one grouped question: a choice of rate model with its bindings (5.1). Software builds the Equation only from confirmed bindings that pass the checks of 3.1 (`S-RATELAW`, "Rate-law bindings"). |
| `R-CTX-RXN` | `Reaction.products` | The reaction has reactants and no products | The scientist names the products. Software creates the molecule and reaction-element entries, and the next round checks them. |

### 3.5 LIST fields

Everything else, for example:
- Protein `ecnumber`, `organism` (the expression host), `organism_tax_id`;
- SmallMolecule `synonymous_names`;
- identifiers beyond the one an identity rule needs;
- `Complex.participants` when empty;
- MeasurementData `initial`, `data`, `time`, `is_simulated`;
- `Measurement.group_id`;
- Parameter `lower_bound`, `upper_bound`, `initial_value`, `fit`, `constant`;
- document `description` and `references`;
- the container lists `proteins`, `small_molecules`, `complexes`, `reactions`, `measurements`, `parameters`, `equations`.

An object the input states but the draft omits is a `missed_value` issue (section 4.1), not a LIST gap.

## 4. Issue

| Field | Written by | Content |
|---|---|---|
| `issue_id` | Software | `ISS-001` and so on. Never chosen by an agent; never reused within a record. |
| `round` | Software | Round in which the issue was raised |
| `raised_by` | Software | `deterministic_verifier` or `verification_agent` |
| `kind` | Raiser | One of ten kinds (4.1) |
| `rule_id` | Raiser, optional | The rule or check that raised it (`R-*` from section 3, `C-*` from section 8). Issues added by the verification agent have none. |
| `fields` | Raiser | Unordered set of pointers. All fields of one issue must take the same value. |
| `summary` | Raiser | One plain sentence (5.3) |
| `document_value` | Raiser, optional | The value the document holds |
| `source_value` | Raiser, optional | The value the input states, typed where possible (`7.4`, not `"pH 7.4"`) |
| `source_locators` | Raiser | List of locators `{xpath, quote}` (section 2). Required for `source_conflict`, `wrong_value` and `missed_value`. |
| `status` | Software | `open`, `unavailable`, `held` or `closed`. `held`: the target of an issue that was `open` or `unavailable` became ambiguous after objects moved; it is neither asked nor answered until a named person maps or disposes it (7.1, "Live pointers"). |
| `closed_by` | Software | A question id, `recheck`, `override` or `structural_edit`. Present only while the issue is `closed`: software removes it when the issue reopens or becomes `unavailable`, so an `open`, `unavailable` or `held` issue has none. Earlier closures stay in the stored history of the issue list (7.1, "On re-check"). |

**Rules**

1. **Blocking is computed, not stored:** every issue blocks approval until it is closed, except `missing_optional`. Statuses `unavailable` and `held` also block.
2. **Missing issues are raised at the highest empty level:** one issue at `/creators`, never at `/creators/0/mail` of a creator that does not exist.
3. **One value per issue:** the pH of two measurements may share one issue. A parameter's value and its unit may not.

### 4.1 Kinds

| Kind | Meaning | Raised by | Closes with |
|---|---|---|---|
| `missing_required` | ASK-REQ field empty | Deterministic verifier | A value. "Not available" sets status `unavailable` (section 5.4). |
| `missing_recommended` | ASK field empty, or ASK-IF field empty while its rule applies | Deterministic verifier | A value, or "not available" with a reason (units: a value only) |
| `missing_optional` | LIST field empty, including ASK-IF fields whose rule does not apply | Deterministic verifier | Never asked; never blocks; stays listed |
| `wrong_type` | Any schema violation (JSON type, enum, range, pattern, a property the schema does not define) or a `null` / `""` / `{}` placeholder; for a "required" error at an empty field, see note 4 | Deterministic verifier | See section 5.2 |
| `broken_reference` | An id reference that points to nothing, or a duplicate id | Deterministic verifier | See section 5.2 |
| `bad_citation` | An extracted value with no citation, an xpath that does not select exactly one node, a quote not in the node, or a value that does not equal its quote under the normaliser (8.2) | Deterministic verifier | See section 5.2 |
| `wrong_unit` | Verifier: the unit cannot be parsed or has the wrong dimension. Agent: the unit differs from the source. | Either | A corrected unit |
| `source_conflict` | Two input statements disagree about what one field should hold | Verification agent | The scientist's choice |
| `wrong_value` | The document value is not what the cited input states | Verification agent | The scientist's choice (document or source value) or a correction |
| `missed_value` | The input states a value for an empty field or an omitted object | Verification agent | The scientist's choice; "use it" fills the field and cites the source |

**Notes**

1. **Structured vs free text:** in a `source_conflict`, the document keeps the structured value until the scientist decides. When two structured values conflict, the document keeps the value as extracted, and both are cited.
2. **`missed_value` pointers:** `fields` holds the empty field's pointer, or the parent's pointer for an omitted object. Never invent child indices.
3. **Out of scope for Stage 1:** values that look implausible but are copied faithfully, e.g. a kcat that disagrees with the paper. The record is copied as it stands.
4. **Schema "required" errors:** at an empty field that has a field role other than SOFTWARE (section 3), a schema "required" error is raised only as that field's `missing_*` issue, never also as `wrong_type`. At an empty SOFTWARE field it stays `wrong_type` and goes to human review (4.2 rule 6).
5. **Parameter links** (an exception to note 2): a parameter link that names the wrong species or dataset, or that the draft leaves out although the input states it, is raised on the parameter as `wrong_value` or `missed_value`, with the link's locators, one issue per link. For such an issue, `fields` holds the parameter's pointer followed by `/link/species_id` or `/link/measurement_id`; it points into the parameter's link entry, not into the document, and 4.2 rule 2 checks the parameter's pointer. Software writes the answer to the parameter's link entry in the evidence file, never to the parameter itself.

### 4.2 Judgment (verification agent's report)

| Field | Content |
|---|---|
| `issue_ids` | One or more issues sharing the same verdict |
| `verdict` | `confirmed`, `rejected` or `uncertain` |
| `reason` | One sentence |

**Rules**

1. **What the agent judges:** every issue from the deterministic verifier, except `missing_optional`. Those it judges only by exception, to flag a problem.
2. **Its own issues:** issues the agent adds carry no judgment. Software registers an issue only if the "Raised by" column of 4.1 allows its raiser for that kind, and each pointer in `fields`, or that pointer's parent, exists in the record (for a parameter-link issue, the parameter's pointer; 4.1 note 5). Any other issue is not registered. It is counted in the run log and passed to human review as a note, and the person working on the record may act on the note with a structural edit (6.2).
3. **A judgment never closes an issue and never changes whether it blocks.**
4. **`uncertain`** is routed like `confirmed`. The question tells the scientist the agent was unsure. An issue of round 1 that rule 1 gives the agent to judge, but that gets no verdict or two different verdicts, is routed like `uncertain`.
5. **Missing issues:** `confirmed` means the input lacks the value. If the input does state it, the agent judges the issue `rejected` and raises a `missed_value` with the source value. One question then covers both.
6. **Routing:**

| Issue | Verdict | Goes to |
|---|---|---|
| `missing_required`, `missing_recommended`, `wrong_unit`, `source_conflict`, `wrong_value`, `missed_value` | Any | Inquiry agent. A rejection's reason is shown in the question. |
| `wrong_type`, `broken_reference`, `bad_citation` on an extracted value | Confirmed or uncertain | Inquiry agent, asked as a lab fact (5.2) |
| `wrong_type`, `broken_reference`, `bad_citation` on an extracted value | Rejected | Human review: a likely checker defect. Not asked unless the person sends it on (below); still blocks. |
| Any issue on a SOFTWARE field | Any | Human review. Closed by a software fix and re-check (issues of the deterministic verifier), by an override, or by a structural edit. |
| `missing_optional` | Not applicable | Nobody; listed in the report |

An issue raised in round 2 or later, other than by the final check (7.1), has no verdict and is routed as if `confirmed`. In this table and in 5.2 rule 7, a value the scientist gave counts as an extracted value, and a `wrong_type`, `broken_reference` or `bad_citation` issue on a value written by a structural edit goes to human review. A reopened issue goes where it went before it closed, unless it is a `wrong_type`, `broken_reference` or `bad_citation` issue on a value since written by a structural edit; that goes to human review. Any issue that the final check raises or reopens goes to human review instead (7.1). If the person reviewing finds that a rejected mechanical issue on an extracted value is real, they send it to the inquiry agent, and it is asked as a lab fact (5.2 rule 7). This never applies to issues on SOFTWARE fields or to issues the scientist already answered with "The question does not fit". A `held` issue goes nowhere until a named person maps or disposes it (6.2); once mapped, it is routed as before it was held.

## 5. Questions and answers

### 5.1 Question

| Field | Written by | Content |
|---|---|---|
| `question_id` | Software | `Q-001` and so on |
| `round` | Software | Round of the question |
| `issue_ids` | Inquiry agent | Hidden tags; at least one. The fields follow from the issues. |
| `text` | Inquiry agent | Plain language (5.3) |
| `answer_type` | Inquiry agent | `value` (free entry: a number with unit, text, or a list) or `choose_one` |
| `options` | Inquiry agent; required for `choose_one` | List of `{label, value}` |

**Options**

1. **What they offer:**
   - For enum fields: the allowed values, in plain words.
   - For conflicts: the document value and the source value.
   - For yes/no fields: yes and no, in plain words.
   - For corrections: the current value and the proposed value.
2. **Standard closing options:** every `choose_one` ends with two of them:
   - **"A different value: …"** (free entry). This closes the issue with the typed value. It is omitted for enum fields, where all allowed values are already listed.
   - **"The question does not fit: …"** (a note is required). This never closes an issue. It goes to human review (6.2).

**Rules**

1. **Grouping:** one question may tag several issues, e.g. the six "constant" fields of T9HQ4X. The answer then has one item per issue.
2. **What is never asked:** `missing_optional`; anything routed to human review, unless the person reviewing sends it on (4.2 rule 6); and a `held` issue (7.1).
3. **Rate law (`R-CTX-LAW`):** one grouped question for all reactions, with one `choose_one` item per reaction. For each reaction, the inquiry agent proposes the models from the starter list that the record's parameters support, each as a fully bound option (3.1, "Rate-law bindings"): its value carries the model, the target reaction, the measurement whose context applies, the parameter id bound to each argument and the species id bound to each variable, and an item chooses only an option of its own reaction. The agent proposes from the record information and evidence its packet supplies, chiefly the parameter links; it does not search the input, invent a missing link or repair the record. An option's label shows the formula with the names, datasets, values and units of what it binds, never ids (5.3), so that parameters that share a name stay distinguishable. Where the record supports materially different bindings, for example two substrates, each is an option of its own; one option never combines parameters of different datasets or substrates. Parameters that share a name but that the links tell apart, such as a kcat in each of two datasets, are not by themselves an ambiguity, and choosing one of several valid ids does not settle a real one. Where no supported option can be formed for a reaction, for example because a needed link is missing, or because quantities that must share a unit are stated in units of different scale (3.1, check 5), the question says so and offers that reaction only the standard closing options. Documentation example, which the model-facing reference text excludes (it is a worked demonstration): "v = kcat · E · S / (Km + S), with kcat = 5.057 s⁻¹ and Km = 0.082 mM from the same dataset, S the substrate and E the enzyme as the record names them". The starter list is extended when a Stage 1 entry needs another model:

   | Model | Formula | Needs | Dimensions | Scale (3.1, check 5) |
   |---|---|---|---|---|
   | Michaelis-Menten, kcat form | v = kcat · E · S / (Km + S) | kcat, Km | kcat: inverse time; Km, E, S: amount concentration | Km and S share one unit |
   | Michaelis-Menten, Vmax form | v = Vmax · S / (Km + S) | Vmax, Km | Vmax: amount concentration per time, not an activity per enzyme mass; Km, S: amount concentration | Km and S share one unit |
   | Substrate inhibition | v = kcat · E · S / (Km + S + S²/Ki) | kcat, Km, Ki | kcat: inverse time; Km, Ki, E, S: amount concentration | Km, Ki and S share one unit |
   | Hill | v = kcat · E · Sⁿ / (K₀.₅ⁿ + Sⁿ) | kcat, K₀.₅, n | kcat: inverse time; K₀.₅, E, S: amount concentration; n: dimensionless | K₀.₅ and S share one unit; n has a dimensionless unit of scale exactly 1 |

   Amount concentration means amount of substance per volume, for example mol/L or mmol/L, and the rate v has the dimension amount concentration per time (3.1, "Rate-law bindings", check 4, and "Units in the equation"). The quantities that the column "Scale" says share one unit enter a sum in the formula, directly or in a term such as S²/Ki or Sⁿ, so they must share one unit, not only one dimension (3.1, check 5); the enzyme, kcat and Vmax are only multiplied and need not. The Hill exponent n is used as a pure number, so its dimensionless unit must have the scale exactly 1: n = 2 is eligible, and n = 200 % is not read as the exponent 200 or converted to 2.

   The standard closing options follow. Here "A different value" means another model or other bindings, named or written as a formula. It goes to human review, and the person working on the record writes the equation, or gives a fully bound option, by a structural edit (6.2). A chosen option that fails a check of 3.1 closes nothing and goes to human review in the same way.

### 5.2 Answer

| Field | Content |
|---|---|
| `question_id` | The question answered |
| `answered_by` | Named scientist, the answer's author |
| `answered_at` | Date and time |
| `entered_by` | Optional: the named person who entered the answer for its author (assisted entry, 6.3) |
| `original_ref` | With `entered_by`: the reference (artifact id) of the author's original message, stored unchanged (6.3) |
| `items` | At most one per tagged issue: `{issue_id, value \| choice \| not_available, unit?, reason_code?, note?, field?}` |

**Rules**

1. **Where values go:** software writes an item's value to all fields of its issue. For a parameter-link issue it writes the value instead to the link that the issue's pointer names, in the parameter's link entry (4.1 note 5). Before writing, software checks that each pointer still addresses its bound object (7.1, "Live pointers"); an item for a `held` issue is not applied, and the issue stays `held`.
2. **`unit`:** required when the value is a number for a field with a unit companion. Software writes it to the companion.
3. **`field`:** only for OR-rule issues; it names which alternative the value fills.
4. **Object and list values:** a value may be an object or a list at a container pointer, e.g. the creators, or the products named for `R-CTX-RXN`. Applying the answer creates the new objects, and the next round checks them. If objects move, software maintains the live pointers as 7.1 says; the stored answer keeps its original form.
5. **Issues without an item stay open.**
6. **`not_available`:** written as `not_available: true` and needs a `reason_code`, one of `not_measured`, `not_at_hand`, `not_applicable` or `other`. `other` needs a note. An item that declares nothing unavailable leaves the key out; `false` is no answer of its own. Whether the item closes the issue or makes it `unavailable` follows 5.4.
7. **Mechanical issues asked as lab facts:** `wrong_type`, `broken_reference` and `bad_citation` on an extracted value (including a value the scientist gave, 4.2 rule 6) are asked as a question about the value, never about mechanics, showing both values. Documentation example, which the model-facing reference text excludes (it is a worked demonstration): "The record gives Km as 0.82 mM, but the cited place says 0.082 mM. Which is right?" The answer closes the issue like a `wrong_value`.

### 5.3 Plain-language rule

1. **Name things the scientist knows:** question texts and issue summaries name objects by their names in the record and by dataset. They never use pointers, ids or EnzymeML field names.
2. **Show the values:** quote the current value and the source value where they exist.
3. **Keep it short:** one decision per question, with the reason in one clause.

### 5.4 Closure

| Kind | Closes with |
|---|---|
| `missing_required` | A value. "Not available" sets status `unavailable`: the issue is not asked again but still blocks, and the record ends as "not approvable", naming those fields. It can continue if the scientist later supplies the value (6.2). |
| `missing_recommended` | A value, or "not available" with a reason code. Units: a value only. |
| `source_conflict`, `wrong_value`, `missed_value` | A choice or a correction |
| `wrong_unit` | A corrected unit |
| `wrong_type`, `broken_reference`, `bad_citation` | An answer (5.2 rule 7), a software fix and re-check, or an override (6.1) |
| Any kind, on a SOFTWARE field | An override (6.1), or, for an issue of the deterministic verifier, a software fix and re-check |
| Any kind | A structural edit (6.2) |

A `held` issue closes by none of these while it is held: a named person first maps or disposes it (6.2).

## 6. Human actions

A named person working on the record takes these actions. Normally this is the scientist, who may answer, correct and approve without switching roles; in Stage 1 it is the scientist or Tillman Heisner. There is no separate curator role, no maintainer role and no second sign-off. Every human action records `by` (the person's name) and `at` (date and time), and may record `entered_by` and `original_ref` (6.3). Each is prepared against the current working copy of the record and names that copy as its base (7.1, "Working copy"); the base is kept with the stored action and in the run log, never in the record files (11). No agent takes any of these actions.

**Human review:** an issue routed to human review (4.2 rule 6) becomes a review item, shown to the person working on the record and not phrased as a lab-fact question. The person may close it by an override (6.1) or a structural edit (6.2), send it on to the inquiry agent as a question (4.2 rule 6), or have software fixed. Approval is not a review action: only an eligible named scientist approves (7.2).

### 6.1 Override

- **What it may close:** mechanical issues only, i.e. `wrong_type`, `broken_reference`, `bad_citation`, or any issue on a SOFTWARE field, whatever its kind. Never a missing field, a conflict, a wrong value, a missed value or a wrong unit on a field that is not a SOFTWARE field.
- **Reason code (required):**

  | Code | Use | Required extra |
  |---|---|---|
  | `checker_false_positive` | The check is wrong for this case | Note; the defect is logged for the developer |
  | `known_external_defect` | A known defect in an external standard or tool | Link |
  | `other` | Anything else | Note |

- **Recorded:** `closed_by: override`, with the reason code, note, link, person (`by`) and time (`at`). Shown in the approval summary and counted in evaluation.

### 6.2 Structural edit

- **When:** an answer says "the question does not fit" or names a rate model or bindings outside the options offered, a chosen rate-law option fails a check of 3.1 ("Rate-law bindings"), or a fix needs changes that answers cannot make, such as moving a species between reactants, products and modifiers, splitting a measurement, or adding objects. A note about an added issue that was not registered (4.2 rule 2) can also lead to a structural edit. A record that ended as not approvable can also continue: if the scientist later supplies the missing value, a named person enters it by a structural edit whose basis is the scientist's statement; this closes the `unavailable` issue and starts a new round.
- **How:** a named person edits the record and records the edit with its basis. The issue the edit addresses, if there is one, closes with `closed_by: structural_edit`, and the next round re-checks. Values the edit writes get evidence entries with `filled_by: structural_edit` (8.1).
- **Base and earlier answers:** the edit is prepared against the current working copy and names it as its base; an edit prepared against any other copy is refused as stale (7.1, "Working copy"). An edit may change a value that an answer wrote: the change is shown against the base, the earlier answer stays stored, and the edit's basis covers the change.
- **Rate law:** an edit may give a fully bound rate-law option (3.1, "Rate-law bindings"), from which `S-RATELAW` builds the equation after its checks, or write the equation itself. An equation that the person writes may handle a conversion of units explicitly, for example for a Km stated in mmol/L with the substrate's data in mol/L (3.1, check 5); it is recorded as that person's equation with its basis, and the stated values and units stay as they are. A combination across measurements or substrates needs a statement in the basis and is never presented as something the source states.
- **Basis (required for every structural edit):**
  - `source`: one or more locators (section 2) that clearly state the change, for example input text that describes two separate assays when a measurement is split;
  - `statement`: an explicit human statement, i.e. an answer's note, a "The question does not fit" note, or a statement entered for the edit;
  - or both.

  A person's explanation alone is a statement, never source evidence. If the source is ambiguous, for example two input statements give different temperatures, a statement is required, and the edit is never presented as something the source states. A source-supported edit needs no further statement. An edit may also carry an optional `note` that explains it for readers; a note is never evidence and never counts as its basis. Re-checks and final approval (7.2) still apply. Overrides keep their own reason-code rules (6.1).
- **Pointers:** an edit that inserts, removes, splits or merges objects moves pointers. The edit declares the ids of the objects it split (`split_ids`) and merged (`merged_ids`); software then retargets or holds the live pointers (7.1, "Live pointers").
- **Held issues and bindings:** a named person maps a `held` issue, by giving the pointers of the object it now concerns, which software binds to that object's id (a retarget); the issue then returns to the status it had before it was held, `open` or `unavailable`. Or the person disposes of it as a structural edit with a basis, which closes it with `closed_by: structural_edit`, for example when its object was removed. A held evidence entry or parameter link is mapped in the same way, or disposed of by a structural edit with a basis. Mapping and disposal are human actions; software never chooses a mapping.
- **T9HQ4X example:** the record lists "Reduced 2,6-Dichlorophenolindophenol" as a compound, and none of the modifier roles fits it honestly.

### 6.3 Assisted entry

Another named person may enter an answer (5.2), an approval (7.2) or a human action that its author gave by another route, such as e-mail. The record keeps the author (`answered_by`, `approved_by` or `by`), `entered_by`, and `original_ref`, the reference (artifact id) of the author's original message, which software stores unchanged as a file of the run. Entry assistance never confers approval authority: an approval still counts only if its author is an eligible named scientist (7.2 condition 4).

## 7. Rounds and approval

### 7.1 Flow

1. The extraction agent drafts the record, its evidence entries and one not-mapped entry for each piece of input information that EnzymeML cannot hold (8.1).
2. The assembly step fills the SOFTWARE fields.
3. The deterministic verifier raises issues (round 1).
4. The verification agent judges them and adds its own.
5. The inquiry agent asks questions.
6. The scientist answers. Software applies the round's answers to a working copy of the round's snapshot (below). The person working on the record handles the review items on that copy (section 6); software applies each human action, in the order it accepts them, to the copy as it then stands, and maintains the live pointers (below).
7. When the review work of the round is done, software re-applies the SOFTWARE rules to the last version of the working copy and commits it as the next snapshot, all or nothing.
8. The deterministic verifier re-runs (round 2, 3, …). New issues are routed by 4.2 rule 6, and steps 5-8 repeat until no askable issue is open. The verification agent does not re-run in Stage 1. If structural edits prove error-prone in the pilot, it may re-run on fields written by structural edits only.
9. The final generation step sets `created` and `modified`.
10. **Final check:** the deterministic verifier checks the final files once more, and this is the last re-check of 7.2 condition 2. Any issue it raises or reopens goes to human review as a software defect, and approval waits until a later final check raises or reopens none.
11. The scientist approves.

This loop runs from the verifier to the scientist. There is still no retry back to the extraction agent. A technical failure, meaning a step that ends without usable output, is a run-log record and never an issue. A technical re-run is not a retry: an agent attempt that crashed, or whose output was unparsable or truncated, may be run once more on the same packet with only a short note of the error added (its class and where it occurred), and every re-run is counted and reported.

**On re-check**, a problem matching an earlier issue (same kind and fields) keeps that issue's id. For a closed issue, the match uses its kept bindings (section 2, Live pointer): a re-find reopens the closed issue when the kind and the bound object (its id plus the path below it) match; otherwise the problem is a new issue.
- An issue closed by "not available", by a "keep" decision or by an override stays closed.
- Any other closed issue found again is reopened, and its `closed_by` is removed (4); the issue list history keeps the earlier closure.
- An `unavailable` issue stays `unavailable`.
- An open issue raised by the deterministic verifier that the re-check no longer finds closes with `closed_by: recheck`.
- An open issue raised by the verification agent stays open on re-check, even when the re-check does not find it, and closes only through an answer or a human action (section 6).
- A `held` issue stays `held` until a named person maps or disposes it (6.2).

**Live pointers**, after a structural edit or an answer application that moves objects:
- **Retarget by id:** software retargets each live pointer (section 2) through the `id` it is bound to, when the correspondence is one-to-one: that id still exists exactly once, the edit did not declare it split or merged (6.2, `split_ids` and `merged_ids`), and the path below it passes through no list whose elements have no `id` (for example reactants and modifiers, species data, creators, or lists of plain values) in which the edit or answer inserted, removed or reordered elements. Example: splitting measurement A turns `[A, B]` into `[A1, A2, B]`; the open issue for B's pH moves from `/measurements/1/ph` to `/measurements/2/ph`, and never silently names A2.
- **Hold the ambiguous:** software never infers a split or merge mapping and never fabricates an id to force a match. Where a bound object was removed, split, merged or is otherwise ambiguous, or the binding's path passes through a list without element ids whose elements were inserted, removed or reordered, each affected issue that is not closed (`open` or `unavailable`) gets status `held`: it still blocks approval, is neither asked nor answered, and waits until a named person maps or disposes it (6.2). An affected evidence entry or parameter link is held too: it is not used, and while any binding is held the record cannot be approved (7.2 condition 5). This raises no issue and adds no issue kind.
- **Check before use:** before software uses a live pointer, it checks that the pointer still addresses its bound id. A pointer that resolves but addresses another object is never used; it is retargeted or held.
- **History stays:** stored snapshots, stored questions and answers, and the xpaths of source locators keep their original pointers; they are never rewritten because the output layout changed.
- Each retarget and hold is recorded in the run log.

**Working copy**, within one round. It starts no round, is no snapshot and is not committed until step 7 ends:
- **Prepared:** once every question of the round has an accepted answer (in a round without questions, at once), software copies the round's snapshot, writes the answers into the copy (5.2) and maintains its live pointers. The snapshot stays unchanged. From then on the round's answers are fixed; a change to an answered value is made by a structural edit (6.2).
- **Base:** software stores each version of the working copy with its checksum. Each human action names, as its base, the version it was prepared against. Software applies the actions one at a time, in the order it accepts them, each to the copy as it then stands; each applied action makes the next version. An action whose base is not the current version is refused as stale and returned to the person for reconciliation: software never merges it, and never lets it replace newer answers or actions. So of two actions prepared against the same version, the later one must be prepared again.
- **Commit:** when the review work of the round is done, software re-applies the SOFTWARE rules to the last version and commits it as the next snapshot, all or nothing; a partial snapshot is never written. A resumed application rebuilds only the chain of applied actions, in recorded order, from the stored versions, each checked against the base and checksum the run log records for it; an action refused as stale stays in the record of the run and is never replayed. An action whose application was interrupted is applied again only to the version its base names, never to another copy.
- **Outside a round of questions:** a structural edit made while the record waits for approval or after it has ended (5.4; 7.2, "Later changes") is prepared against a working copy of the record as it then stands.

### 7.2 Approval

A record can be approved when all five hold:
1. No blocking issue is `open`, `held` or `unavailable`.
2. The last re-check, which is the final check (7.1 step 10), raised or reopened no issue.
3. `created` and `modified` are set.
4. The approver is one named scientist who is listed among the creators.
5. No evidence entry or parameter-link binding is held (7.1, "Live pointers").

**Other creators** do not need to approve. Several sign-offs are left to Stage 2 (Q7).

**Recorded:** the approval goes into the evidence file as `{approved_by, approved_at}`, with `entered_by` and `original_ref` when another named person entered it (6.3).

**Later changes:** approval holds only for the files as approved. Any later change to them, other than adding the approval entry itself, voids the approval: the approval entry is removed (the run log keeps it), and the record is re-checked and needs a new approval.

**Sharing** still needs the data owner's separate approval.

**The approved deliverable** is the EnzymeML document, the evidence file and the not-mapped report.

**Numerical use:** approval is no evidence that a rate-law equation in the deliverable suits a numerical use, such as the derivative of a species in a particular tool (3.1, "Numerical use").

## 8. What the deterministic verifier checks

| Check | Raises |
|---|---|
| `C-SCHEMA`: schema validity under the validation profile (section 9) | `wrong_type` (for a "required" error at an empty field, see 4.1 note 4) |
| `C-REF`: every id reference resolves; no duplicate ids; parameter links in the evidence (8.1) resolve. A rate law's `species_id` is a label, checked for uniqueness only (section 9). | `broken_reference` |
| `C-CITE`: the citation check (8.2) | `bad_citation` |
| `C-UNIT`: units parse and have the right dimension (section 9) | `wrong_unit` |
| Role rules `R-*` (section 3) | `missing_*` |

It reads the input **only** to resolve xpaths and quotes for the citation check ([Architecture](ARCHITECTURE.md#components)). It holds no knowledge of any input format.

### 8.1 Evidence entries this format relies on

Q2.4 already requires an evidence file. This format uses these entry types:

| Entry | Content |
|---|---|
| Value | `pointer` (one per filled leaf field; elements of a list of plain values count as leaf fields, see "Lists" below), `value`, `filled_by` (`extraction_agent`, `software`, `scientist` or `structural_edit`), plus the filler-specific fields below |
| Value, extracted | `xpath`, `quote` (the shortest verbatim part of the node that states the value), `interpreted: true` when the normaliser cannot reproduce the value |
| Value, software | `rule_id` (`S-*`); `S-UNIT` also keeps the extracted unit spelling with the extraction agent's citation (3.1); `S-RATELAW` also keeps the confirmed option, that is the model and its bindings, and the answer or structural edit that confirmed it (3.1, "Rate-law bindings") |
| Value, scientist | `question_id`. If the chosen value equals a cited source value, the entry also keeps that xpath and quote, marked `interpreted: true` when the normaliser cannot reproduce the value from the quote. |
| Value, structural edit | Reference to the structural edit (6.2), which records its basis |
| Parameter links | Each parameter's link entry names its `link.species_id` and `link.measurement_id`, each with a citation. This keeps parameter-substrate-dataset links traceable (Q2.4), because EnzymeML parameters have no such fields. A wrong or missing link is raised as 4.1 note 5 says. Rate-law bindings rest on these links (3.1); whether a link was extracted with a citation or given by a person shows whether a binding's context is source-supported or human-stated. |
| Not available | `pointer`, `reason_code`, `note`, `issue_id`, `question_id` |
| Keep decision | `resolved_by` (`question_id` and reason) on the kept value's entry |
| Correction | `replaced_value` and its xpath |
| Override, structural edit | As in section 6 |
| Approval | `approved_by`, `approved_at`, optional `entered_by` with `original_ref` (6.3) |
| Not-mapped entry (in the not-mapped report) | A locator (`xpath`, `quote`) and a one-sentence `reason`. For a value its field cannot hold, the entry also names that field; in the not-mapped report, the assembly step gives that field as its pointer. Drafted by the extraction agent (7.1 step 1). No entry needs a link to an issue, and nothing checks that every part of the input is either mapped or listed. |

**Lists:** a list of plain values (for example synonyms, references or data points) is cited element by element: each element counts as a filled leaf field with its own Value entry, its own pointer (for example `/small_molecules/0/synonymous_names/1`) and its own citation. An issue about one element points at that element; a missing or empty list is still one issue at the list's own pointer.

**Values the field cannot hold:** some input values don't fit their field, e.g. a substrate given only as a range, as for both substrates in T9HQ4X. The extraction agent records such a value as a not-mapped entry that names the field, and the not-mapped report gives that field's pointer. The deterministic verifier copies the entry's quote into the `source_value` of the missing issue at that pointer and never searches the input for it; the entry stays in the not-mapped report whatever the answer.

### 8.2 Citation check

1. The `xpath` selects exactly one node (section 2, Locator).
2. The `quote` is a verbatim part of that node's string value.
3. The `value` **equals** the quote under one fixed normaliser:
   - numbers compare as exact decimals, never as binary floating point (`1` equals `1.0`), and a quote counts as a number only if the whole quote matches `^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$` under ECMA-262 rules. So `0.0820` and `8.2e-2` equal `0.082`, while a quote with a decimal comma, a space, a thousands separator or a Unicode minus is not a number, and its value needs `interpreted: true`;
   - letter case is ignored, except in unit spellings (3.1), because `mM` and `MM` differ;
   - URL templates for DOI, UniProt, PubChem and ChEBI identifiers are applied.

   This is equality, not containment: `0.08` must not pass for a quote of `0.082`.

**Exceptions**
- Values marked `interpreted: true` get only checks 1 and 2. The verification agent judges whether they are right.
- Reference fields (`species_id` in ReactionElement, ModifierElement and MeasurementData; `Complex.participants`; an extracted `vessel_id`; and the ids in parameter links) get only checks 1 and 2, because software writes their ids; the verification agent judges whether the reference is right.
- Software values are exempt; they carry their rule id instead. An extracted unit spelling that `S-UNIT` builds on is not exempt: its citation gets all three checks, check 3 compares the spelling with its quote, and a failure is raised as `bad_citation` at the unit field, not at its internals (3.1).

## 9. Validation profile

1. **Schema:** EnzymeML V2.0 JSON Schema at commit bf9321f (Q3), with **one documented deviation**:
   - **The defect:** the `/version` pattern in that file has literal quote characters around it, so it matches no string (upstream issue EnzymeML/enzymeml-specifications#35).
   - **The deviation:** validate against `^(\d+)\.\d+$` instead, the pattern the same commit's `specifications/v2.md` intends.
   - **Matching:** the whole string must match, with ECMA-262 regex rules. (Python's `re.search` with `$` would wrongly accept `"2.0\n"`.)
   - **End:** remove the deviation and re-pin when #35 is fixed.
2. **Unit dimensions:**
   - `Vessel.unit` must be a volume;
   - `temperature_unit` a temperature;
   - `time_unit` a time;
   - `data_unit` must fit `data_type`;
   - `Parameter.unit` must parse.

   Check the dimension of the document's unit definition, not the input's unit symbol ("C" means coulomb in some unit systems).
3. **Rate-law label:** in a rate law, `species_id` holds the rate label `v_<reaction id>`, e.g. `v_r1`. The spec text calls this field "a defined species", but a rate law's left-hand side is the reaction rate, and EnzymeML's own example uses a rate name there ("slac_oxidation"). This is a known gap between spec text and practice, documented here like the `/version` deviation. The verifier checks that the label is unique and does not treat it as a link to a species.

## 10. Examples (T9HQ4X)

The examples use the public STRENDA DB entry T9HQ4X (https://doi.org/10.22011/strenda_db.T9HQ4X). Issue and question numbers are illustrative. These are documentation examples: the model-facing reference text excludes them, because they are worked demonstrations.

### 10.1 A pH conflict

The **issue**, raised by the verification agent:

```json
{
  "issue_id": "ISS-021", "round": 1, "raised_by": "verification_agent",
  "kind": "source_conflict",
  "fields": ["/measurements/0/ph", "/measurements/1/ph"],
  "summary": "Both datasets give pH 7.8, but the methods text says the buffer was at pH 7.4.",
  "document_value": 7.8, "source_value": 7.4,
  "source_locators": [
    {"xpath": "/experiment/datasets/dataset[1]/assayConditions/value[2]/@value", "quote": "7.8"},
    {"xpath": "/experiment/datasets/dataset[2]/assayConditions/value[2]/@value", "quote": "7.8"},
    {"xpath": "/experiment/methodology", "quote": "20mM HEPES pH 7.4"}
  ],
  "status": "open"
}
```

The **question**:

```json
{
  "question_id": "Q-004", "round": 1, "issue_ids": ["ISS-021"],
  "text": "Both datasets give the assay pH as 7.8, but the methods text says '20mM HEPES pH 7.4'. Which pH was used in the assays?",
  "answer_type": "choose_one",
  "options": [
    {"label": "7.8 (dataset values)", "value": 7.8},
    {"label": "7.4 (methods text)", "value": 7.4},
    {"label": "A different value: ...", "value": "free_entry"},
    {"label": "The question does not fit: ...", "value": "does_not_fit"}
  ]
}
```

The **answer** (illustrative):

```json
{"question_id": "Q-004", "answered_by": "<scientist>", "answered_at": "2026-10-20T14:03:00Z",
 "items": [{"issue_id": "ISS-021", "choice": 7.8}]}
```

**Result:** ISS-021 closes with `closed_by: Q-004`. The evidence entries for both pH fields get `resolved_by: {question_id: Q-004, reason: "scientist chose the dataset value"}`.

### 10.2 A grouped question

The deterministic verifier raises six `missing_required` issues, ISS-001 to ISS-006, one each for the `constant` field of the enzyme and the five small molecules.

The **question:** "During an assay, does the amount of each of these stay the same, i.e. it is not used up or formed? (1) the enzyme, (2) HEPES NaOH, (3) Phenazine methosulfate, (4) (R)-2-hydroxyglutarate, (5) Reduced 2,6-Dichlorophenolindophenol, (6) (R)-malate."

The **answer** has six items, one per issue (illustrative):

```json
{"question_id": "Q-001", "answered_by": "<scientist>", "answered_at": "2026-10-20T14:01:00Z", "items": [
  {"issue_id": "ISS-001", "choice": true},
  {"issue_id": "ISS-002", "choice": true},
  {"issue_id": "ISS-004", "choice": false}
]}
```

Here ISS-003, ISS-005 and ISS-006 stay open, because no item answered them.

### 10.3 A missed value

1. The deterministic verifier raises ISS-007: `missing_required` on `/vessels/0/name`.
2. The verification agent judges ISS-007 `rejected` ("the methods text names the vessel"). It raises ISS-022: `missed_value`, fields `["/vessels/0/name"]`, `source_value` "microwell plate", locator `{xpath: "/experiment/methodology", quote: "Reactions carried in a microwell plate"}`.
3. One question tags both issues: "The methods text says 'Reactions carried in a microwell plate'. Should the reaction vessel be named 'microwell plate'?"
4. "Yes" closes ISS-022 and fills the field, citing the methods text. ISS-007 closes on re-check (`closed_by: recheck`).

## 11. Deliberately left out

- **Stage 2, if ever:** heavier machinery such as revision chains, file hashes inside the record files (in Stage 1, software keeps checksums in the run log only, and the record format is unchanged), idempotency keys, a 19-field approval record and disposition attestations. Stage 1 has 15-25 entries and no separate curator role.
- **Rejected:** a missing-field registry with input search coverage, and STRENDA mapping in the verifier. These would make the verifier read the input beyond citations, which ARCHITECTURE.md rules out.
- **Not adopted:** one bundled issue for all empty optional fields. Instead, each field gets its own issue and the agent judges them by exception, which keeps Q2.2 as written.
- **Out of scope for Stage 1:** flagging values that are copied faithfully but look implausible.
- **Stage 2 (Q7):** the review interface, answer forms and several sign-offs.
- **Not adopted:** model fitting, automatic model discovery and a general relationship graph for rate laws (3.1); locking, automatic merging and a second approval for human actions, since a stale action is refused for reconciliation (7.1, "Working copy"); and, for rate laws, automatic conversion of stated values, conversion factors written by software and a general unit-conversion system (3.1, "Units in the equation").
- **Left to a later decision:** how a numerical target for a rate-law equation and its unit are determined, how an equation is passed to a downstream tool, and any conversion for that use (3.1, "Numerical use").

## Changes from version 0.9

The change was decided by Tillman Heisner on 2026-10-28, after version 0.9 (see the [provenance ledger](README.md#2026-10-29---workflow-and-review-design-consolidated); for the boundary, [Numerical use of rate laws bounded](README.md#2026-10-29---workflow-and-review-design-consolidated)).

- Numerical use of rate laws: checks 4 and 5 of 3.1 establish compatibility inside the formula only. An equation is recorded and reviewed without any claim that it suits a numerical use; before it is represented as suitable for a specified use, such as a species derivative, the unit and scale of its rate are checked against that use; with no specified target no claim is made; a specified target that does not match gets neither the equation nor a conversion, and the question goes to review; approval is no evidence of numerical compatibility. How targets are determined, downstream integration and conversion are left to a later decision (3.1, "Numerical use"; 7.2; 11).

## Changes from version 0.8

The change was decided by Tillman Heisner on 2026-10-28, after version 0.8 (see the [provenance ledger](README.md#2026-10-29---workflow-and-review-design-consolidated); for the units, [Rate-law unit scales decided](README.md#2026-10-29---workflow-and-review-design-consolidated)).

- Rate-law unit scales: the reading of version 0.8, that an equation is sound because each symbol keeps the unit stated for it, is replaced. Check 5 of 3.1 requires the bound quantities that the model adds, subtracts or compares to share one unit, not only one dimension, and the starter list names them; quantities of different dimensions, such as kcat and Km, need not share a unit. The Hill exponent n must have a dimensionless unit of scale exactly 1, so n = 200 % is not used as the exponent 200. If the quantities that must share a unit differ in scale, if n has another scale, or if such a scale cannot be read, no equation is built from that binding, every stated value and unit stays as it is, the units are not thereby wrong, the record is not marked invalid, and the rate-law issue goes to human review, to be resolved by a representation in matching units or by an equation that a named person writes. Software converts no stated value and writes no conversion factor (3.1, check 5 and "Units in the equation"; 5.1 rule 3; 6.2).

## Changes from version 0.7

The changes were decided by Tillman Heisner on 2026-10-28 (see the [provenance ledger](README.md#2026-10-29---workflow-and-review-design-consolidated); for the units, [Rate-law unit dimensions decided](README.md#2026-10-29---workflow-and-review-design-consolidated)).

- Rate-law units: the starter list states amount concentration (for example mol/L or mmol/L) for the substrate, the enzyme and the K constants, inverse time for kcat and amount concentration per time for Vmax, with n dimensionless; a mass concentration or an activity per enzyme mass fails the dimension check and goes to human review, its value kept and never converted; units of one dimension but different scale are never equated, and the equation relates quantities with their stated units (3.1, check 4 and "Units in the equation"; 5.1 rule 3).
- `closed_by` is present only while an issue is closed and is removed when it reopens or becomes `unavailable`, with earlier closures kept in the stored history; `not_available` is written as `true`, and otherwise left out (4; 5.2 rule 6; 7.1, "On re-check"). These are the two points that D30 A carried to the next version.

## Changes from version 0.6

Decision numbers refer to the design decisions of 2026-10-27 (see the [provenance ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)).

- AD-D01, with its clarification of the same day: `S-RATELAW` builds a rate law only from one confirmed, fully bound option (model, target reaction, measurement, a parameter for each argument and a species for each variable), which the inquiry agent proposes from the record's parameter links and the scientist confirms, or which a named person gives by a structural edit (6.2); software checks it (complete, resolved, one context, dimensions), builds exactly that option, never assigns roles or rebinds, and re-validates it when it applies the rule again; a combination across contexts needs a structural edit with a statement; the starter list gives each argument's dimension; the evidence keeps the option and what confirmed it (3.1; 3.4, `R-CTX-LAW`; 5.1 rule 3; 6.2; 8.1; 11).
- AD-D04: a round's answers are applied to a working copy of its snapshot; human actions are prepared against the current version of that copy, name it as their base and are applied one at a time in recorded order; a stale action is refused for reconciliation; a change to an answered value is a structural edit that shows the change; the next snapshot is committed all or nothing (6; 6.2; 7.1 steps 6 and 7, "Working copy"; 11).

## Changes from version 0.5

Change numbers refer to the design changes decided on 2026-10-22 (see the [provenance ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)).

- C01: live pointers are bound to the nearest ancestor id plus the path below it, retargeted only one-to-one (the id exists once, the edit declared it neither split nor merged, and no list without element ids on its path changed) and checked before use; an ambiguous target makes an open or unavailable issue `held` until a named person maps it (it returns to its earlier status) or disposes of it by a structural edit (`closed_by: structural_edit`); a held issue blocks approval and is neither asked nor answered; a held evidence entry or parameter link is not used and blocks approval (new condition 5), with no new issue kind; closed issues keep their bindings for re-check matching only, and a re-find reopens one when kind and bound object match; historical pointers stay (2, Live pointer; 4; 4.2 rule 6; 5.1 rule 2; 5.2 rules 1 and 4; 5.4; 6.2; 7.1; 7.2 conditions 1 and 5).
- C02: every structural edit records its basis, source locators that clearly state the change and/or an explicit human statement; an explanation alone is not source evidence, and an ambiguous source needs a statement; an optional `note` explains an edit for readers and is never evidence (6.2).
- C10: no separate curator role; a named person working on the record, normally the scientist, takes the human actions without switching roles; issues formerly routed to the curator go to human review as review items; assisted entry keeps the author, `entered_by` and `original_ref` (the reference, an artifact id, of the original message, stored unchanged) and confers no approval authority; serialized values `closed_by: curator_edit` and `filled_by: curator` become `structural_edit` (1; 4; 4.1 note 4; 4.2 rules 2 and 6; 5.1; 5.2; 5.4; 6, renamed "Human actions"; 6.3, new; 7.1; 7.2; 8.1; 11).
- C11: the filled-in rate-law presentation and the completed example question are documentation examples that the model-facing reference text excludes; so are the section 10 examples; the rules and symbolic formulas stay (5.1 rule 3; 5.2 rule 7; 10).

The items below describe earlier changes and keep their original wording, including the curator role of version 0.5.

## Changes from version 0.4

Item numbers refer to the [package adoption register, section 11](design/PACKAGE_ADOPTION.md#11-pending-issue-format-changes).

- Item 1: a schema "required" error at an empty field with a role other than SOFTWARE is raised only as that field's missing issue (4.1 note 4; 8).
- Item 2: every xpath selects exactly one node, stated once in the new term Locator (2; 4.1, `bad_citation`; 8.2 check 1).
- Item 3: the extraction agent drafts the not-mapped entries, and their content is defined (7.1 step 1; 8.1).
- Item 4: the number grammar of the citation normaliser (8.2 check 3).
- Item 5: software registers only issues that the "Raised by" column allows, and the curator may act on a note about any other (4.2 rule 2; 6.2); a technical failure is a run-log record, never an issue (7.1).
- Item 7: a technical re-run is not a retry (7.1); checksums are kept in the run log only (11).
- Item 8: a later change to the approved files voids the approval (7.2).
- Item 9: reference fields get citation checks 1 and 2 only (8.2).
- Item 10: a unit that software cannot derive keeps its stated spelling and is raised as a wrong unit, not as empty (2, Empty; 3.1, `S-UNIT`).
- Item 12: a list of plain values is cited element by element (8.1).
- Item 13: the assembly step never reads the input; `S-UNIT` uses the unit spelling of the draft or the answer, whose citation gets the full check, and `S-SYMBOL` uses the parameter's name (3.1; 8.1; 8.2).
- Item 14: xpaths are absolute XPath 1.0 location paths, as part of the term Locator (2; 8.2 check 2).
- Item 15: an issue of round 1 left without a verdict, or with two, is routed like `uncertain` (4.2 rule 4); an added issue that does not attach to the record is not registered (4.2 rule 2).
- Item 17: the term Locator also covers an issue's `source_locators` (2; 4).
- Item 18: routing of issues raised in round 2 or later and of reopened issues (4.2 rule 6; 5.2 rule 7; 7.1 step 8).
- Item 19: on re-check, the deterministic verifier's open issues close when no longer found, and the verification agent's open issues stay open until an answer or a curator action closes them (7.1).
- Item 20: a final check of the final files before approval, whose issues go to the curator (7.1 steps 9 to 11; 7.2 condition 2; 4.2 rule 6).
- Item 22: a record that ended as not approvable can continue by a curator's structural edit (5.4; 6.2).
- Item 23: the curator may send a rejected mechanical issue that proves real to the inquiry agent (4.2 rule 6; 5.1 rule 2).
- Item 26: a value its field cannot hold reaches the missing issue at the field's pointer through its not-mapped entry, which stays in the report (8.1).
- Item 27: a wrong or missing parameter link is raised on the parameter, with a pointer that names the link, and its answer goes to the link entry (2, Pointer; 4.1 note 5; 4.2 rule 2; 5.2 rule 1; 8.1).
- Without an item number: an empty `Complex.participants` is LIST, as 3.5 already said (3.1); an override may close an issue of any kind on a SOFTWARE field, and such an issue may also close by a structural edit (4.2 rule 6; 5.4; 6.1); a scientist value's kept citation is marked interpreted when the normaliser cannot reproduce the value (8.1).

Items 6, 11, 16, 21, 24 and 25 were not taken into the format; they stay rules of the design documents (item 24 matters only under version 0.4, because item 1 removes its case).

## Notes for the evaluation datasets (not part of the format)

1. **Matching:** score issues as (kind, pointer) pairs and ignore `issue_id`, `rule_id`, `summary` and `raised_by` (mode A; in mode B through source anchors, Evaluation interfaces 4.1 rule 12).
2. **Verifier vs agent:** the deterministic `missing_*` issues are an exact-match test of the verifier. Leave them out of the agent's verdict accuracy.
3. **Q4.2 classes:**
   - confirmed and rejected are verdicts;
   - source conflict is the kind `source_conflict`;
   - gap is `missing_*` or `missed_value`.
4. **Uncertain:** count `uncertain` as flagged, and report the uncertain rate separately.
5. **Unwanted questions:** a question is unwanted when none of its `issue_ids` should have reached the inquiry agent.
6. **What to report:** the question count, the answer-item count and the override rate per record.
