import streamlit as st
import pandas as pd
from datetime import datetime


# Fungsi Beaufort Cipher
def beaufort_cipher(text, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = text.upper()
    key = key.upper()
    result = ''

    key_repeated = ''
    while len(key_repeated) < len(text):
        key_repeated += key
    key_repeated = key_repeated[:len(text)]

    for t_char, k_char in zip(text, key_repeated):
        if t_char in alphabet:
            t_index = alphabet.index(t_char)
            k_index = alphabet.index(k_char)
            c_index = (k_index - t_index) % 26
            result += alphabet[c_index]
        else:
            result += t_char
    return result


# Inisialisasi session_state untuk database lokal
if 'db' not in st.session_state:
    st.session_state.db = []

# UI Streamlit
st.set_page_config(page_title="Beaufort Cipher App", layout="centered")

st.title("🔐 Aplikasi Keamanan Data - Beaufort Cipher")

mode = st.radio("Pilih Mode:", ["Enkripsi", "Dekripsi"])
text = st.text_area("Masukkan Teks:", "")
key = st.text_input("Masukkan Kunci:", "")

if st.button("Proses"):
    if not text or not key:
        st.warning("Teks dan kunci tidak boleh kosong.")
    else:
        result = beaufort_cipher(text, key)
        st.success(f"Hasil {mode}:\n{result}")

        # Simpan ke 'database'
        st.session_state.db.append({
            "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Mode": mode,
            "Teks Awal": text,
            "Kunci": key,
            "Hasil": result
        })

# Tampilkan tabel
if st.session_state.db:
    st.markdown("### 📋 Riwayat Enkripsi/Dekripsi")
    df = pd.DataFrame(st.session_state.db)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Belum ada data yang diproses.")
import streamlit as st
import pandas as pd
from datetime import datetime


# Fungsi Beaufort Cipher
def beaufort_cipher(text, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = text.upper()
    key = key.upper()
    result = ''

    key_repeated = ''
    while len(key_repeated) < len(text):
        key_repeated += key
    key_repeated = key_repeated[:len(text)]

    for t_char, k_char in zip(text, key_repeated):
        if t_char in alphabet:
            t_index = alphabet.index(t_char)
            k_index = alphabet.index(k_char)
            c_index = (k_index - t_index) % 26
            result += alphabet[c_index]
        else:
            result += t_char
    return result


# Inisialisasi session_state untuk database lokal
if 'db' not in st.session_state:
    st.session_state.db = []

# UI Streamlit
st.set_page_config(page_title="Beaufort Cipher App", layout="centered")

st.title("🔐 Aplikasi Keamanan Data - Beaufort Cipher")

mode = st.radio("Pilih Mode:", ["Enkripsi", "Dekripsi"])
text = st.text_area("Masukkan Teks:", "")
key = st.text_input("Masukkan Kunci:", "")

if st.button("Proses"):
    if not text or not key:
        st.warning("Teks dan kunci tidak boleh kosong.")
    else:
        result = beaufort_cipher(text, key)
        st.success(f"Hasil {mode}:\n{result}")

        # Simpan ke 'database'
        st.session_state.db.append({
            "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Mode": mode,
            "Teks Awal": text,
            "Kunci": key,
            "Hasil": result
        })

# Tampilkan tabel
if st.session_state.db:
    st.markdown("### 📋 Riwayat Enkripsi/Dekripsi")
    df = pd.DataFrame(st.session_state.db)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Belum ada data yang diproses.")
