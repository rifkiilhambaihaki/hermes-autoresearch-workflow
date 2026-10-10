# Hermes AutoResearch Methodology

## 1. Konsep AutoResearch

AutoResearch adalah workflow riset iteratif yang menggabungkan pembuatan eksperimen, verifikasi metrik, keputusan keep/discard, dan pelaporan sistematis.

Workflow konseptual:

```text
Goal → Scope → Metric → Verify → Modify → Keep/Discard → Log → Repeat
```

## 2. Adaptasi untuk Hermes Agent

Dalam Hermes, workflow ini diadaptasi menjadi:

```text
Hermes buat notebook → user menjalankan di Google Colab → Hermes membaca hasil metrik → Hermes memutuskan keep/discard → Hermes membuat eksperimen berikutnya → Hermes membuat laporan akhir
```

## 3. Peran Hermes Agent

Hermes bertugas untuk:

- membuat struktur project,
- menginspeksi dataset,
- membuat notebook Colab,
- membaca hasil eksperimen,
- menganalisis metrik,
- menyarankan eksperimen berikutnya,
- membuat laporan akhir,
- menjaga batasan keamanan folder.

Hermes tidak menjalankan training berat di VPS.

## 4. Peran Google Drive

Google Drive menjadi workspace utama untuk:

- dataset,
- notebooks,
- results,
- models,
- reports,
- README,
- final artifacts.

## 5. Peran Google Colab

Google Colab digunakan untuk:

- training baseline,
- transfer learning,
- fine-tuning,
- evaluasi model,
- inference/testing.

## 6. Prinsip Evaluasi Model

Pada tahap iterasi dan model selection, model dibandingkan menggunakan validation set berdasarkan:

- validation accuracy,
- validation loss,
- precision macro,
- recall macro,
- F1 macro,
- precision/recall/F1 weighted,
- confusion matrix,
- classification report,
- training curve,
- stabilitas validation accuracy/loss,
- indikasi overfitting/underfitting.

Held-out test set tidak digunakan berulang kali untuk tuning atau keputusan keep/discard. Setelah kandidat model dan konfigurasi dipilih menggunakan validation evidence, test set digunakan untuk evaluasi final yang disetujui. Semua laporan harus menyatakan split asal setiap metrik.

## 7. Prinsip Keep/Discard

Model direkomendasikan untuk di-keep jika metrik validation utama meningkat dan performa antar kelas stabil; keputusan tetap berada pada peneliti.

Model direkomendasikan untuk di-discard jika accuracy tinggi tetapi F1 macro rendah, ada kelas yang gagal dikenali, validation loss tidak stabil, atau ada indikasi data leakage.

## 8. Prinsip Keamanan Folder

Hermes hanya boleh bekerja pada folder project yang ditentukan. Dataset asli tidak boleh dihapus, direname, atau dimodifikasi tanpa instruksi eksplisit.

## 9. Batasan untuk Riset Citra Medis

Untuk citra medis atau gigi, model harus diposisikan sebagai prototipe riset/eksperimen, bukan alat diagnosis klinis mandiri. Validasi eksternal, review ahli, dan uji klinis diperlukan sebelum penggunaan nyata.
