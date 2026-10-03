# Product Requirements Document (PRD)

## 1. Ringkasan Produk
Aplikasi web untuk mengolah data presensi pegawai dan mengelompokkan tingkat kedisiplinan menggunakan algoritma K-Means. Sistem mengikuti tahapan Knowledge Discovery in Databases (KDD): selection, preprocessing, transformation, data mining, evaluation, dan interpretation.

## 2. Masalah
Sistem kepegawaian telah merekam presensi secara digital, tetapi data tersebut masih terbatas untuk kebutuhan administratif dan belum dimanfaatkan secara optimal untuk menghasilkan informasi analitis mengenai tingkat kedisiplinan pegawai.

## 3. Tujuan Produk
- Mengolah data presensi menjadi informasi analitis.
- Mengelompokkan pegawai berdasarkan karakteristik kehadiran dan pemenuhan jam kerja.
- Menghasilkan tiga kategori kedisiplinan.
- Menyediakan evaluasi kualitas klaster menggunakan Silhouette Score.
- Menampilkan hasil klasterisasi secara otomatis.

## 4. Target Pengguna
- Admin/pengelola sistem kepegawaian.
- Pihak manajemen yang melakukan monitoring dan evaluasi kedisiplinan.

## 5. Fitur Utama
### Must Have
- Pemilihan periode bulan.
- Pemilihan periode tahun.
- Pemuatan dataset presensi.
- Selection atribut.
- Preprocessing dan validasi.
- Normalisasi Min-Max.
- Proses K-Means.
- Proses bertahap hingga konvergen.
- Hasil otomatis.
- Tampilan kategori kedisiplinan.
- Evaluasi Silhouette Score.

### Should Have
- Dashboard pegawai.
- Riwayat hasil klasterisasi.
- Visualisasi hasil.
- Export hasil.

## 6. Non-Functional Requirements
- Antarmuka mudah digunakan.
- Hasil konsisten dengan perhitungan K-Means.
- Validasi data.
- Proses dapat dijalankan pada data numerik terstruktur.
- Informasi pegawai ditampilkan secara aman/anonim sesuai kebutuhan.
