import streamlit as st
import backend as bd

with open ("style.css") as f :
    st.markdown( f'<style>{f.read()}</style>',unsafe_allow_html=True)
st.header("Encrypter")
txt=st.text_area("Input")
col1,col2=st.columns(2)

if col1.button("encode"):
        st.code(bd.encode(txt))

if col2.button("decode"):
    try:
        st.code(bd.decode(txt[2:][:-1]))
    except:
        st.warning("Invalid text fromat entered")
        st.info("[How to use](https://github.com/MinulSandith/Text-encrypter/blob/main/README.md)")




