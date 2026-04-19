import streamlit as st

st.set_page_config(page_title="Sistem Rekomendasi Router", layout="centered")

st.title("📡 Sistem Rekomendasi Router")
st.write("Sistem Cerdas berbasis Rule (IF-THEN)")

# ====== INPUT (FAKTA) ======
budget = st.selectbox("💰 Budget:", ["< 500 ribu", "500 ribu - 1 juta", "> 1 juta"])

kebutuhan = st.selectbox(
    "🎯 Kebutuhan:",
    ["Rumah biasa", "Gaming/Streaming", "Kantor"]
)

luas = st.selectbox(
    "🏠 Luas Rumah:",
    ["Kecil", "Sedang", "Besar"]
)

device = st.selectbox(
    "📱 Jumlah Device:",
    ["1-5", "6-10", ">10"]
)

kecepatan = st.selectbox(
    "⚡ Kecepatan Internet:",
    ["< 20 Mbps", "20-100 Mbps", "> 100 Mbps"]
)

# ====== PROSES ======
if st.button("🚀 Dapatkan Rekomendasi"):

    hasil = ""
    detail = ""

    # RULE 1
    if budget == "< 500 ribu" and kebutuhan == "Rumah biasa":
        hasil = "TP-Link TL-WR840N"
        detail = "Cocok untuk penggunaan ringan seperti browsing dan YouTube"

    # RULE 2
    elif kebutuhan == "Gaming/Streaming" and kecepatan == "> 100 Mbps":
        hasil = "TP-Link Archer AX55 / ASUS RT-AX55"
        detail = "Router WiFi 6, stabil untuk gaming dan streaming"

    # RULE 3
    elif luas == "Besar" and device == ">10":
        hasil = "TP-Link Deco X20 (Mesh WiFi)"
        detail = "Cocok untuk rumah besar dan banyak perangkat"

    # RULE 4
    elif kebutuhan == "Kantor" and device == "6-10":
        hasil = "Huawei AX3 Pro"
        detail = "Stabil untuk banyak user dalam kantor kecil"

    # RULE 5
    elif budget == "500 ribu - 1 juta" and kebutuhan == "Rumah biasa":
        hasil = "Xiaomi Mi Router 4A Gigabit"
        detail = "Harga terjangkau dengan performa stabil"

    # RULE 6 (tambahan biar kuat)
    elif kecepatan == "> 100 Mbps":
        hasil = "ASUS RT-AX56U"
        detail = "Performa tinggi untuk internet cepat"

    # ELSE
    else:
        hasil = "Tenda AC6"
        detail = "Pilihan umum untuk kebutuhan standar"

    # ===== OUTPUT =====
    st.success(f"🎯 Rekomendasi: {hasil}")
    st.info(detail)
