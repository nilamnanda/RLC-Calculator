import streamlit as st
from rlc_utils import hitung_rangkaian

st.set_page_config(page_title="RLC Circuit Analyzer", page_icon="🔌", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🔌 RLC Circuit Analyzer</h1>
    <p style='text-align: center;'>Masukkan nilai R, L, dan C untuk menganalisis rangkaian listrik RLC seri</p>
""", unsafe_allow_html=True)

st.sidebar.header("Input Nilai Komponen")

R = st.sidebar.number_input("Resistor (R) dalam Ohm", value=4.0)
L = st.sidebar.number_input("Induktor (L) dalam Henry", value=0.2)
C = st.sidebar.number_input("Kapasitor (C) dalam Farad", value=0.0001)

if st.sidebar.button("Hitung"):
    hasil = hitung_rangkaian(R, L, C)

    st.success("✅ Perhitungan Berhasil")

    st.markdown("---")
    st.markdown("### ⚙️ Hasil Perhitungan:")

    st.write(f"**ω (omega)** = `{hasil['omega']:.2f}` rad/s")
    st.write(f"**X_L** = `{hasil['X_L']:.2f}` Ω")
    st.write(f"**X_C** = `{hasil['X_C']:.2f}` Ω")
    st.write(f"**Z (Impedansi)** = `{hasil['Z']:.2f}` Ω")
    st.write(f"**I (Arus)** = `{hasil['I']:.2f}` A")
    st.write(f"**cos(φ)** = `{hasil['cos_phi']:.4f}`")
    st.write(f"**φ** = `{hasil['phi_deg']:.2f}`°")
    st.write(f"**P (Daya Aktif)** = `{hasil['P']:.2f}` W")
    st.write(f"**Q (Daya Reaktif)** = `{hasil['Q']:.2f}` VAR")
    st.write(f"**S (Daya Semu)** = `{hasil['S']:.2f}` VA")
    
    warna = "green" if "Netral" in hasil["sifat"] else ("orange" if "Leading" in hasil["sifat"] else "red")
    st.markdown(f"<h4 style='color:{warna};'>Sifat Fasa: {hasil['sifat']}</h4>", unsafe_allow_html=True)

else:
    st.info("Masukkan nilai dan tekan tombol **Hitung**.")

