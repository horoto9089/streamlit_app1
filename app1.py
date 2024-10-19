import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.snow()



st.header("卒論リポジトリ")
st.subheader("専修大学4年 山原大翔")

if st.button('Click Me'):
     st.write('こんにちは')

with st.expander("st.expanderとは"):
    st.write("このようにして、ユーザーがクリックすると、追加の情報を表示できるようになります。")

    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.plot(x, y)
    st.pyplot(plt)