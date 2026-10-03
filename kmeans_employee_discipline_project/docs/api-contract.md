# API Contract

## GET /api/attendance/periods
Mengambil daftar periode presensi.

## GET /api/attendance
Mengambil data presensi berdasarkan bulan dan tahun.

## POST /api/clustering/runs
Memulai proses K-Means.

Request:
```json
{
  "month": 12,
  "year": 2025,
  "k": 3
}
```

## POST /api/clustering/{id}/step
Menjalankan satu tahap/iterasi K-Means.

## POST /api/clustering/{id}/automatic
Menjalankan K-Means sampai konvergen.

## GET /api/clustering/{id}/centroids
Mengambil centroid setiap iterasi.

## GET /api/clustering/{id}/results
Mengambil hasil cluster dan kategori kedisiplinan.

## GET /api/clustering/{id}/evaluation
Mengambil Silhouette Score.

Response:
```json
{
  "silhouette_score": 0.500844,
  "clusters": {
    "C1": "tinggi",
    "C2": "sedang",
    "C3": "rendah"
  }
}
```
