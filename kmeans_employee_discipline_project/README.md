# K-Means Employee Discipline Clustering Project

## Deskripsi
Proyek ini merupakan rancangan aplikasi berbasis web untuk mengelompokkan tingkat kedisiplinan pegawai berdasarkan data presensi menggunakan algoritma **K-Means Clustering**.

Topik mengacu pada jurnal “Implementasi Algoritma K-Means untuk Klasterisasi Tingkat Kedisiplinan Pegawai pada Sistem Kepegawaian STMIK El Rahma Yogyakarta”.

## Tujuan sistem
1. Mengambil data presensi pegawai berdasarkan periode.
2. Melakukan selection, preprocessing, dan validasi data.
3. Mengubah data presensi menjadi persentase kehadiran dan pemenuhan jam kerja.
4. Melakukan normalisasi Min-Max.
5. Mengelompokkan pegawai dengan K-Means menjadi tiga klaster.
6. Mengevaluasi hasil menggunakan Silhouette Score.
7. Menampilkan kategori kedisiplinan tinggi, sedang, dan rendah.
8. Menyediakan pengujian fungsi sistem.

## Variabel utama
- X1 = persentase pemenuhan jam kerja
- X2 = persentase kehadiran

## Kategori klaster
- C1 = kedisiplinan tinggi
- C2 = kedisiplinan sedang
- C3 = kedisiplinan rendah

## Alur utama
Pilih periode → muat data presensi → selection → preprocessing → normalisasi Min-Max → K-Means → pembaruan centroid → konvergensi → evaluasi Silhouette Score → interpretasi → tampilkan hasil.

## Catatan sumber
Isi teknis dan angka hasil penelitian dalam proyek ini disusun berdasarkan jurnal yang diunggah. Jurnal menggunakan data presensi Desember 2025–Februari 2026, 26 pegawai anonim A–Z, dan menghasilkan rata-rata Silhouette Score 0,500844.
