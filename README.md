# Analisis Sentimen - Naive Bayes + Lexicon

Aplikasi web untuk menganalisis sentimen teks ulasan berbahasa Indonesia menggunakan model **Multinomial Naive Bayes** yang dikombinasikan dengan fitur **Lexicon-based**. Dibangun dengan **Streamlit** untuk deployment yang mudah dan cepat.

---

## Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Teknologi](#teknologi)
- [Arsitektur Model](#arsitektur-model)
- [Struktur Proyek](#struktur-proyek)
- [Instalasi](#instalasi)
- [Menjalankan Aplikasi](#menjalankan-aplikasi)
- [Deployment](#deployment)
- [Performa Model](#performa-model)
- [Preprocessing Pipeline](#preprocessing-pipeline)

---

## Fitur Utama

- **Dashboard** -- Ringkasan performa model, KPI utama, dan distribusi label dataset
- **Live Prediction** -- Prediksi sentimen satu ulasan dalam satu panel ringkas
- **Model Performance** -- Confusion matrix, classification report, dan ringkasan metrik
- **About System** -- Arsitektur, metodologi, dan spesifikasi pipeline

---

## Teknologi

| Komponen           | Teknologi                                             |
| ------------------ | ----------------------------------------------------- |
| Framework Web      | Streamlit                                             |
| Model ML           | Multinomial Naive Bayes (scikit-learn)                |
| Feature Extraction | TF-IDF + Lexicon (CountVectorizer)                    |
| Preprocessing      | Regex, Sastrawi Stopwords, Custom Slang Normalization |
| Bahasa             | Python 3.9+                                           |

---

## Arsitektur Model

Model menggunakan pipeline sklearn yang terdiri dari:

1. **FeatureUnion** -- menggabungkan dua fitur extractor:
   - **TF-IDF Vectorizer** -- unigram hingga trigram, max 150,000 fitur, sublinear TF
   - **Lexicon CountVectorizer** -- 242 kata sentimen (positif, negatif, netral + negasi)
2. **Multinomial Naive Bayes** -- classifier dengan alpha=0.1, fit_prior=False

### Konfigurasi Terbaik

| Parameter         | Nilai                     |
| ----------------- | ------------------------- |
| Alpha (smoothing) | 0.1                       |
| Fit Prior         | False                     |
| Lexicon Weight    | 1.0                       |
| ROS Ratio         | None (tanpa oversampling) |
| Stemming          | Tidak digunakan           |

---

## Struktur Proyek

```
web/
|-- model.pkl                              # Model terlatih (pipeline + metadata)
|-- assets/
|   |-- metrics/                           # metrics.json, epoch_history.csv, confusion_matrix.csv, dataset_summary.json
|-- requirements.txt                       # Dependensi Python
|-- README.md                              # Dokumentasi ini
|-- naive_bayes_lexicon_improved.ipynb      # Notebook training model
|-- app/
|   |-- main.py                            # Entry point Streamlit
|   |-- data/                              # Loader model, metrics, preprocess
|   |-- pages/                             # Dashboard, Prediction, Performance, About
|   |-- ui/                                # Theme & UI components
```

---

## Instalasi

### Prasyarat

- Python 3.9 atau lebih baru
- pip (Python package manager)

### Langkah Instalasi

```bash
# 1. Clone atau navigasi ke direktori proyek
cd projects/web

# 2. Buat virtual environment (opsional tapi disarankan)
python -m venv venv
source venv/bin/activate  # macOS/Linux
# atau
venv\Scripts\activate     # Windows

# 3. Install dependensi
pip install -r requirements.txt
```

---

## Menjalankan Aplikasi

```bash
# Dari direktori web/
streamlit run app/main.py
```

Jika `model.pkl` belum ada, aplikasi akan otomatis mengunduhnya dari Google Drive.
Set salah satu environment variable berikut sebelum menjalankan Streamlit:

```bash
# Opsi 1: gunakan link Google Drive
export GDRIVE_MODEL_URL="https://drive.google.com/file/d/FILE_ID/view?usp=sharing"

# Opsi 2: gunakan file ID saja
export GDRIVE_MODEL_ID="FILE_ID"
```

### Streamlit Community Cloud (Secrets)

Jika deploy ke Streamlit Cloud, simpan ID di **Secrets**:

1. Buka app di Streamlit Cloud
2. Settings → Secrets
3. Tambahkan:

```toml
GDRIVE_MODEL_ID = "FILE_ID"
```

Aplikasi akan terbuka di browser pada `http://localhost:8501`.

## Metrics Assets & Google Drive

Aplikasi membaca file berikut dari `assets/metrics/`:

- `metrics.json`
- `epoch_history.csv`
- `confusion_matrix.csv`
- `dataset_summary.json`

Jika file tidak ada, aplikasi akan mencoba mengunduh otomatis dari Google Drive. Pilih salah satu opsi env berikut:

```bash
# Opsi 1: satu folder berisi semua file metrics
export GDRIVE_METRICS_FOLDER_URL="https://drive.google.com/drive/folders/FOLDER_ID"

# Opsi 2: file ID per asset
export GDRIVE_METRICS_JSON_ID="FILE_ID"
export GDRIVE_EPOCH_HISTORY_ID="FILE_ID"
export GDRIVE_CONFUSION_MATRIX_ID="FILE_ID"
export GDRIVE_DATASET_SUMMARY_ID="FILE_ID"
```

Notebook `naive_bayes_lexicon_improved.ipynb` mengekspor file metrics ke folder ini.

### Opsi Tambahan

```bash
# Menentukan port khusus
streamlit run app/main.py --server.port 8080

# Menjalankan dalam mode headless (tanpa membuka browser)
streamlit run app/main.py --server.headless true

# Menjalankan dengan alamat tertentu
streamlit run app/main.py --server.address 0.0.0.0
```

---

## Deployment

### Streamlit Community Cloud

1. Push proyek ke repository GitHub
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Hubungkan repository
4. Set main file path: `app/main.py`
5. Deploy

### Docker (Opsional)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## Performa Model

### Evaluasi pada Test Set (14,489 sampel)

| Metrik          | Nilai      |
| --------------- | ---------- |
| **Accuracy**    | **82.06%** |
| Macro F1        | 0.6873     |
| Macro Precision | 0.6861     |
| Macro Recall    | 0.6985     |

### Performa per Kelas

| Kelas   | Precision | Recall | F1-Score | Support |
| ------- | --------- | ------ | -------- | ------- |
| Negatif | 0.8413    | 0.8920 | 0.8659   | 6,268   |
| Netral  | 0.2563    | 0.3673 | 0.3019   | 1,225   |
| Positif | 0.9609    | 0.8360 | 0.8941   | 6,996   |

### Catatan

- Kelas **Netral** memiliki performa rendah karena proporsi data yang jauh lebih kecil dan ambiguitas isi teks
- Kelas **Positif** memiliki precision tertinggi (0.96)
- Kelas **Negatif** memiliki recall tertinggi (0.89)

---

## Preprocessing Pipeline

Preprocessing yang digunakan terdiri dari beberapa tahap:

1. **Text Cleaning** -- Menghapus URL, mention, hashtag, angka, dan karakter spesial
2. **Repeated Character Normalization** -- `baguuuuss` menjadi `baguuss`
3. **Slang Normalization** -- Mengubah singkatan/slang ke bentuk baku (`gk` -> `gak`, `bgt` -> `banget`, dll.)
4. **Negation Handling** -- Menggabungkan kata negasi dengan kata berikutnya (`tidak bagus` -> `tidak_bagus`)
5. **Stopword Removal** -- Menghapus kata umum sambil mempertahankan kata negasi dan kontras (`tapi`, `namun`, `cuman`, dll.)

### Tanpa Stemming

Stemming sengaja **tidak digunakan** karena:

- Runtime sangat lama pada dataset besar
- Kenaikan akurasi yang tidak signifikan
- Fokus perbaikan akurasi ada di normalisasi slang dan negation handling

---

## Dataset

- **Sumber**: Google Play Store Reviews - Shopee 12.12
- **Total**: 85,290 ulasan (setelah cleaning)
- **Distribusi**: Positif (39,924) | Netral (8,538) | Negatif (36,828)
- **Labeling**: Berdasarkan rating bintang (1-2: Negatif, 3: Netral, 4-5: Positif)
- **Label Noise Filter**: 12,848 data (15.1%) dihapus karena isi teks bertentangan dengan rating
- **Split**: 80% Training | 20% Testing

---

## Lisensi

Proyek ini dibuat sebagai bagian dari tugas skripsi.
