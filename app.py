# ===============================================================
# Aplikasi Prediksi Harga Mobil BMW
# Dibuat oleh: [Febriansyah Syafaat]
# Deskripsi: Aplikasi Streamlit sederhana untuk memprediksi harga
# mobil BMW berdasarkan fitur seperti tahun, jarak tempuh, mesin,
# bahan bakar, transmisi, dan tipe model.
# ===============================================================

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import joblib
from PIL import Image

# ---------------------------------------------------------------
# 1. Judul dan Deskripsi Aplikasi
# ---------------------------------------------------------------
st.set_page_config(page_title="BMW Price Prediction", page_icon="🚗")

st.title("🚗 Prediksi Harga Mobil BMW")
st.write(
    """
    Aplikasi ini menggunakan model *Machine Learning* untuk memprediksi harga mobil BMW
    berdasarkan detail seperti tahun pembuatan, jarak tempuh, jenis bahan bakar, transmisi, dan ukuran mesin.
    """
)

# ---------------------------------------------------------------
# 2. Setup Paths & Load Assets
# ---------------------------------------------------------------
# Get absolute paths
CURRENT_DIR = Path(__file__).parent
MODEL_PATH = CURRENT_DIR / "model" / "bmw_model.pkl"
ASSETS_PATH = CURRENT_DIR / "assets"
PROFILE_PHOTO = ASSETS_PATH / "profile_febriansyah.jpg"

@st.cache_resource
def load_model():
    """Load model with better error handling"""
    try:
        model = joblib.load(MODEL_PATH)
        st.success("✅ Model berhasil dimuat dan siap digunakan.")
        return model
    except FileNotFoundError:
        st.warning(f"⚠️ File model tidak ditemukan di {MODEL_PATH}")
        st.info("💡 Jalankan notebook training terlebih dahulu untuk membuat model.")
        return None
    except Exception as e:
        st.error(f"❌ Error saat memuat model: {str(e)}")
        return None

# Load model
model = load_model()

# ---------------------------------------------------------------
# 3. Sidebar Profil (Tentang Saya)
# ---------------------------------------------------------------
st.sidebar.title("👤 Tentang Saya")

def load_profile_pic(path):
    try:
        if path.exists():
            # .convert("RGB") akan mengubah data gambar mentah 
            # menjadi format warna yang dipahami Python
            img = Image.open(path).convert("RGB") 
            return img
        return None
    except:
        
        return None

# Panggil fungsinya
profile_img = load_profile_pic(PROFILE_PHOTO)

if profile_img:
    st.sidebar.image(profile_img, width=200)
else:
    # Tampilkan teks ramah sebagai pengganti jika foto error
    st.sidebar.info("📷 Foto Profil")

st.sidebar.markdown("""
**Nama:** Febriansyah Syafaat  
**Peran:** Student AI & Machine Learning  
**Project:** Streamlit Mini Project — Prediksi Harga BMW  
**Deskripsi:**  
Saya sedang membangun fondasi karier di bidang Artificial Intelligence, dengan fokus pada Machine Learning dan penerapan praktisnya dalam bisnis dan pelayanan publik.  
Melalui proyek ini, saya belajar bagaimana data bisa diubah menjadi keputusan yang bernilai.
""")

# ---------------------------------------------------------------
# 4. Input Data dari Pengguna
# ---------------------------------------------------------------
st.header("BMW")

col1, col2 = st.columns(2)
with col1:
    year = st.number_input("Tahun Pembuatan", min_value=1990, max_value=2025, value=2018)
    mileage = st.number_input("Jarak Tempuh (dalam km)", min_value=0, max_value=300000, value=50000)
    engine_size = st.number_input("Ukuran Mesin (L)", min_value=0.5, max_value=5.0, value=2.0, step=0.1)
with col2:
    transmission = st.selectbox("Transmisi", ["Manual", "Automatic", "Semi-Auto"])
    fuel_type = st.selectbox("Jenis Bahan Bakar", ["Petrol", "Diesel", "Hybrid", "Electric"])
    model_type = st.selectbox("Model", ["1 Series", "3 Series", "5 Series", "X1", "X3", "X5"])

# ---------------------------------------------------------------
# 5. Konversi Input ke Bentuk DataFrame
# ---------------------------------------------------------------
input_data = pd.DataFrame({
    "year": [year],
    "mileage": [mileage],
    "engine_size": [engine_size],
    "transmission": [transmission],
    "fuel_type": [fuel_type],
    "model": [model_type]
})

st.subheader("📊 Data Input")
st.write(input_data)

# ---------------------------------------------------------------
# 6. One-Hot Encoding (Sama seperti saat training)
# ---------------------------------------------------------------
input_encoded = pd.get_dummies(input_data)

# Align features with model if model is available
if model is not None and hasattr(model, "feature_names_in_"):
    model_columns = model.feature_names_in_
    # Tambahkan kolom yang hilang biar urutannya sama
    for col in model_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    # Pastikan urutan kolom sesuai model
    input_encoded = input_encoded[model_columns]
else:
    model_columns = input_encoded.columns
    input_encoded = input_encoded[model_columns]

# ---------------------------------------------------------------
# 7. Prediksi Harga
# ---------------------------------------------------------------
if st.button("Prediksi Harga Mobil"):
    if model is None:
        st.error("Model belum dimuat. Silakan latih model dan simpan ke `model/bmw_model.pkl`.")
    else:
        try:
            prediction = model.predict(input_encoded)
            st.success(f"Perkiraan harga mobil BMW ini sekitar **£{prediction[0]:,.2f}**")
        except Exception as e:
            st.error(f"Gagal melakukan prediksi: {e}")
    # ---------------------------------------------------------------
    # ---------------------------------------------------------------
# 8. Tentang Saya & Proyek Saya
# ---------------------------------------------------------------

st.markdown("---")
st.header("👨‍💻 Tentang Saya")

st.markdown("""
### **Febriansyah Syafaat**
Lulusan **S1 Manajemen - Universitas Gunadarma** dengan pengalaman di bidang **pelayanan publik dan administrasi pemerintahan**.  
Saat ini saya berfokus membangun karier di bidang **Artificial Intelligence (AI)**, khususnya pada **Machine Learning** dan penerapan praktisnya untuk mendukung bisnis serta efisiensi pelayanan publik.  

Saya memiliki minat besar terhadap data, analitik, serta bagaimana teknologi dapat membantu pengambilan keputusan berbasis insight nyata.
""")

st.markdown("""
📫 **Kontak:**
- Email: febriansyah.syafaat@gmail.com  
- LinkedIn: [linkedin.com/in/febriansyahsyafaat](https://linkedin.com/in/febriansyahsyafaat)
- Portfolio: [https://github.com/febriansyahsyafaat](https://github.com/febriansyahsyafaat)
""")

st.markdown("---")
st.header("📂 Proyek Saya")

st.subheader("1. BMW Car Price Prediction App")
st.markdown("""
Aplikasi prediksi harga mobil BMW menggunakan **Machine Learning (Random Forest)** dan **Streamlit** sebagai antarmuka web interaktif.  
Menunjukkan kemampuan membangun **end-to-end ML pipeline** dari data preprocessing, training model, hingga deployment web.
""")

st.subheader("2. Customer Service AI Chatbot (RULS Casual)")
st.markdown("""
Chatbot berbasis **Large Language Model (LLM)** untuk membantu brand dalam melayani pertanyaan pelanggan di **Instagram dan WhatsApp Business**.  
Proyek ini mengasah keterampilan **prompt engineering** dan integrasi model AI ke use case bisnis.
""")

st.subheader("3. Data Analysis & Visualization Project")
st.markdown("""
Analisis eksploratif dan visualisasi data penjualan produk menggunakan **Pandas, Matplotlib, dan Seaborn**.  
Fokus proyek ini adalah menemukan insight dari data serta menampilkan tren penjualan dan pola pelanggan secara visual.
""")