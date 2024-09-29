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

st.header('Welcome to WaterWorks 🤣😭💧! Rate your favourite campus fountains.', divider='gray')


import webbrowser

url = 'https://www.figma.com/proto/FEQXQxkTZfBenvMYxaxtZ3/cute?node-id=15-1205&node-type=frame&t=eSieWsLVPfvhFYe4-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=15%3A1205&show-proto-sidebar=1'

if st.button('Click this button to go in 🤩 (or scroll down if you dare😈...)!'):
    webbrowser.open_new_tab(url)

iframe_code = '''<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="1000" src="https://embed.figma.com/proto/FEQXQxkTZfBenvMYxaxtZ3/cute?node-id=15-1205&node-type=frame&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=15%3A1205&show-proto-sidebar=1&embed-host=share" allowfullscreen></iframe>'''
st.markdown(iframe_code, unsafe_allow_html=True)

st.text('This website is not fully functional yet. Come back soon....')