# Software Requirements Specification (SRS)

## 1. Functional Requirements

### FR-01 Pemilihan Periode
Sistem menyediakan pilihan periode bulan dan tahun untuk menentukan data presensi yang akan dianalisis.

### FR-02 Pemuatan Dataset
Sistem memuat data presensi sesuai periode yang dipilih.

### FR-03 Selection
Sistem memilih variabel persentase pemenuhan jam kerja dan persentase kehadiran sebagai atribut clustering.

### FR-04 Preprocessing
Sistem melakukan pembersihan dan validasi nilai. Persentase pemenuhan jam kerja dibatasi maksimum 120%, sedangkan persentase kehadiran berada pada rentang 0–100%.

### FR-05 Transformation
Sistem melakukan normalisasi Min-Max agar skala variabel sebanding.

### FR-06 K-Means
Sistem menjalankan K-Means dengan k=3 dan centroid awal Min–Mean–Max.

### FR-07 Evaluation
Sistem menghitung Silhouette Score untuk mengevaluasi kualitas klaster.

### FR-08 Interpretation
Sistem memetakan C1, C2, dan C3 menjadi kedisiplinan tinggi, sedang, dan rendah.

### FR-09 Tampilan
Sistem menampilkan hasil klasterisasi dan informasi tingkat kedisiplinan.

### FR-10 Pengujian
Fungsi utama sistem dapat diuji menggunakan blackbox testing.

## 2. Business Rules
- Dataset harus memiliki data presensi yang relevan.
- Atribut utama adalah X1 dan X2.
- Jumlah klaster adalah 3.
- Data ditempatkan pada centroid dengan jarak Euclidean terkecil.
- Centroid diperbarui menggunakan rata-rata anggota klaster.
- Proses berulang sampai konvergen.

## 3. Data Requirements
Entitas utama:
- users
- attendance_periods
- attendance_records
- clustering_runs
- centroids
- cluster_results
- evaluations

## 4. Acceptance Criteria
Sistem dianggap berhasil apabila periode dapat dipilih, data presensi dimuat, preprocessing dan normalisasi berjalan, K-Means menghasilkan tiga klaster, evaluasi Silhouette Score dapat ditampilkan, dan hasil kategori kedisiplinan ditampilkan.
