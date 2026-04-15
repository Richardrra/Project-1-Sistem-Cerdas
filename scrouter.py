import streamlit as st

st.set_page_config(page_title="Sistem Rekomendasi Router", layout="centered")

st.title("📡 Sistem Rekomendasi Router Sederhana")
st.write("Sistem Cerdas berbasis Rule (IF-ELSE)")


budget = st.selectbox(
    "Pilih Budget Anda:",
    ["< 500 ribu", "500 ribu - 1 juta", "> 1 juta"]
)

kebutuhan = st.selectbox(
    "Pilih Kebutuhan:",
    ["Rumah kecil", "Streaming/Gaming", "Kantor / Banyak device"]
)

if st.button("Dapatkan Rekomendasi"):
    

    if budget == "< 500 ribu":
        if kebutuhan == "Rumah kecil":
            st.success("Rekomendasi: TP-Link TL-WR840N (murah, cukup untuk rumah kecil)")
        elif kebutuhan == "Streaming/Gaming":
            st.success("Rekomendasi: Tenda AC6 (sudah dual band, lebih stabil)")
        elif kebutuhan == "Kantor / Banyak device":
            st.warning("Budget kurang, disarankan tambah budget untuk performa lebih baik")

    elif budget == "500 ribu - 1 juta":
        if kebutuhan == "Rumah kecil":
            st.success("Rekomendasi: Xiaomi Mi Router 4A Gigabit Edition")
        elif kebutuhan == "Streaming/Gaming":
            st.success("Rekomendasi: TP-Link Archer C6 (dual band, stabil untuk gaming)")
        elif kebutuhan == "Kantor / Banyak device":
            st.success("Rekomendasi: Huawei AX3 (WiFi 6, banyak device lebih lancar)")

    elif budget == "> 1 juta":
        if kebutuhan == "Rumah kecil":
            st.success("Rekomendasi: ASUS RT-AX55 (future proof, WiFi 6)")
        elif kebutuhan == "Streaming/Gaming":
            st.success("Rekomendasi: ASUS RT-AX56U / TP-Link Archer AX73 (gaming + stabil)")
        elif kebutuhan == "Kantor / Banyak device":
            st.success("Rekomendasi: Mesh WiFi (TP-Link Deco X20 / Huawei Mesh)")
