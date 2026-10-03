# High Level Design (HLD)

## 1. Arsitektur

```text
Browser
   |
   v
Frontend
   |
   v
REST API / Backend
   |
   +---- Attendance Service
   +---- KDD Preprocessing Service
   +---- K-Means Service
   +---- Evaluation Service
   +---- Interpretation Service
   |
   v
Database
```

## 2. Komponen
### Frontend
Menampilkan pemilihan periode, data presensi, proses K-Means, evaluasi, dan hasil kedisiplinan.

### Backend
Mengelola data presensi, proses KDD, clustering, evaluasi, dan API.

### K-Means Service
Melakukan inisialisasi centroid, perhitungan jarak, penentuan cluster, pembaruan centroid, dan iterasi sampai konvergen.

### Evaluation Service
Menghitung Silhouette Score.

### Database
Menyimpan periode, presensi, proses clustering, centroid, hasil cluster, dan evaluasi.

## 3. Alur Klasifikasi/Clustering

```mermaid
flowchart TD
    A[Data Presensi] --> B[Selection]
    B --> C[Preprocessing]
    C --> D[Min-Max Transformation]
    D --> E[K-Means k=3]
    E --> F[Centroid dan Cluster]
    F --> G[Silhouette Score]
    G --> H[Interpretasi]
    H --> I[Informasi Kedisiplinan]
```
