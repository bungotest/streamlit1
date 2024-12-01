import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('レイアウト -サイドバー、カラム')

st.subheader('st.sidebarで書いた')
st.page_link("https://docs.streamlit.io/develop/api-reference/layout/st.sidebar", label="st.sidebarはこちらから👈")

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

st.subheader('st.columnで書いた')
st.page_link("https://docs.streamlit.io/develop/api-reference/layout/st.columns", label="st.columnはこちらから👈")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.divider()

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)
