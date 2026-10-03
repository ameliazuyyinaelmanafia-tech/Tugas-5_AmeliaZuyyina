# Use Cases

## UC-01 Pilih Periode
**Aktor:** Admin  
**Tujuan:** Menentukan periode data presensi.

Alur:
1. Admin membuka halaman clustering.
2. Admin memilih bulan.
3. Admin memilih tahun.
4. Sistem memuat dataset presensi.

## UC-02 Proses K-Means
**Aktor:** Admin  
**Tujuan:** Mengelompokkan tingkat kedisiplinan.

Alur:
1. Sistem melakukan selection.
2. Sistem melakukan preprocessing.
3. Sistem melakukan normalisasi Min-Max.
4. Sistem menentukan centroid awal C1, C2, C3.
5. Sistem menghitung jarak Euclidean.
6. Sistem menentukan cluster terdekat.
7. Sistem menghitung centroid baru.
8. Sistem mengulangi proses sampai konvergen.
9. Sistem menyimpan hasil klaster.

## UC-03 Evaluasi
**Aktor:** Admin  
**Tujuan:** Menilai kualitas hasil clustering.

Alur:
1. Sistem menghitung a(i).
2. Sistem menghitung b(i).
3. Sistem menghitung s(i).
4. Sistem menghitung rata-rata Silhouette Score.
5. Sistem menampilkan hasil evaluasi.

## UC-04 Lihat Informasi Kedisiplinan
**Aktor:** Admin/Manajemen  
**Tujuan:** Melihat kategori kedisiplinan pegawai.

Alur:
1. Pengguna membuka hasil clustering.
2. Sistem menampilkan pegawai dan cluster.
3. Sistem menampilkan kategori kedisiplinan.
