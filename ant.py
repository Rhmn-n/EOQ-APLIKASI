import streamlit as st
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="EOQ - Persediaan Beras", layout="centered")
st.title("🌾 Aplikasi EOQ - Produksi dan Persediaan Beras")

st.markdown("""
Aplikasi ini digunakan untuk menghitung **Jumlah Pembelian Ekonomis (EOQ)** dalam sistem persediaan gabah/beras, dengan mempertimbangkan:
- Permintaan tahunan beras
- Biaya pemesanan gabah dari petani
- Biaya penyimpanan per karung di gudang
""")

# Input Data
st.header("📥 Input Data Produksi Beras")
D = st.number_input("Permintaan tahunan beras (karung)", value=5000.0, step=100.0, min_value=1.0)
S = st.number_input("Biaya pemesanan gabah (Rp/pemesanan)", value=500000.0, step=50000.0, min_value=1.0)
H = st.number_input("Biaya penyimpanan per karung/tahun (Rp)", value=200000.0, step=10000.0, min_value=1.0)

# Perhitungan EOQ dan Biaya
if D > 0 and S > 0 and H > 0:
    EOQ = np.sqrt((2 * D * S) / H)
    jumlah_pemesanan = D / EOQ
    total_biaya = (D / EOQ) * S + (EOQ / 2) * H

    st.header("📊 Hasil Perhitungan EOQ Beras")
    st.metric("Jumlah Optimal Pembelian Gabah (EOQ)", f"{EOQ:.2f} karung")
    st.metric("Frekuensi Pemesanan/Tahun", f"{jumlah_pemesanan:.2f} kali")
    st.metric("Total Biaya Persediaan", f"Rp {total_biaya:,.2f}")

    # Rumus Penyelesaian
    st.header("📘 Rumus EOQ & TC")

    st.latex(r'''
    EOQ = \sqrt{ \frac{2 \times D \times S}{H} }
    ''')

    st.markdown(f"""
    Substitusi nilai:
    """)

    st.latex(r'''
    EOQ = \sqrt{ \frac{2 \times 5000 \times 500{,}000}{200{,}000} } = \sqrt{25{,}000} = 158.11\ \text{karung}
    ''')

    st.latex(r'''
    TC = \left( \frac{D}{EOQ} \right) \cdot S + \left( \frac{EOQ}{2} \right) \cdot H
    ''')

    st.markdown("Substitusi nilai:")

    st.latex(r'''
    TC = \left( \frac{5000}{158.11} \right) \cdot 500{,}000 + \left( \frac{158.11}{2} \right) \cdot 200{,}000
    = Rp\,31{,}622{,}776.60
    ''')

    st.success("✅ Perhitungan EOQ dan total biaya berhasil ditampilkan dengan format rapi dan benar.")

else:
    st.warning("Silakan isi semua data input dengan benar untuk menghitung EOQ.")
