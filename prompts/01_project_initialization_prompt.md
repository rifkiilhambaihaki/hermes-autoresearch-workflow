# Prompt 01 — Project Initialization

Mulai project AutoResearch Machine Learning baru.

Nama project: `{Nama Project}`
Jenis masalah: `{Jenis Masalah}`
Jenis data: `{Jenis Data}`
Daftar kelas awal: `{Daftar Kelas}`
Google Drive project: `{Path Google Drive}`
Folder lokal VPS: `{Path Lokal VPS}`

Tugas:
1. Buat folder Google Drive project.
2. Buat folder lokal mirror.
3. Buat struktur folder: `dataset/`, `notebooks/`, `src/`, `results/`, `models/`, `reports/`.
4. Buat `README.md` awal berisi tujuan project, struktur folder, instruksi upload dataset, dan catatan Colab.
5. Jangan membuat kode training sebelum dataset tersedia.
6. Kirim link folder Drive dan instruksi upload dataset.

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
