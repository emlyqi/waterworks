import streamlit as st
import pandas as pd
import math
from pathlib import Path
from pages import graphs
from pages import map
# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Bottle Saved at Top 50 Waterloo Water Fountains',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

st.header('Hello World')
st.selectbox('Who are you?', ['Login','Register','WatIAm'])
st.button('Click this button to go in!')

st.header('Welcome to WaterWorks! Rate your favourite campus fountains.', divider='gray')
st.text('This website is not fully functional yet. Come back soon....')