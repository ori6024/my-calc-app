import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ページの設定を「ワイドモード」にする（スマホで余白を減らす）
st.set_page_config(layout="wide")

st.title('シミュレーション・グラフ')

# スマホだとサイドバーが隠れて気づきにくいので、メイン画面にも説明を入れる
st.write("左上の「＞」ボタンから設定を変更できます")

# サイドバーの設定
frequency = st.sidebar.slider('周波数', 1.0, 10.0, 5.0)
amplitude = st.sidebar.slider('振幅', 0.1, 2.0, 1.0)

# 計算
x = np.linspace(0, 10, 500)
y = amplitude * np.sin(frequency * x)

# グラフのサイズをスマホの横幅に合わせる工夫
fig, ax = plt.subplots(figsize=(8, 4)) # 横長に設定
ax.plot(x, y)
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.grid(True)

# use_container_width=True を追加（画面幅いっぱいに広げる）
st.pyplot(fig, use_container_width=True)
