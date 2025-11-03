# BMW Car Price Prediction - Portfolio Project

Sebuah aplikasi web berbasis Streamlit untuk memprediksi harga mobil BMW berdasarkan berbagai fitur menggunakan machine learning.

## Struktur Proyek
```
bmw_streamlit_portfolio/
│
├── app.py                         # Aplikasi Streamlit utama
├── data/
│   └── bmw_car_sales.csv         # Dataset BMW
├── model/
│   └── bmw_model.pkl             # Model ML yang sudah dilatih
├── assets/                       # Gambar dan media
├── notebooks/                    # Jupyter notebooks
└── requirements.txt              # Dependencies
```

## Fitur Utama
- Prediksi harga mobil BMW
- Visualisasi data interaktif
- Analisis data eksploratori
- Portfolio proyek data science

## Cara Menjalankan Aplikasi

1. Clone repository ini
```bash
git clone https://github.com/username/bmw_streamlit_portfolio.git
cd bmw_streamlit_portfolio
```

2. Buat virtual environment (opsional tapi direkomendasikan)
```bash
python -m venv venv
source venv/bin/activate  # Untuk Unix/macOS
# atau
venv\Scripts\activate     # Untuk Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Jalankan aplikasi
```bash
streamlit run app.py
```

## Dataset
Dataset berisi informasi penjualan mobil BMW dengan fitur-fitur:
- Year (Tahun)
- Model
- Mileage (Kilometer)
- Fuel Type (Jenis Bahan Bakar)
- dan lainnya

## Model
Model machine learning dilatih menggunakan algoritma Random Forest dengan fitur-fitur yang telah dioptimasi.

## Author
Febriansyah Syafaat

## License
This project is licensed under the MIT License - see the LICENSE file for details