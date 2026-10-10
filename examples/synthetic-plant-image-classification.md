# Synthetic Plant Image Classification

> **Fictional example only.** This scenario uses invented labels and placeholders to demonstrate the workflow. It does not describe a real dataset or project, and no training, evaluation, or experiment has been executed.

## Scenario

A user wants to prototype an image classifier for synthetic leaf illustrations. Each image belongs to one of three invented visual categories:

- **Aurivela Speckle** — leaves illustrated with gold-like speckles.
- **Cobalune Curl** — leaves illustrated with curled, blue-toned edges.
- **Verdantia Veil** — leaves illustrated with a translucent green overlay.

These labels are fictional categories, not plant species, diseases, or real-world diagnoses.

## Placeholders

Replace these values before using any prompt:

- `{Nama Project}`: `<SYNTHETIC_PROJECT_NAME>`
- `{Jenis Masalah}`: `multiclass image classification`
- `{Jenis Data}`: `synthetic leaf illustrations`
- `{Daftar Kelas}`: `Aurivela Speckle, Cobalune Curl, Verdantia Veil`
- `{Path Google Drive}`: `<PROJECT_DRIVE_FOLDER>`
- `{Path Lokal VPS}`: `<AUTHORIZED_LOCAL_WORKSPACE>`
- `{Model Yang Dicoba}`: `<CANDIDATE_MODEL_NAMES>`
- `{Metrik Utama}`: `<USER_APPROVED_PRIMARY_METRIC>`
- `{Catatan Khusus Dataset}`: `<KNOWN_DATASET_NOTES>`

Keep paths, links, and identifiers project-specific and private. Do not paste credentials into prompts or notebooks.

## Human–Hermes workflow

Hermes prepares prompts, notebook drafts, review notes, and report structures. The human user confirms scope, supplies or uploads the dataset, reviews generated code, and makes approval decisions. Compute-heavy notebook cells are run by the human in Google Colab—not claimed as work performed by Hermes.

After each Colab run, the human saves the produced artifacts in the approved project folder and tells Hermes which files may be inspected. Hermes then reads those artifacts, distinguishes observed evidence from missing information, and proposes the next step. The human decides whether to proceed.

## Workflow stages and expected artifact types

### Project setup

Start with the [project-initialization prompt](../prompts/01_project_initialization_prompt.md) and adapt the [project README template](../templates/README-project-template.md).

Expected artifact types:

- project README (`.md`)
- approved folder structure
- placeholder and scope record (`.md` or `.txt`)

### Dataset readiness

Arrange synthetic images by category without changing the source files. Use the [dataset-inspection prompt](../prompts/02_dataset_inspection_prompt.md), the [dataset inspection template](../templates/dataset-inspection-template.md), and the [dataset-readiness checklist](../checklists/dataset-readiness-checklist.md).

Expected artifact types:

- dataset inventory (`.csv` or `.json`)
- inspection report (`.md`)
- optional issue lists (`.csv` or `.txt`)
- approved split manifest (`.csv` or `.json`)

### Baseline preparation and human execution

Ask Hermes to draft a notebook with the [baseline-notebook prompt](../prompts/03_baseline_notebook_prompt.md). The human reviews it, opens it in Google Colab, selects an appropriate runtime, and executes the cells. The human then saves outputs to the approved project folder.

Expected artifact types, if produced by the Colab run:

- notebook (`.ipynb`)
- experiment log (`.csv` or `.json`)
- evaluation summaries (`.json`, `.csv`, or `.txt`)
- plots (`.png`)
- model checkpoint in the framework's documented format

No baseline artifacts or results are asserted in this example.

### Evidence review and iteration

Provide the saved artifacts to Hermes and use the [baseline-analysis prompt](../prompts/04_baseline_analysis_prompt.md) with the [baseline analysis template](../templates/baseline-analysis-template.md). Review experiment quality with the [experiment-quality checklist](../checklists/experiment-quality-checklist.md). If the evidence supports another iteration, continue with the [transfer-learning prompt](../prompts/05_transfer_learning_prompt.md) and its [analysis prompt](../prompts/06_transfer_learning_analysis_prompt.md).

Expected artifact types:

- evidence-based analysis (`.md`)
- comparison or ranking data (`.csv`)
- keep/discard decision record (`.md`)
- next notebook draft (`.ipynb`)

Any subsequent notebook is again reviewed and executed by the human in Colab. Missing or invalid artifacts remain marked as unresolved rather than being inferred.

### Optional refinement and final review

Only after human approval, use the [fine-tuning prompt](../prompts/07_finetuning_prompt.md). When the available evidence is complete, use the [final-audit prompt](../prompts/08_final_audit_prompt.md), [final-audit checklist](../checklists/final-audit-checklist.md), and [final report template](../templates/final-report-template.md).

Expected artifact types:

- human-executed refinement notebook (`.ipynb`), if approved
- final audit (`.md`)
- final report (`.md`)
- artifact index (`.md`)
- prediction notebook (`.ipynb`), if requested and reviewed

The final documents should link only to artifacts that actually exist, state limitations, and avoid presenting planned or missing outputs as measured evidence.
