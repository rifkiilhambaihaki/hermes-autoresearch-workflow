# Prompt 10 — Google Docs Final Report

Buat laporan akhir Google Docs untuk `{Nama Project}`.

Isi laporan:
1. Title Page.
2. Project Overview.
3. Dataset Description.
4. Baseline Experiment.
5. Transfer Learning Experiments.
6. Fine-Tuning Experiment.
7. Final Model Decision.
8. Predict/Deployment Notebook.
9. Limitations.
10. Conclusion.
11. Future Work.

Masukkan link artefak penting: notebooks, metrics, confusion matrix, training curve, model final, README, dan reports.
Buat juga executive summary jika diminta.

## Placeholder wajib

Gunakan dan sesuaikan placeholder berikut:

- `{Nama Project}`
- `{Jenis Masalah}`
- `{Jenis Data}`
- `{Daftar Kelas}`
- `{Path Google Drive}`
- `{Path Lokal VPS}`
- `{Model Yang Dicoba}`
- `{Metrik Utama}`
- `{Catatan Khusus Dataset}`

## Batasan keamanan

- Jangan training berat di VPS.
- Training hanya dilakukan di Google Colab jika diperlukan.
- Jangan menghapus atau mengubah dataset asli.
- Jangan membuat cronjob otomatis.
- Jangan akses `/root`, `/etc`, `/var/www`, database production, atau file `.env`.
- Hanya akses folder Google Drive project: `{Path Google Drive}`.
- Hanya akses folder lokal project: `{Path Lokal VPS}`.
- Jika informasi tidak tersedia, tulis `[PERLU KONFIRMASI]`.
