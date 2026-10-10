# Keep/Discard Decision Checklist

## Keep jika

- [ ] F1-score macro meningkat.
- [ ] Recall macro meningkat atau stabil.
- [ ] Validation loss membaik atau tetap stabil pada kondisi eksperimen yang sebanding.
- [ ] Confusion matrix membaik.
- [ ] Kelas lemah membaik.
- [ ] Overfitting berkurang.
- [ ] Model lebih stabil.
- [ ] Model lebih efisien atau masih layak digunakan.

## Discard jika

- [ ] Accuracy tinggi tetapi F1 macro rendah.
- [ ] Recall salah satu kelas sangat rendah.
- [ ] Validation loss naik terus.
- [ ] Gap train-validation terlalu besar.
- [ ] Confusion matrix menunjukkan bias kelas.
- [ ] Ada indikasi data leakage.

Held-out test tidak digunakan berulang kali untuk keputusan keep/discard. Gunakan test set hanya untuk evaluasi final yang telah disetujui.
