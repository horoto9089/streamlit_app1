import streamlit as st
import pandas as pd
import numpy as np

st.snow()



st.header("卒論リポジトリ")
st.subheader("Hiroto Yamahara")

if st.button('Click Me'):
     st.write('こんにちは')

with st.expander("st.expanderとは"):
    st.write("このようにして、ユーザーがクリックすると、追加の情報を表示できるようになります。")