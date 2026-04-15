import streamlit as st

# ====== CONFIG ======
st.set_page_config(page_title="Sistem Rekomendasi Wisata", layout="centered")

# ====== CSS ======
st.markdown("""
<style>
body {
    background-color: #0e1117;
}

h1 {
    color: white;
    text-align: center;
}

/* Card hasil */
.result-box {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #333;
    margin-top: 20px;
}

/* Tombol */
div.stButton > button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
}

/* Hover tombol */
div.stButton > button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

# ====== HEADER ======
st.title("🌍 Sistem Rekomendasi Tempat Wisata")
st.markdown("### ✨ Temukan wisata terbaik sesuai kebutuhan Anda")
st.write("Sistem Cerdas berbasis Rule (IF-ELSE)")

# ====== INPUT (5 PARAMETER) ======
budget = st.selectbox("💰 Pilih Budget:", ["Murah", "Sedang", "Mahal"])

jenis = st.selectbox(
    "🏝️ Jenis Wisata:",
    ["Air", "Alam", "Edukasi", "Hiburan", "Kuliner"]
)

waktu = st.selectbox(
    "⏰ Waktu Kunjungan:",
    ["Pagi", "Siang", "Malam"]
)

jumlah = st.selectbox(
    "👥 Jumlah Orang:",
    ["Sendiri", "2-5 Orang", "> 5 Orang"]
)

cuaca = st.selectbox(
    "🌦️ Kondisi Cuaca:",
    ["Cerah", "Hujan"]
)

# ====== PROSES ======
if st.button("🚀 Dapatkan Rekomendasi"):

    hasil = ""
    detail = []

    # RULE 1
    if jenis == "Air" and cuaca == "Cerah" and budget == "Murah":
        hasil = "Pantai atau Air Terjun 🌊"
        detail = [
            "Pantai Parangtritis (Yogyakarta)",
            "Pantai Kuta (Bali)",
            "Air Terjun Tumpak Sewu (Malang)",
            "Umbul Ponggok (Klaten)"
        ]

    # RULE 2
    elif jenis == "Air" and cuaca == "Hujan":
        hasil = "Wisata air indoor 🏊"
        detail = [
            "Waterboom Bali",
            "Trans Snow World (Bekasi)",
            "Kolam Renang Indoor Senayan",
        ]

    # RULE 3
    elif jenis == "Alam" and waktu == "Pagi":
        hasil = "Gunung / Bukit Sunrise ⛰️"
        detail = [
            "Gunung Bromo (Jawa Timur)",
            "Bukit Sikunir (Dieng)",
            "Gunung Prau (Jawa Tengah)",
        ]

    # RULE 4
    elif jenis == "Hiburan" and waktu == "Malam" and jumlah != "Sendiri":
        hasil = "Hiburan malam 🎡"
        detail = [
            "Malioboro Night Street (Jogja)",
            "Pasar Malam Sekaten",
            "Dufan Ancol (Jakarta)",
        ]

    # RULE 5
    elif jenis == "Edukasi" and jumlah == "Sendiri":
        hasil = "Wisata edukasi 📚"
        detail = [
            "Museum Nasional Indonesia",
            "Museum Angkut (Malang)",
            "Perpustakaan Nasional",
        ]

    # RULE 6
    elif jenis == "Kuliner":
        hasil = "Wisata kuliner 🍜"
        detail = [
            "Malioboro (Jogja)",
            "Cibadak Culinary Night (Bandung)",
            "Pecenongan (Jakarta)",
        ]

    # ELSE
    else:
        hasil = "Wisata santai 🌳"
        detail = [
            "Taman Kota",
            "Alun-alun kota",
            "Hutan kota"
        ]

    # ===== OUTPUT CARD =====
    st.markdown(f"""
    <div class="result-box">
        <h3>🎯 Rekomendasi Untuk Anda</h3>
        <p><b>{hasil}</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📍 Contoh Tempat Wisata:")
    for tempat in detail:
        st.write("✅", tempat)

    st.markdown("### 💡 Tips")
    st.write("Pilih wisata sesuai cuaca dan jumlah orang agar pengalaman lebih maksimal!")
