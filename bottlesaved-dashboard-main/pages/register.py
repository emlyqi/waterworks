import streamlit as st
import streamlit.components.v1 as components
path_to_html = r"C:\Users\cathe\waterworks\bottlesaved-dashboard-main\pages\saveme.html"
file_name = r"C:\Users\cathe\waterworks\bottlesaved-dashboard-main\pages\index.css"

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.ibb.co/fMMhNLB/hugeBg.png");
    background-size: 100vw 140vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

with open(path_to_html,'r') as f: 
    html_content = f.read()

components.html(html_content, height = 1000)

