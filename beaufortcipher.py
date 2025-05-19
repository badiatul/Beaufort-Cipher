import streamlit as st

def beaufort_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            p = ord(char) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')
            c = (k - p + 26) % 26
            ciphertext += chr(c + ord('A'))
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def beaufort_decrypt(ciphertext, key):
    return beaufort_encrypt(ciphertext, key)

# Streamlit UI
st.title("🔐 Beaufort Cipher - Enkripsi & Dekripsi")

menu = st.radio("Pilih mode:", ("Enkripsi", "Dekripsi"))

input_text = st.text_area("Masukkan Teks", "")
key = st.text_input("Masukkan Kunci (key)", "")

if st.button("Proses"):
    if not input_text or not key:
        st.warning("Teks dan kunci tidak boleh kosong!")
    else:
        if menu == "Enkripsi":
            result = beaufort_encrypt(input_text, key)
            st.success("Hasil Enkripsi:")
        else:
            result = beaufort_decrypt(input_text, key)
            st.success("Hasil Dekripsi:")

        st.code(result, language='text')

