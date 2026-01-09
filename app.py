import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. ページの設定（スマホの横幅いっぱいに使う）
st.set_page_config(page_title="計算アプリ", layout="wide")

st.title('シミュレーション・グラフアプリ')

# 2. パラメータ設定（サイドバー）
st.sidebar.header("パラメータ設定")
frequency = st.sidebar.slider('周波数', 1.0, 10.0, 5.0)

# 【修正ポイント】振幅の幅を 0.0 〜 2.0 に設定
amplitude = st.sidebar.slider('振幅', 0.0, 2.0, 1.0)

# 3. 計算ロジック
x = np.linspace(0, 10, 500)
y = amplitude * np.sin(frequency * x)

# 4. グラフの描画
# figsizeでスマホで見やすい比率に調整
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, color='#1f77b4', linewidth=2)

# 縦軸を固定（0〜2の変化が分かりやすいよう、-2.2 〜 2.2 で固定）
ax.set_ylim(-2.2, 2.2) 

# デザインの調整
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.grid(True, linestyle='--', alpha=0.7)
ax.axhline(0, color='black', linewidth=1) # 0の基準線

# 5. 画面への表示
# use_container_width=True でスマホ画面にフィットさせる
st.pyplot(fig, use_container_width=True)

# 補足情報
st.write(f"現在の設定：周波数 **{frequency}** / 振幅 **{amplitude}**")
st.write("---")
st.caption("スライダーを0にすると、波が消えて平らになるのが確認できます。")
