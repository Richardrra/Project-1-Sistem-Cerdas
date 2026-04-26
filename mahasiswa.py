import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Penilaian Mahasiswa", layout="centered")

st.title("🎓 Sistem Penilaian Mahasiswa")

# ===== DATABASE =====
conn = sqlite3.connect("mahasiswa.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS mahasiswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT,
    nim TEXT,
    jurusan TEXT,
    nilai INTEGER,
    grade TEXT,
    keterangan TEXT
)
""")
conn.commit()

# ===== RULE BASED =====
def hitung_nilai(nilai):
    if nilai >= 85:
        return "A", "Sangat Baik"
    elif nilai >= 75:
        return "B", "Baik"
    elif nilai >= 65:
        return "C", "Cukup"
    elif nilai >= 50:
        return "D", "Kurang"
    else:
        return "E", "Tidak Lulus"

# ===== DATABASE FUNCTION =====
def get_data():
    return pd.read_sql_query("SELECT * FROM mahasiswa", conn)

def add_data(nama, nim, jurusan, nilai):
    grade, ket = hitung_nilai(nilai)
    c.execute("""
        INSERT INTO mahasiswa (nama, nim, jurusan, nilai, grade, keterangan)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nama, nim, jurusan, nilai, grade, ket))
    conn.commit()

def delete_data(id):
    c.execute("DELETE FROM mahasiswa WHERE id=?", (id,))
    conn.commit()

def update_data(id, nama, nim, jurusan, nilai):
    grade, ket = hitung_nilai(nilai)
    c.execute("""
        UPDATE mahasiswa
        SET nama=?, nim=?, jurusan=?, nilai=?, grade=?, keterangan=?
        WHERE id=?
    """, (nama, nim, jurusan, nilai, grade, ket, id))
    conn.commit()

# ===== LOGIN STATE =====
if "login" not in st.session_state:
    st.session_state.login = False

if "show_login" not in st.session_state:
    st.session_state.show_login = False

# ===== SIDEBAR =====
st.sidebar.title("⚙️ Menu")

if not st.session_state.login:
    if st.sidebar.button("🔐 Login Admin"):
        st.session_state.show_login = True

if st.session_state.show_login and not st.session_state.login:
    st.sidebar.subheader("Login Admin")
    user = st.sidebar.text_input("Username")
    pw = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Masuk"):
        if user == "admin" and pw == "12345":
            st.session_state.login = True
            st.session_state.show_login = False
            st.sidebar.success("Login berhasil")
            st.rerun()
        else:
            st.sidebar.error("Login gagal")

if st.session_state.login:
    st.sidebar.success("✅ Admin aktif")
    if st.sidebar.button("Logout"):
        st.session_state.login = False
        st.rerun()

# ===== TAB =====
tab1, tab2 = st.tabs(["➕ Input Data", "📊 Data Mahasiswa"])

# ===== TAB 1 INPUT =====
with tab1:
    st.subheader("➕ Input Data Mahasiswa")

    with st.form("form_input"):
        nama = st.text_input("Nama")
        nim = st.text_input("NIM")
        jurusan = st.selectbox("Jurusan", ["Informatika", "Sistem Informasi", "Manajemen", "Akuntansi"])
        nilai = st.number_input("Nilai", 0, 100)

        submit = st.form_submit_button("Simpan")

        if submit:
            if nama and nim:
                add_data(nama, nim, jurusan, nilai)
                st.success("Data berhasil disimpan")
                st.rerun()
            else:
                st.warning("Nama & NIM wajib diisi")

# ===== TAB 2 DATA =====
with tab2:
    st.subheader("📊 Data Mahasiswa")

    data = get_data()

    if not data.empty:
        for i, row in data.iterrows():
            col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([2,2,2,1,1,2,1,1])

            col1.write(row["nama"])
            col2.write(row["nim"])
            col3.write(row["jurusan"])
            col4.write(row["nilai"])
            col5.write(row["grade"])
            col6.write(row["keterangan"])

            if st.session_state.login:
                if col7.button("✏️", key=f"edit_{row['id']}"):
                    st.session_state.edit_id = row["id"]

                if col8.button("🗑️", key=f"hapus_{row['id']}"):
                    delete_data(row["id"])
                    st.success("Data dihapus")
                    st.rerun()

    # ===== EDIT =====
    if st.session_state.login and "edit_id" in st.session_state:
        st.subheader("✏️ Edit Data")

        edit_id = st.session_state.edit_id
        data_edit = data[data["id"] == edit_id].iloc[0]

        nama = st.text_input("Nama", data_edit["nama"])
        nim = st.text_input("NIM", data_edit["nim"])

        jurusan_list = ["Informatika", "Sistem Informasi", "Manajemen", "Akuntansi"]
        jurusan = st.selectbox("Jurusan", jurusan_list, index=jurusan_list.index(data_edit["jurusan"]))
        nilai = st.number_input("Nilai", 0, 100, int(data_edit["nilai"]))

        col1, col2 = st.columns(2)

        if col1.button("Update"):
            update_data(edit_id, nama, nim, jurusan, nilai)
            st.success("Data berhasil diupdate")
            del st.session_state.edit_id
            st.rerun()

        if col2.button("Batal"):
            del st.session_state.edit_id
            st.rerun()

# ===== INFO =====
if not st.session_state.login:
    st.info("🔒 Login admin untuk edit & hapus data")
    