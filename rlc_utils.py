if st.button("Hitung"):
    hasil = hitung_rangkaian(R, L, C)

    # (bagian menampilkan hasil perhitungan di sini...)

    # ⬇⬇⬇ Tambahkan ini di bagian bawah ⬇⬇⬇
    st.subheader("📈 Segitiga Daya")

    P = hasil["P"]
    Q = hasil["Q"]
    S = hasil["S"]

    fig, ax = plt.subplots()
    ax.arrow(0, 0, P, 0, head_width=5, head_length=5, fc='blue', ec='blue')
    ax.arrow(0, 0, 0, Q, head_width=5, head_length=5, fc='green', ec='green')
    ax.arrow(0, 0, P, Q, head_width=5, head_length=5, fc='orange', ec='orange')

    ax.text(P/2, -10, f"P = {P:.2f} W", color='blue')
    ax.text(-30, Q/2, f"Q = {Q:.2f} VAR", color='green')
    ax.text(P/2, Q/2, f"S = {S:.2f} VA", color='orange')

    ax.set_xlim(0, P + 50)
    ax.set_ylim(0, Q + 50)
    ax.set_xlabel("Daya Aktif (W)")
    ax.set_ylabel("Daya Reaktif (VAR)")
    ax.set_title("Segitiga Daya (P-Q-S)")
    ax.grid(True)

    st.pyplot(fig)
