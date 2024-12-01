import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

st.title('インプット系Element')

st.subheader('st.sliderで書いた')
st.page_link("https://docs.streamlit.io/develop/api-reference/widgets/st.slider", label="st.sliderはこちらから👈")
x=st.slider('x')
st.write(x, 'を2倍にすると', 2*x)

st.divider()

st.subheader('その他、st.checkbox, st.で書いた')

st.page_link("https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox", label="st.checkboxはこちらから👈")
st.page_link("https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox", label="st.selectboxはこちらから👈")

st.write('Checkbox')
agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

st.divider()

st.write('Checkbox')
option=st.selectbox(
    'How do you want to get contact?',
    ('email','call','visit','video conf')
)
st.write('you selected : ', option)


