import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Perhitungan EOQ", layout="centered")
st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")

# ---------------------------------------
# Penjelasan EOQ
# ---------------------------------------
with st.expander("📘 Penjelasan EOQ (Economic Order Quantity)"):
    st.markdown("""
    **Economic Order Quantity (EOQ)** adalah model perhitungan jumlah pemesanan optimal yang meminimalkan total biaya persediaan.

    Rumus EOQ:

    $$
    EOQ = \\sqrt{\\frac{2DS}{H}}
    $$

    Dimana:
    - **D** = Permintaan tahunan (unit/tahun)
    - **S** = Biaya pemesanan per pesanan (Rp)
    - **H** = Biaya penyimpanan per unit per tahun (Rp)

    Total Biaya Persediaan:

    $$
    TC = \\left( \\frac{D}{Q} \\right) S + \\left( \\frac{Q}{2} \\right) H
    $$

    Dimana:
    - **Q** = Kuantitas pemesanan
    - **TC** = Total biaya tahunan
    """)

# ---------------------------------------
# Input Data
# ---------------------------------------
st.header("📥 Input Data")
col1, col2 = st.columns(2)
with col1:
    D = st.number_input("Permintaan Tahunan (unit)", min_value=1, value=1200)
    S = st.number_input("Biaya Pemesanan per Pesanan (Rp)", min_value=1, value=150000)
with col2:
    H = st.number_input("Biaya Penyimpanan per Unit per Tahun (Rp)", min_value=1, value=2500)

# ---------------------------------------
# Perhitungan EOQ
# ---------------------------------------
EOQ = np.sqrt((2 * D * S) / H)
total_order = D / EOQ
total_cost = (D / EOQ) * S + (EOQ / 2) * H

# ---------------------------------------
# Output Hasil
# ---------------------------------------
st.header("📤 Hasil Perhitungan EOQ")
st.success(f"📌 **EOQ (Jumlah Pemesanan Optimal): {EOQ:.2f} unit**")
st.write(f"📦 **Jumlah Pemesanan per Tahun:** {total_order:.2f} kali")
st.write(f"💰 **Total Biaya Persediaan:** Rp {total_cost:,.2f}")

# ---------------------------------------
# Diagram Kolom (Bar Chart) Lebih Mudah Dipahami
# ---------------------------------------
st.header("📊 Diagram Kolom Biaya EOQ")

# Hitung komponen biaya di titik EOQ
ordering_cost = (D / EOQ) * S
holding_cost = (EOQ / 2) * H
total_cost = ordering_cost + holding_cost

# Data untuk bar chart
labels = ['Biaya Pemesanan', 'Biaya Penyimpanan', 'Total Biaya']
values = [ordering_cost, holding_cost, total_cost]
colors = ['green', 'orange', 'blue']

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(labels, values, color=colors)

# Tambahkan label nilai pada atas batang
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + total_cost*0.02, f"Rp {yval:,.0f}", ha='center', va='bottom', fontsize=10)

ax.set_title("Perbandingan Komponen Biaya pada EOQ")
ax.set_ylabel("Biaya (Rp)")
st.pyplot(fig)
