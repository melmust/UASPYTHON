import streamlit as st

st.title("Galeri Buah")

buah = st.selectbox("Pilih buah", ["Apel", "Jeruk", "Pisang"])

if buah == "Apel":
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg", width=200)
elif buah == "Jeruk":
    st.image("https://upload.wikimedia.org/wikipedia/commons/c/c4/Orange-Fruit-Pieces.jpg", width=200)
elif buah == "Pisang":
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg", width=200)



import streamlit as st

st.title("Hitung Luas Persegi Panjang")

panjang = st.number_input("Masukkan panjang (cm):")
lebar = st.number_input("Masukkan lebar (cm):")

luas = panjang * lebar
st.write("Luasnya adalah", luas, "cm²")


import streamlit as st

st.title("Tebak Hewan")

soal = st.selectbox("Petunjuk:", ["Bersuara 'meong'", "Hidup di air", "Bertelur dan bisa terbang"])

if soal == "Bersuara 'meong'":
    st.success("Jawaban: Kucing")
elif soal == "Hidup di air":
    st.success("Jawaban: Ikan")
elif soal == "Bertelur dan bisa terbang":
    st.success("Jawaban: Burung")


import streamlit as st

st.title("🐾 Tebak Hewan Berdasarkan Ciri")

st.write("Pilih hewan berdasarkan ciri berikut:")

# Ciri-ciri hewan
ciri = "Hewan ini bersuara 'meong' dan suka bermain di rumah."

# Pilihan jawaban
opsi = ["Anjing", "Kucing", "Ayam", "Gajah"]
pilihan = st.radio(ciri, opsi)

# Tombol cek jawaban
if st.button("Cek Jawaban"):
    if pilihan == "Kucing":
        st.success("Benar! Ini adalah kucing. 🐱")
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg", width=300)
    elif pilihan == "Anjing":
        st.error("Salah. Ini adalah anjing 🐶.")
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg", width=300)
    elif pilihan == "Ayam":
        st.error("Salah. Ini adalah ayam 🐔.")
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/5b/Hen_5.jpg", width=300)
    elif pilihan == "Gajah":
        st.error("Salah. Ini adalah gajah 🐘.")
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/63/African_elephant_warning_raised_trunk.jpg", width=300)





