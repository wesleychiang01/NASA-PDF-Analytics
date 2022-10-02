import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np


def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link
    return f'<a target="_blank" href="{link}">Original</a>'


def make_clickable2(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link
    return f'<a target="_blank" href="{link}">Click</a>'


title_container = st.container()
col1, col2 = st.columns([4, 15])
image = Image.open('SoloMan.png')
with title_container:
    with col1:
        st.image(image, width=150)
    with col2:
        st.markdown('<h1>NASA Technical Report Collection</h1>', unsafe_allow_html=True)

df = pd.read_excel('Result.xlsx')

df['Original'] = df['Original'].apply(make_clickable)
df['Result'] = df['Result'].apply(make_clickable2)
df = df.to_html(escape=False)
st.write(df, unsafe_allow_html=True)
