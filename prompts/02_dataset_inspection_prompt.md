# Prompt 02 — Dataset Inspection

Dataset untuk `{Nama Project}` sudah diupload ke `{Path Google Drive}/dataset/`.

Tugas inspeksi:
1. Baca struktur folder kelas `{Daftar Kelas}`.
2. Hitung jumlah gambar per kelas dan total gambar.
3. Deteksi format file, resolusi, mode warna, file corrupt, file non-gambar.
4. Cek duplikasi nama file dan kemungkinan duplikasi gambar.
5. Cek indikasi data leakage, termasuk pola augmentasi seperti `_aug_`.
6. Analisis keseimbangan dataset.
7. Rekomendasikan preprocessing, resize, augmentation, dan split train/validation/test.
8. Simpan laporan ke `reports/dataset-inspection.md`.
9. Jangan mengubah dataset asli.

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
