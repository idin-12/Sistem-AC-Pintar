import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from scipy.optimize import linprog
from pulp import LpProblem, LpVariable, LpMaximize, value

# ============================
# 🎨 Konfigurasi halaman
st.set_page_config(page_title="🌡️ Sistem AC Pintar Rumah John", page_icon="❄️", layout="centered")

# ============================
# 🌟 Judul dan Deskripsi
st.title("❄️ Sistem AC Pintar Rumah John")
st.markdown("""
### 💡 Studi Kasus
Rumah pintar milik John memiliki sistem AC otomatis.  
AC akan **MENYALA** jika:
- 🔥 Suhu panas
- 🪟 Jendela tertutup
- 🏠 Ada orang di rumah
""")

# ============================
# 🔧 Input Status Sensor (Sidebar)
st.sidebar.header("🔧 Input Status Sensor")
is_hot = st.sidebar.checkbox("🔥 Suhu Panas?", value=False)
window_closed = st.sidebar.checkbox("🪟 Jendela Tertutup?", value=False)
someone_home = st.sidebar.checkbox("🏠 Ada Orang di Rumah?", value=False)

# ============================
# ⚡ Logika AC
st.subheader("⚡ Status AC")
if is_hot and window_closed and someone_home:
    st.success("✅ AC MENYALA")
    ac_status = 1
else:
    st.warning("❌ AC MATI")
    ac_status = 0

# ============================
# 📊 Visualisasi Kondisi Sensor (Plotly)
st.subheader("📊 Visualisasi Sensor dan Status AC")
labels = ['Suhu Panas', 'Jendela Tertutup', 'Ada Orang di Rumah', 'Status AC']
values = [int(is_hot), int(window_closed), int(someone_home), ac_status]
colors = ['#4CAF50' if v==1 else '#F44336' for v in values]

fig = go.Figure(data=[go.Bar(
    x=labels,
    y=values,
    marker_color=colors,
    text=['Ya' if v==1 else 'Tidak' for v in values],
    textposition='auto'
)])
fig.update_layout(title="Status Sensor dan AC", yaxis=dict(range=[0,1.2]))
st.plotly_chart(fig)

# ============================
# 🔢 NumPy Array Status
np_array = np.array(values)
st.write("🔢 **Array Status (NumPy):**", np_array)

# ============================
# 🧠 Contoh Sympy
st.subheader("🧠 Contoh Pemanggilan Sympy")
x = sp.Symbol('x')
eq = sp.Eq(2*x + 5, 15)
solution = sp.solve(eq, x)
st.write(f"Persamaan: {eq}, Solusi x = {solution[0]}")

# ============================
# 📈 Pie Chart dengan Matplotlib
st.subheader("📈 Pie Chart Status Sensor (Matplotlib)")
fig2, ax = plt.subplots()
ax.pie(values[:-1], labels=labels[:-1], autopct='%1.0f%%', colors=colors[:-1])
ax.set_title("Proporsi Kondisi Sensor")
st.pyplot(fig2)

# ============================
# 🔬 Contoh Linear Programming dengan Scipy
st.subheader("🔬 Contoh Linear Programming (scipy.linprog)")
c = [-1, -2]
A = [[2, 1], [1, 2]]
b = [20, 16]
res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)])
if res.success:
    st.write(f"Scipy linprog solution (max profit): {-res.fun:.2f}")
else:
    st.write("Scipy linprog: Tidak ada solusi")

# ============================
# 📝 Contoh Linear Programming dengan Pulp
st.subheader("📝 Contoh Linear Programming (pulp)")
prob = LpProblem("MaximizeDummy", LpMaximize)
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
prob += 4*x1 + 3*x2
prob += x1 + x2 <= 10
prob.solve()
st.write(f"Pulp solution (max objective): {value(prob.objective):.2f}")

# ============================
# ✨ Footer
st.markdown("""
---
👨‍💻 **Dibuat oleh: [Nama Kamu]**  
Untuk latihan pemrograman sistem kontrol rumah pintar dan integrasi library di `requirements.txt`.
""")
