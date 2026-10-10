# Prompt 08 — Final Audit

Lakukan audit final `{Nama Project}` tanpa training ulang.

Tugas:
1. Baca hasil baseline, transfer learning, dan fine-tuning.
2. Pastikan model/configuration selection dilakukan dari validation evidence, lalu bandingkan held-out test accuracy, test loss, precision, recall, F1-score, confusion matrix, classification report, dan training curve untuk evaluasi final.
3. Gunakan `results/final/final_comparison_initial_vs_finetuning.csv` jika tersedia.
4. Rekomendasikan model final berdasarkan held-out test F1 macro, recall macro, confusion matrix, stabilitas, dan loss; bukan accuracy saja. User harus memverifikasi dan menyetujui keputusan final.
5. Analisis overfitting, underfitting, dan risiko data leakage.
6. Simpan `reports/audit-final-hasil-model.md`.
7. Buat/update `reports/final-report.md` dan `README.md`.

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
