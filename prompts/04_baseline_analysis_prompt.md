# Prompt 04 — Baseline Analysis

Baca hasil baseline `{Nama Project}` dari `results/`.

Analisis:
1. `baseline_metrics.csv`: validation loss, accuracy, precision/recall/F1 macro dan weighted untuk keputusan iterasi. Jika file juga memuat held-out test metrics, pisahkan secara eksplisit dan jangan gunakan test set untuk tuning.
2. `baseline_classification_report.txt`: performa per kelas `{Daftar Kelas}`.
3. `baseline_confusion_matrix.png`: kelas paling benar, kelas paling sering salah, pasangan kelas tertukar.
4. `baseline_training_curve.png`: overfitting, underfitting, stabilitas validation accuracy/loss.
5. `baseline_split_assignments.csv`: distribusi split dan kebocoran `group_id`.
6. Simpan laporan ke `reports/analisis-hasil-baseline.md`.
7. Jika baseline valid, rekomendasikan lanjut transfer learning untuk diputuskan oleh user.

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
