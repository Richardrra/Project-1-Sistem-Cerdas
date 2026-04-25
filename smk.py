import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sistem Nilai Siswa SMK", layout="centered")

st.title("📚 Sistem Input Nilai Siswa SMK")

# ====== INIT DATA ======
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "Nama", "NIS", "Jurusan", "Kelas", "Nilai"
    ])

if "login" not in st.session_state:
    st.session_state.login = False

# ====== LOGIN ADMIN ======
st.sidebar.title("🔐 Login Admin")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

ADMIN_USER = "admin"
ADMIN_PASS = "12345"

if st.sidebar.button("Login"):
    if username == ADMIN_USER and password == ADMIN_PASS:
        st.session_state.login = True
        st.sidebar.success("Login berhasil")
    else:
        st.sidebar.error("Login gagal")

if st.sidebar.button("Logout"):
    st.session_state.login = False

# ====== INPUT DATA (SEMUA USER) ======
st.subheader("➕ Input Data Siswa")

with st.form("form_input"):
    nama = st.text_input("Nama")
    nis = st.text_input("NIS")
    jurusan = st.selectbox("Jurusan", ["RPL", "TKJ", "AKL", "BDP"])
    kelas = st.selectbox("Kelas", ["X", "XI", "XII"])
    nilai = st.number_input("Nilai", 0, 100)

    submit = st.form_submit_button("Simpan")

    if submit:
        new_data = pd.DataFrame([[nama, nis, jurusan, kelas, nilai]],
                                columns=st.session_state.data.columns)
        st.session_state.data = pd.concat(
            [st.session_state.data, new_data],
            ignore_index=True
        )
        st.success("Data berhasil ditambahkan")

# ====== TAMPIL DATA ======
st.subheader("📊 Data Siswa")

if not st.session_state.data.empty:
    for i, row in st.session_state.data.iterrows():
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2,2,2,1,1,1,1])

        col1.write(row["Nama"])
        col2.write(row["NIS"])
        col3.write(row["Jurusan"])
        col4.write(row["Kelas"])
        col5.write(row["Nilai"])

        # ===== ADMIN ACTION =====
        if st.session_state.login:
            if col6.button("✏️ Edit", key=f"edit_{i}"):
                st.session_state.edit_index = i

            if col7.button("🗑️ Hapus", key=f"hapus_{i}"):
                st.session_state.data = st.session_state.data.drop(i).reset_index(drop=True)
                st.success("Data dihapus")
                st.rerun()

# ====== FORM EDIT ======
if st.session_state.login and "edit_index" in st.session_state:
    st.subheader("✏️ Edit Data")

    idx = st.session_state.edit_index
    data_edit = st.session_state.data.loc[idx]

    nama = st.text_input("Nama", data_edit["Nama"])
    nis = st.text_input("NIS", data_edit["NIS"])
    jurusan = st.selectbox("Jurusan", ["RPL", "TKJ", "AKL", "BDP"], index=["RPL","TKJ","AKL","BDP"].index(data_edit["Jurusan"]))
    kelas = st.selectbox("Kelas", ["X", "XI", "XII"], index=["X","XI","XII"].index(data_edit["Kelas"]))
    nilai = st.number_input("Nilai", 0, 100, int(data_edit["Nilai"]))

    col1, col2 = st.columns(2)

    if col1.button("Update"):
        st.session_state.data.loc[idx] = [nama, nis, jurusan, kelas, nilai]
        st.success("Data berhasil diupdate")
        del st.session_state.edit_index
        st.rerun()

    if col2.button("Batal"):
        del st.session_state.edit_index
        st.rerun()

# ====== INFO ======
if not st.session_state.login:
    st.info("🔒 Login sebagai admin untuk edit & hapus data")