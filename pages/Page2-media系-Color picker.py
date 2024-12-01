import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Media系-Color Picker,Video')

st.subheader('Colorピッカー')
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)
