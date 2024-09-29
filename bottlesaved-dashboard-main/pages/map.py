# page1.py
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import mysql.connector
import os

# # Path to your background image
# background_image_path = os.path.join("assets", "hugeBg.png")

# Set up CSS for the background

# background_image = """
# <style>
# [data-testid="stAppViewContainer"] > .main {
#     background-image: url("{background_image_path}");
#     background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
#     background-position: center;  
#     background-repeat: no-repeat;
# }
# </style>
# """
# st.markdown(background_image, unsafe_allow_html=True)

# def load_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# load_css("C:/Users/cathe/waterworks/bottlesaved-dashboard-main/pages/background.css")

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


# # st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url({background_image_path});
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

def create_connection():
    connection = mysql.connector.connect(
        host='localhost',  # e.g., 'localhost'
        user='yuan',
        password='SQLjhyuan101!',
        database='waterworks'
    )
    return connection


if "shared" not in st.session_state:
   st.session_state["shared"] = True

# Create a temporary SQLite database
conn = create_connection()

query = "SELECT fountain_name, building, location_in_building, longitude, latitude FROM  Water_Fountains"

# Read SQL file and execute it
with conn.cursor() as cursor:
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [i[0] for i in cursor.description]
    data = pd.DataFrame(result, columns=columns)

# Fetch data from the SQLite database

m = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=15)

folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('CartoDB dark_matter').add_to(m)
folium.TileLayer('CartoDB positron').add_to(m)
folium.LayerControl().add_to(m)


for idx, row in data.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=3,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        popup =row['fountain_name']+ '\nBuilding: ' + row['building'] + '\n Spot: ' + row['location_in_building']
    ).add_to(m)

# Display the map
st_folium(m, width=700)

