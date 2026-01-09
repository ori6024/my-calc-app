import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. ページの設定（スマホの横幅いっぱいに使う）
st.set_page_config(page_title="計算アプリ", layout="wide")

st.title('シミュレーション・グラフアプリ')

# 2. サイドバーの設定
st.sidebar.header("パラメータ設定")
frequency = st.sidebar.slider('周波数', 1.0, 10.0, 5.0)
# 振幅を -2.0 〜 2.0 に固定
amplitude = st.sidebar.slider('振幅', -2.0, 2.0, 1.0)

# 3. 計算ロジック
x = np.linspace(0, 10, 500)
y = amplitude * np.sin(frequency * x)

# 4. グラフの描画
# figsizeでスマホで見やすい比率に調整
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, color='#1f77b4', linewidth=2)

# 縦軸を固定（これがポイント！振幅の変化がはっきりわかります）
ax.set_ylim(-2.5, 2.5) 

# デザインの調整
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.grid(True, linestyle='--', alpha=0.7)
ax.axhline(0, color='black', linewidth=1) # 0の線を見やすく

# 5. 画面への表示
# use_container_width=True でスマホ画面からはみ出さないように自動調整
st.pyplot(fig, use_container_width=True)

# 補足説明
st.write("---")
st.caption("左側のスライダーを動かすと、リアルタイムで計算結果が反映されます。")
