import streamlit as st
from rlc_utils import hitung_rangkaian

st.set_page_config(page_title="RLC Circuit Analyzer", page_icon="🔌", layout="centered")

    st.markdown("---")
    st.markdown("""
    <h3 style='color:#BB86FC;'>⚙️ Hasil Perhitungan:</h3>
    """, unsafe_allow_html=True)

    def format_hasil(label, value, satuan=""):
        return f"<span style='color:#80D8FF;'><b>{label}</b> = {value} {satuan}</span>"

    st.markdown(format_hasil("ω (omega)", f"{hasil['omega']:.2f}", "rad/s"), unsafe_allow_html=True)
    st.markdown(format_hasil("X_L", f"{hasil['X_L']:.2f}", "Ω"), unsafe_allow_html=True)
    st.markdown(format_hasil("X_C", f"{hasil['X_C']:.2f}", "Ω"), unsafe_allow_html=True)
    st.markdown(format_hasil("Z (Impedansi)", f"{hasil['Z']:.2f}", "Ω"), unsafe_allow_html=True)
    st.markdown(format_hasil("I (Arus)", f"{hasil['I']:.2f}", "A"), unsafe_allow_html=True)
    st.markdown(format_hasil("cos(φ)", f"{hasil['cos_phi']:.4f}"), unsafe_allow_html=True)
    st.markdown(format_hasil("φ", f"{hasil['phi_deg']:.2f}", "°"), unsafe_allow_html=True)
    st.markdown(format_hasil("P (Daya Aktif)", f"{hasil['P']:.2f}", "W"), unsafe_allow_html=True)
    st.markdown(format_hasil("Q (Daya Reaktif)", f"{hasil['Q']:.2f}", "VAR"), unsafe_allow_html=True)
    st.markdown(format_hasil("S (Daya Semu)", f"{hasil['S']:.2f}", "VA"), unsafe_allow_html=True)

    st.markdown(
        f"<div style='background-color:#2A003F; padding:10px; border-radius:10px;'><h4 style='color:#FF69B4;'>Sifat Fasa: {hasil['sifat']}</h4></div>",
        unsafe_allow_html=True
    )

else:
    st.info("Masukkan nilai dan tekan tombol **Hitung**.")

