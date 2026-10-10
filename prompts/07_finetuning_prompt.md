# Prompt 07 — Fine-Tuning Notebook

Buat notebook fine-tuning untuk model terbaik sementara `{Nama Project}`.

Notebook: `notebooks/{Nama Project}_finetuning_colab.ipynb`

Isi wajib:
1. Mount Google Drive.
2. Load split sama dari `results/baseline_split_assignments.csv`.
3. Load model terbaik sementara dari `models/`.
4. Unfreeze sebagian kecil layer terakhir backbone.
5. Learning rate kecil, misalnya `1e-5` atau `1e-6`.
6. Callback: EarlyStopping, ReduceLROnPlateau, ModelCheckpoint.
7. Evaluasi sebelum dan sesudah fine-tuning.
8. Simpan hasil ke `results/final/`.
9. Simpan model ke `models/final_best_model.keras`.
10. Tambahkan aturan: jika fine-tuning lebih buruk, rekomendasikan initial model terbaik.

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
