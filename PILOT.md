# Proposed ARIADNE pilot

## Purpose

ARIADNE is proposed to begin as a small, human-centered ELEGANCE pilot focused on making EnzymeML easier to use. Researchers would work with familiar scientific files and receive evidence-linked candidate EnzymeML records without needing to master the complete standard in advance.

## Proposed participants

The proposed cohort includes John M. Woodley, Carlos G. Acevedo-Rocha, Jürgen Pleiss, Tillman Heisner, and relevant members of their groups. Participation, responsibilities, available effort, dataset ownership, and decision authority remain to be confirmed.

## How the pilot would work

### Stage 1 - Establish the workflow with existing datasets

1. Select a small set of existing enzyme reaction or kinetics datasets and define the expected outputs.
2. Preserve and deterministically parse the source files, linking candidate values to exact evidence.
3. Compare zero-shot and few-shot-guided extraction agents for producing candidate EnzymeML records and clarification questions.
4. Apply deterministic validation, separate verifier agents, and human scientific review.
5. Confirm that the resulting records follow the selected EnzymeML specification without losing important information.

The STRENDA DB entries of Stage 1 are a controlled benchmark for developing a workflow that is intended later to take the varied files researchers use. Stage 1 results would show how the workflow performs on these entries, not that it handles arbitrary files. Development entries are used for tuning and are reported apart from held-out test entries, and agent evaluation stops after the first round of questions ([Open questions, Q1 and Q4](OPEN_QUESTIONS.md#q1---which-existing-datasets-should-be-used)).

### Stage 2 - Apply it to researcher workflows

6. Select a small set of representative enzyme reaction or kinetics workflows and define what users consider useful.
7. Obtain data-owner approval and agree how the files may be processed, stored, and shared.
8. Apply the established workflow to their files and let researchers review, correct, and approve the candidate records.
9. Evaluate record quality, usability, time saved, and willingness to use ARIADNE again.

## Evaluation

The pilot should assess both record quality and user experience.

**Record quality:** Are extracted values supported by exact source evidence, are metadata and units represented correctly, and do deterministic checks and verifier agents detect errors and ambiguity?

**User experience:** Do researchers understand the candidate record and clarification questions, can they correct it with reasonable effort, does the workflow save time, and would they use it again?

**In Stage 1**, record quality would be reported in three separate views rather than as one overall score: integrity (for example invented values, unit errors and unsupported citations), usefulness (for example stated facts recovered and the questions asked) and operational completion (for example items completed, failures and re-runs). These views are used to diagnose the workflow during development. The criteria for continuing are to be set by Tillman Heisner, in a versioned evaluation plan, before held-out test results are inspected; meeting them would mean that the workflow is technically ready for proposing a bounded trial with researchers, not that such a trial is authorized. No numerical thresholds have been chosen ([Open questions, Q4 and Q8](OPEN_QUESTIONS.md#q4---how-should-extraction-and-verification-be-evaluated)). Stage 1 does not measure user experience or time saved; those belong to Stage 2.