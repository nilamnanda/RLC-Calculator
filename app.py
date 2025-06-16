if st.button("Hitung"):
    hasil = hitung_rangkaian(R, L, C)

    # Tampilkan hasil perhitungan
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

    # ===== Grafik Segitiga Daya =====
    st.markdown("## 📈 Segitiga Daya")

    P = hasil['P']
    Q = hasil['Q']
    S = hasil['S']

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.arrow(0, 0, P, 0, head_width=10, head_length=5, fc='blue', ec='blue')
    ax.arrow(P, 0, 0, Q, head_width=10, head_length=5, fc='green', ec='green')
    ax.arrow(0, 0, P, Q, head_width=10, head_length=5, fc='orange', ec='orange')

    ax.text(P/2, -20, f"P = {P:.2f} W", color='blue', fontsize=10, ha='center')
    ax.text(P + 10, Q/2, f"Q = {Q:.2f} VAR", color='green', fontsize=10)
    ax.text(P/2, Q/2, f"S = {S:.2f} VA", color='orange', fontsize=10, ha='center')

    ax.set_xlim(0, P + 50)
    ax.set_ylim(0, Q + 50)
    ax.set_aspect('equal')
    ax.axis('off')

    st.pyplot(fig)
