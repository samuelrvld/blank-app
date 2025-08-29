import streamlit as st  


# Inisialisasi Session State

if "page" not in st.session_state:
    st.session_state.page = "home"

# Fungsi kembali ke halaman utama

def go_home():
    st.session_state.page = "home"

# Halaman Utama
if st.session_state.page == "home":
    st.title("📚 Aplikasi Sederhana Streamlit")
    st.write("Aplikasi ini memiliki 3 fitur:")
    st.markdown("""
    1. 🔢 Kalkulator Sederhana  
    2. 🌡️ Konversi Suhu (Celcius, Reamur, Fahrenheit)  
    3. 🌀 Deret Fibonacci  
    """)
    st.write("Silakan pilih fitur di bawah:")

    if st.button("Kalkulator Sederhana"):
        st.session_state.page = "kalkulator"
    if st.button("Konversi Suhu"):
        st.session_state.page = "konversi"
    if st.button("Perhitungan Fibonacci"):
        st.session_state.page = "fibonacci"


# Halaman Kalkulator
elif st.session_state.page == "kalkulator":
    if st.button("⬅️ Kembali"):
        go_home()

    st.header("🔢 Kalkulator Sederhana")
    a = st.number_input("Masukkan angka pertama", value=0.0)
    b = st.number_input("Masukkan angka kedua", value=0.0)
    operator = st.selectbox("Pilih operator:", ["+", "-", "*", "/"])

    if st.button("Hitung"):
        if operator == "+":
            hasil = a + b
        elif operator == "-":
            hasil = a - b
        elif operator == "*":
            hasil = a * b
        elif operator == "/":
            hasil = a / b if b != 0 else "Error: Tidak bisa dibagi 0!"
        else:
            hasil = "Operator tidak valid!"
        
        st.success(f"Hasil: {hasil}")


# Halaman Konversi Suhu
elif st.session_state.page == "konversi":
    if st.button("⬅️ Kembali"):
        go_home()

    st.header("🌡️ Konversi Suhu")
    nilai = st.number_input("Masukkan nilai suhu:", value=0.0)
    satuan_asal = st.selectbox("Pilih satuan asal:", ("Celcius", "Reamur", "Fahrenheit"))

    if satuan_asal == "Celcius":
        celcius = nilai
        reamur = (4/5) * celcius
        fahrenheit = (9/5) * celcius + 32
    elif satuan_asal == "Reamur":
        reamur = nilai
        celcius = (5/4) * reamur
        fahrenheit = (9/4) * reamur + 32
    elif satuan_asal == "Fahrenheit":
        fahrenheit = nilai
        celcius = (5/9) * (fahrenheit - 32)
        reamur = (4/9) * (fahrenheit - 32)

    st.subheader("📊 Hasil Konversi:")
    st.write(f"Celcius: {celcius:.2f} °C")
    st.write(f"Fahrenheit: {fahrenheit:.2f} °F")
    st.write(f"Reamur: {reamur:.2f} °R")


# Halaman Fibonacci
elif st.session_state.page == "fibonacci":
    if st.button("⬅️ Kembali"):
        go_home()

    st.header("🌀 Deret Fibonacci")
    n = st.number_input("Masukkan jumlah suku (n):", min_value=1, step=1)

    def fibonacci(n):
        deret = []
        a, b = 0, 1
        for _ in range(n):
            deret.append(a)
            a, b = b, a + b
        return deret

    if st.button("Generate Deret"):
        hasil = fibonacci(n)
        st.subheader(f"Deret Fibonacci hingga suku ke-{n}:")
        st.info(", ".join(map(str, hasil)))
