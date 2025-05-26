import streamlit as st
import sqlite3
import pandas as pd

# ===== Fungsi Beaufort Cipher =====
def generate_key(text, key):
    key = list(key)
    if len(key) == len(text):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def beaufort_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = generate_key(plaintext, key.upper())
    cipher = ""
    for p, k in zip(plaintext, key):
        c = (ord(k) - ord(p)) % 26
        cipher += chr(c + ord('A'))
    return cipher

def beaufort_decrypt(ciphertext, key):
    # Decryption sama dengan enkripsi di Beaufort Cipher
    return beaufort_encrypt(ciphertext, key)

# ===== Fungsi Database =====
DB_NAME = "beaufort.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS beaufort_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mode TEXT,
            input_text TEXT,
            key TEXT,
            result TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_record(mode, input_text, key, result):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO beaufort_history (mode, input_text, key, result) VALUES (?, ?, ?, ?)",
              (mode, input_text, key, result))
    conn.commit()
    conn.close()

def fetch_records():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT mode, input_text, key, result, timestamp FROM beaufort_history ORDER BY id DESC")
    records = c.fetchall()
    conn.close()
    return records

# ===== Streamlit App =====
def main():
    st.title("🔐 Beaufort Cipher with SQLite")

    init_db()

    mode = st.radio("Pilih Mode", ["Enkripsi", "Dekripsi"])
    input_text = st.text_input("Masukkan teks")
    key = st.text_input("Masukkan kunci")

    if st.button("Proses"):
        if not input_text or not key:
            st.warning("Teks dan kunci tidak boleh kosong!")
        else:
            if mode == "Enkripsi":
                result = beaufort_encrypt(input_text, key)
            else:
                result = beaufort_decrypt(input_text, key)

            insert_record(mode, input_text.upper(), key.upper(), result)

            st.success(f"Hasil {mode}: {result}")
            st.table([{"Input": input_text.upper(), "Key": key.upper(), "Output": result}])

    st.subheader("📜 Riwayat Proses")
    records = fetch_records()
    if records:
        df = pd.DataFrame(records, columns=["Mode", "Input", "Key", "Output", "Timestamp"])
        st.dataframe(df)
    else:
        st.write("Belum ada data tersimpan.")

if __name__ == "__main__":
    main()
