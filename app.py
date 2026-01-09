import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('シミュレーション・グラフアプリ')

# サイドバーで数値を調整できるようにします
frequency = st.sidebar.slider('周波数', 1.0, 10.0, 5.0)
amplitude = st.sidebar.slider('振幅', 0.1, 2.0, 1.0)

# 計算
x = np.linspace(0, 10, 500)
y = amplitude * np.sin(frequency * x)

# グラフの描画
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.grid(True)

# 表示
st.pyplot(fig)
