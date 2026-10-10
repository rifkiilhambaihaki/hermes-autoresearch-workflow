# Artifact Index Template — AutoResearch Project

Use this template when creating a final artifact index for an AutoResearch project. Fill only with artifacts that were actually created or inspected. Do not invent links, metrics, or file paths.

## Usage Rules

1. Keep this template with the project's reusable workflow materials.
2. Save the primary `artifact_index.md` in the approved project artifact store.
3. Treat local copies as working copies unless the project plan declares otherwise.
4. Record which approved location is authoritative.
5. Do not overwrite an existing `artifact_index.md` without explicit permission.
6. If `artifact_index.md` already exists, create a timestamped version instead.
7. Do not modify old datasets, models, notebooks, or experiment outputs when creating the artifact index.
8. Add integrity or duplication procedures only when required by the reviewed project plan and approved by the project owner.

## 1. Nama Project

- Project name: `<Project-Name>`
- Project type: `<CNN / GCN / Transformer / YOLO / Paper Audit / Prototype Handoff>`
- Primary project artifact store: `<approved folder path or access-controlled link>`
- Local workspace folder, if any: `<workspace path>`
- Public/private visibility classification: `<public / restricted / private>`

## 2. Tanggal Audit

- Audit date: `<YYYY-MM-DD>`
- Audit stage: `<iteration review / final audit / paper audit / prototype handoff>`
- Auditor/reviewer: `<person or tool, with human approver>`

## 3. Dataset Path

- Dataset source path: `<approved dataset path or access-controlled link>`
- Dataset use mode: `<read-only / copied with permission / split file used>`
- Dataset license/terms and consent status: `<verified terms or needs review>`
- Split file, if used: `<split file path/link>`
- Notes: `<dataset limitation or source-project note>`

## 4. Notebook Colab

- Iteration 01 notebook: `<Colab/Drive link>`
- Iteration 02 notebook: `<Colab/Drive link>`
- Final audit notebook: `<Colab/Drive link>`
- Additional notebook, if any: `<name and link>`

## 5. Model File

- Best model name: `<model name>`
- Best model file: `<Drive path/link>`
- Iteration/source: `<iteration name>`
- Model format: `<.keras / .pt / .pth / .onnx / other>`
- Notes: `<inference constraints or loading notes>`

## 6. Metrics JSON/CSV

- Metrics JSON: `<path/link>`
- Metrics CSV: `<path/link>`
- Ranking/comparison CSV: `<path/link>`
- Training log CSV: `<path/link>`

## 7. Classification Report

- Classification report TXT: `<path/link>`
- Classification report CSV, if available: `<path/link>`
- Per-class summary source: `<path/link>`

## 8. Confusion Matrix PNG/CSV

- Confusion matrix CSV: `<path/link>`
- Confusion matrix PNG: `<path/link>`
- Normalized confusion matrix CSV, if available: `<path/link>`
- Normalized confusion matrix PNG, if available: `<path/link>`

## 9. Training Curves

- Training curve image: `<path/link>`
- Loss curve image, if separate: `<path/link>`
- Accuracy/F1 curve image, if separate: `<path/link>`
- Training stability notes: `<brief note>`

## 10. Final Report Markdown

- Final report Markdown: `<path/link>`
- Report status: `<draft / final / needs revision>`

## 11. Shareable Report

- Report location: `<approved path or access-controlled link>`
- Report status: `<created / updated / not requested>`

## 12. Paper Writing Guide Jika Ada

- Paper writing guide: `<path/link>`
- Status: `<available / not created / not requested>`

## 13. Executive Summary Jika Ada

- Executive summary: `<path/link>`
- Status: `<available / not created / not requested>`

## 14. Keputusan Model Terbaik

- Best model decision: `<selected model>`
- Primary selection metric: `<metric requested by user or default metric>`
- Key metrics:
  - Accuracy: `<value>`
  - Precision macro: `<value>`
  - Recall macro: `<value>`
  - F1 macro: `<value>`
  - F1 weighted: `<value>`
- Main reason: `<brief evidence-based reason>`
- Main limitation: `<brief limitation>`

## 15. Next Steps

- Recommended next step 1: `<action>`
- Recommended next step 2: `<action>`
- Recommended next step 3: `<action>`
- Need user approval before:
  - `<training / inference / deployment / dataset change / manuscript edit / other>`

## Safety Confirmation

- Source dataset modified: `No, unless explicitly approved.`
- Old models/results/reports overwritten: `No, unless explicitly approved.`
- Training/inference automatically run by the assistant: `No, unless explicitly approved and verified.`
- Integrity/duplication procedures added: `<No / Yes, approved and documented>`
- Secrets/credentials displayed: `No.`
- Private links or paths prepared for public release: `No.`
