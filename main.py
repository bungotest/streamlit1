import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

with st.sidebar:
    st.write('目次')
    st.page_link("https://docs.streamlit.io/develop/api-reference/text", label="テキスト系Element", icon="😕")
    st.page_link("https://docs.streamlit.io/develop/api-reference/data", label="データ表示系Element", icon="😁")
    st.page_link("https://docs.streamlit.io/develop/api-reference/charts", label="図,チャート系Element", icon="😊")
    st.page_link("https://docs.streamlit.io/develop/api-reference/widgets", label="インプット系Element", icon="😊")
    st.page_link("https://docs.streamlit.io/develop/api-reference/media", label="メディア系Element", icon="😎")

st.title('Data,Map,Chart')
df=pd.DataFrame({
    'Column1' : [1,3,4,5],
    'Column2' : [3,4,7,9]
})

st.subheader('st.writeで書いた')
st.write(df)

st.divider()

st.subheader('st.titleで書いた')
st.table(df)
st.page_link("https://docs.streamlit.io/develop/api-reference/data/st.table", label="st.tableはこちらから👈")
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['data1', 'data2', 'data3']
)

st.divider()

st.subheader('st.line_chartで書いた')
st.page_link("https://docs.streamlit.io/develop/api-reference/charts/st.line_chart", label="st.linechartはこちらから👈")
st.line_chart(chart_data)

st.divider()

map_data=pd.DataFrame(
    np.random.randn(1000,2) / [50,50] 
    + [35.6894, 139.6917],
    columns=['lat','lon'] 
)

st.subheader('st.mapで書いた')
st.page_link("https://docs.streamlit.io/develop/api-reference/charts/st.map", label="st.mapはこちらから👈")
st.map(map_data)


st.divider()
st.subheader('st.data_editorで書いた')

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.divider()
st.subheader('st.column_config')

st.write('st.column_config.DatetimeColumnで書いた')
data_df = pd.DataFrame(
    {
        "appointment": [
            datetime(2024, 2, 5, 12, 30),
            datetime(2023, 11, 10, 18, 0),
            datetime(2024, 3, 11, 20, 10),
            datetime(2023, 9, 12, 3, 0),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "appointment": st.column_config.DatetimeColumn(
            "Appointment",
            min_value=datetime(2023, 6, 1),
            max_value=datetime(2025, 1, 1),
            format="D MMM YYYY, h:mm a",
            step=60,
        ),
    },
    hide_index=True,
)

st.write('st.column_config.NumberColumnで書いた')
data_df = pd.DataFrame(
    {
        "price": [20, 950, 250, 500],
    }
)

st.data_editor(
    data_df,
    column_config={
        "price": st.column_config.NumberColumn(
            "Price (in USD)",
            help="The price of the product in USD",
            min_value=0,
            max_value=1000,
            step=1,
            format="$%d",
        )
    },
    hide_index=True,
)
st.divider()
st.subheader('st.metric')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.divider()
st.subheader('st.json')
st.json(
    {
        "foo": "bar",
        "stuff": [
            "stuff 1",
            "stuff 2",
            "stuff 3",
        ],
        "level1": {"level2": {"level3": {"a": "b"}}},
    },
    expanded=2,
)

st.divider()

st.title('Media系-Color Picker,Video')

st.subheader('Colorピッカー')
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

st.divider()

st.subheader('video')
video_file = open("sky1.mp4", "rb")
video_sky1 = video_file.read()

st.video(video_sky1, subtitles="subtitles.vtt")

