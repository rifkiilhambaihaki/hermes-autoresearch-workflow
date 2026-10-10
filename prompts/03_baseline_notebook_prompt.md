# Prompt 03 — Baseline Notebook

Buat notebook baseline Google Colab untuk `{Nama Project}`.

Tujuan: memastikan pipeline dataset, preprocessing, training baseline, evaluasi, dan penyimpanan hasil berjalan.

Notebook: `notebooks/{Nama Project}_baseline_colab.ipynb`

Isi wajib:
1. Mount Google Drive.
2. Set path project: `{Path Google Drive}`.
3. Load dataset dari `dataset/`.
4. Buat dataframe: `filepath`, `filename`, `class_name`, `label`, `group_id`.
5. Split train/validation/test 70/15/15 secara stratified dan group-aware bila ada indikasi augmentasi.
6. Simpan split ke `results/baseline_split_assignments.csv`.
7. Preprocessing `{Jenis Data}`: resize, normalisasi, augmentation ringan untuk train.
8. Custom CNN baseline.
9. Callback: EarlyStopping, ReduceLROnPlateau, ModelCheckpoint.
10. Evaluasi: accuracy, loss, precision, recall, F1-score, confusion matrix, classification report.
11. Simpan output baseline ke `results/` dan model ke `models/baseline_model.keras`.
12. Tambahkan fungsi `predict_image(image_path)`.
13. Tambahkan markdown penjelasan setiap bagian.

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
