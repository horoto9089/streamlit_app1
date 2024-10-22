import streamlit as st
import pandas as pd
import numpy as np
import plotly
#import japanize-matplotlib

st.set_page_config(layout="wide")

st.snow()

st.sidebar.markdown('''
# MENU
- [purpose and significance](#研究目的・意義)
- [model](#モデル)
- [data](#データ)
- [result](#結果・考察)
- [conclusion](#結論)
''', unsafe_allow_html=True)


st.title("Repository of Graduation Thesis")







st.header("研究目的・意義")
st.markdown("---")
st.text("自動販売機は公共財（災害時物資提供媒体、地域情報、AEDなど）の供給面でも地域への大切な役割がある。")

st.text("しかしながら、自動販売機台数は減少傾向にある。")

st.text("よって、自動販売機普及への取り組み・分布傾向の分析が必要である。")

with st.expander("English.ver"):
    st.write("Vendingmachines have an important role to play in the community in terms of supplying public goods (medium for providing supplies during disasters, local information, AED, etc.). However, the number of vendingmachines is on the decline. Therefore, efforts to promote the use of vending machines are needed.")








st.header("モデル")
st.markdown("---")


with st.expander("English.ver"):
    st.write("このようにして、ユーザーがクリックすると、追加の情報を表示できるようになります。")










st.header("データ")
st.markdown("---")



with st.expander("English.ver"):
    st.write("このようにして、ユーザーがクリックすると、追加の情報を表示できるようになります。")










st.header("結果・考察")
st.markdown("---")




with st.expander("English.ver"):
    st.write("このようにして、ユーザーがクリックすると、追加の情報を表示できるようになります。")









st.header("結論")
st.markdown("---")




with st.expander("English.ver"):
    st.write("このようにして、ユーザーがクリックすると、追加の情報を表示できるようになります。")

