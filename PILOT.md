# Proposed ARIADNE pilot

## Purpose

ARIADNE is proposed to begin as a small, human-centered ELEGANCE pilot focused on making EnzymeML easier to use. Researchers would work with familiar scientific files and receive evidence-linked candidate EnzymeML records without needing to master the complete standard in advance.

## Proposed participants

The proposed cohort includes John M. Woodley, Carlos G. Acevedo-Rocha, Jürgen Pleiss, Tillman Heisner, and relevant members of their groups. Participation, responsibilities, available effort, dataset ownership, and decision authority remain to be confirmed.

## How the pilot would work

### Stage 1 — Establish the workflow with existing datasets

1. Select a small set of existing enzyme reaction or kinetics datasets and define the expected outputs.
2. Preserve and deterministically parse the source files, linking candidate values to exact evidence.
3. Compare zero-shot and few-shot-guided extraction agents for producing candidate EnzymeML records and clarification questions.
4. Apply deterministic validation, separate verifier agents, and human scientific review.
5. Confirm that the resulting records follow the selected EnzymeML specification without losing important information.

### Stage 2 — Apply it to researcher workflows

6. Select a small set of representative enzyme reaction or kinetics workflows and define what users consider useful.
7. Obtain data-owner approval and agree how the files may be processed, stored, and shared.
8. Apply the established workflow to their files and let researchers review, correct, and approve the candidate records.
9. Evaluate record quality, usability, time saved, and willingness to use ARIADNE again.

## Evaluation

The pilot should assess both record quality and user experience.

**Record quality:** Are extracted values supported by exact source evidence, are metadata and units represented correctly, and do deterministic checks and verifier agents detect errors and ambiguity?

**User experience:** Do researchers understand the candidate record and clarification questions, can they correct it with reasonable effort, does the workflow save time, and would they use it again?