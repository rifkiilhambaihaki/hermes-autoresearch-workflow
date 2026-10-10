# Quick Start Guide — Hermes AutoResearch Workflow

## 1. Mulai project baru

Gunakan prompt:

```text
prompts/01_project_initialization_prompt.md
```

Isi placeholder seperti nama project, jenis masalah, jenis data, kelas, path Google Drive, dan path lokal.

## 2. Upload dataset

Setelah folder dibuat, upload dataset ke:

```text
{Path Google Drive}/dataset/
```

Struktur disarankan:

```text
dataset/
├── Class_1/
├── Class_2/
└── Class_3/
```

## 3. Inspeksi dataset

Gunakan prompt:

```text
prompts/02_dataset_inspection_prompt.md
```

Hermes akan mengecek kelas, jumlah data, format, corrupt file, duplikasi, dan risiko data leakage.

## 4. Buat notebook baseline

Gunakan prompt:

```text
prompts/03_baseline_notebook_prompt.md
```

User menjalankan notebook di Google Colab.

## 5. Hermes membaca hasil baseline

Gunakan prompt:

```text
prompts/04_baseline_analysis_prompt.md
```

Jika baseline valid, lanjut transfer learning.

## 6. Transfer learning

Gunakan prompt:

```text
prompts/05_transfer_learning_prompt.md
```

User menjalankan notebook di Colab, lalu Hermes membaca `experiment_log.csv`.

## 7. Analisis dan keep/discard

Gunakan prompt:

```text
prompts/06_transfer_learning_analysis_prompt.md
```

Hermes merekomendasikan kandidat model terbaik sementara berdasarkan validation F1 macro, validation recall macro, confusion matrix, dan stabilitas. User memverifikasi evidence dan membuat keputusan keep/discard.

## 8. Fine-tuning

Gunakan prompt:

```text
prompts/07_finetuning_prompt.md
```

User menjalankan fine-tuning di Colab.

## 9. Audit final

Gunakan prompt:

```text
prompts/08_final_audit_prompt.md
```

Hermes menyusun rekomendasi model final berdasarkan artefak yang tersedia. User memverifikasi held-out test evidence dan menyetujui atau menolak rekomendasi tersebut.

## 10. Notebook prediksi dan laporan akhir

Gunakan:

```text
prompts/09_predict_deployment_prompt.md
prompts/10_google_docs_final_report_prompt.md
```

Hasil akhir: model final, notebook predict, final report, executive summary, dan README final.
