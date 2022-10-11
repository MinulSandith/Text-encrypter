import streamlit as st
import backend as bd
st.header("Encrypter")
txt=st.text_area("Input")
col1,col2=st.columns(2)
if col1.button("encode"):
    st.code(bd.encode(txt))
if col2.button("decode"):
    st.code(bd.decode(txt[2:][:-1]))




