# Prompt 09 — Predict/Deployment Notebook

Buat notebook testing/deployment untuk `{Nama Project}`.

Notebook: `notebooks/{Nama Project}_predict_colab.ipynb`

Isi wajib:
1. Mount Google Drive.
2. Load model final yang direkomendasikan.
3. Definisikan label kelas `{Daftar Kelas}`.
4. Fungsi `preprocess_image(image_path)`.
5. Fungsi `predict_image(image_path)`.
6. Fitur upload gambar dari komputer.
7. Tampilkan gambar, prediksi kelas, confidence score, dan top-3 prediction.
8. Tambahkan catatan bahwa model adalah prototipe riset, bukan alat keputusan klinis/produksi mandiri.

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
