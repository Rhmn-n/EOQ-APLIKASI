import streamlit as st
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="🌾 EOQ - Persediaan Beras", layout="centered")

# ========================
# CSS CUSTOM UI
# ========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

.title {
    font-size: 2.8em;
    font-weight: 800;
    background: linear-gradient(to right, #00b894, #55efc4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2em;
}

.box {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
    margin-bottom: 25px;
}

.metric-box {
    background-color: #e0f7fa;
    border-radius: 10px;
    padding: 15px;
    text-align: center;
    font-size: 1.1em;
    font-weight: 600;
    color: #00796b;
}
</style>
""", unsafe_allow_html=True)

# ========================
# Judul Aplikasi
# ========================
st.markdown('<div class="title">🌾 Aplikasi EOQ - Produksi & Persediaan Gabah</div>', unsafe_allow_html=True)

st.markdown("Menghitung **Jumlah Pembelian Ekonomis (EOQ)** dengan mempertimbangkan:")
st.markdown("- Permintaan tahunan gabah (D)  \n- Biaya pemesanan (S)  \n- Biaya penyimpanan per karung per tahun (H)")

# ========================
# Penjelasan Variabel
# ========================
with st.expander("📘 Penjelasan Simbol EOQ"):
    st.markdown("""
    - **D** = Permintaan tahunan gabah (karung)  
    - **S** = Biaya pemesanan per transaksi (Rp)  
    - **H** = Biaya penyimpanan per karung per tahun (Rp)  
    - **EOQ (Q)** = Jumlah optimal pemesanan  
    - **TC** = Total Cost = Biaya total tahunan (biaya pesan + simpan)  
    """)

# ========================
# Input Data
# ========================
st.markdown('<div class="box">', unsafe_allow_html=True)
st.subheader("📥 Input Data Produksi Gabah")
col1, col2, col3 = st.columns(3)
with col1:
    D = st.number_input("📦 Permintaan Tahunan [D]", value=5000.0, step=100.0, min_value=1.0)
with col2:
    S = st.number_input("🛒 Biaya Pemesanan (Rp) [S]", value=500000.0, step=50000.0, min_value=1.0)
with col3:
    H = st.number_input("🏬 Biaya Penyimpanan/Tahun (Rp) [H]", value=200000.0, step=10000.0, min_value=1.0)
st.markdown('</div>', unsafe_allow_html=True)

# ========================
# Perhitungan
# ========================
if D > 0 and S > 0 and H > 0:
    EOQ = np.sqrt((2 * D * S) / H)
    jumlah_pesan = D / EOQ
    total_biaya = (D / EOQ) * S + (EOQ / 2) * H

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("📊 Hasil Perhitungan EOQ")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="metric-box">🔢 Jumlah Optimal Pembelian Gabah: <br> {EOQ:.2f} karung</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-box">📆 Frekuensi Pemesanan: <br> {jumlah_pesan:.2f} kali/tahun</div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-box">💰 Total Biaya: <br> Rp {total_biaya:,.2f}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ========================
    # Penjelasan Rumus
    # ========================
    with st.expander("📐 Tampilkan Rumus dan Substitusi"):
        st.latex(r'''
        EOQ = \sqrt{ \frac{2 \times D \times S}{H} }
        ''')

        st.markdown("**Substitusi nilai ke dalam rumus EOQ:**")
        st.latex(r'''
        EOQ = \sqrt{ \frac{2 \times 5000 \times 500{,}000}{200{,}000} } = \sqrt{25{,}000} = 158.11
        ''')

        st.latex(r'''
        TC = \left( \frac{D}{EOQ} \right) \cdot S + \left( \frac{EOQ}{2} \right) \cdot H
        ''')

        st.markdown("**Substitusi nilai ke dalam rumus TC:**")
        st.latex(r'''
        TC = \left( \frac{5000}{158.11} \right) \cdot 500{,}000 + \left( \frac{158.11}{2} \right) \cdot 200{,}000 = Rp\,31{,}622{,}776.60
        ''')

    st.success("✅ Perhitungan EOQ dan biaya total berhasil ditampilkan.")
else:
    st.warning("⚠️ Silakan masukkan semua data input untuk melakukan perhitungan.")
