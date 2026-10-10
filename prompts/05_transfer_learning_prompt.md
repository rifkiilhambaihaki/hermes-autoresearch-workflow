# Prompt 05 — Transfer Learning Experiments

Buat notebook transfer learning untuk `{Nama Project}`.

Notebook: `notebooks/{Nama Project}_transfer_learning_experiments.ipynb`

Model yang dicoba: `{Model Yang Dicoba}`

Isi wajib:
1. Mount Google Drive dan set path project `{Path Google Drive}`.
2. Load split yang sama dari `results/baseline_split_assignments.csv`.
3. Gunakan preprocessing sesuai model pretrained.
4. Resize gambar, augmentation ringan train-only, class weight jika tidak seimbang.
5. Fungsi modular: `build_model`, `train_model`, `evaluate_model`, `plot_training_curve`, `save_confusion_matrix`, `save_classification_report`.
6. Simpan `results/experiment_log.csv`.
7. Simpan confusion matrix, training curve, classification report tiap model.
8. Simpan model terbaik setiap arsitektur ke `models/`.
9. Tambahkan ranking berdasarkan validation `{Metrik Utama}`, validation loss, dan stabilitas validation curve. Jangan gunakan held-out test set untuk ranking iteratif.

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
