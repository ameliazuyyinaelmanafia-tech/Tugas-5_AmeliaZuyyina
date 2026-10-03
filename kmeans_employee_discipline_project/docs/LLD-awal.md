# Low Level Design (LLD)

## 1. Modul Periode dan Dataset
Tanggung jawab:
- memilih bulan dan tahun
- mengambil data presensi
- memvalidasi dataset

## 2. Modul Selection
Memilih:
- X1 = persentase pemenuhan jam kerja
- X2 = persentase kehadiran

## 3. Modul Preprocessing
- mengubah data hadir, tidak hadir, dan tidak memenuhi menjadi persentase
- membatasi pemenuhan jam kerja maksimum 120%
- membatasi kehadiran pada 0–100%

## 4. Modul Transformation
Normalisasi Min-Max:
X' = (X - Xmin) / (Xmax - Xmin)

## 5. Modul K-Means
K=3:
- C1: tinggi
- C2: sedang
- C3: rendah

Centroid awal:
- minimum
- mean
- maksimum

Jarak Euclidean:
d = sqrt((x1-c1)^2 + (x2-c2)^2)

Centroid baru:
Ck = Σx / n

Iterasi diulang sampai cluster stabil.

## 6. Modul Evaluation
Silhouette:
s(i) = (b(i)-a(i)) / max(a(i),b(i))

Output:
- nilai Silhouette setiap data
- rata-rata Silhouette Score

## 7. Modul Interpretation
Memetakan:
- C1 → kedisiplinan tinggi
- C2 → kedisiplinan sedang
- C3 → kedisiplinan rendah
