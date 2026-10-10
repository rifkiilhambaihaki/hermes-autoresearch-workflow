# Prompt 06 — Transfer Learning Analysis

Baca `results/experiment_log.csv` dan artefak tiap model untuk `{Nama Project}`.

Analisis:
1. Bandingkan semua model berdasarkan validation `{Metrik Utama}`.
2. Baca classification report setiap model.
3. Analisis confusion matrix setiap model.
4. Analisis training curve: overfitting, underfitting, stabilitas validation loss.
5. Ranking model dengan prioritas: validation F1 macro, validation recall macro, validation confusion matrix, stabilitas curve, validation loss, dan efisiensi. Jangan gunakan held-out test untuk tuning atau ranking berulang.
6. Rekomendasikan kandidat model terbaik sementara dan alasan akademiknya; keputusan keep/discard tetap pada user.
7. Simpan laporan ke `reports/analisis-hasil-transfer-learning.md`.

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
