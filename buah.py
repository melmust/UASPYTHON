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

