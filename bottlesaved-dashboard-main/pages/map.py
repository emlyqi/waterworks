# page1.py
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import mysql.connector

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

query = "SELECT fountain_name, longitude, latitude FROM  Water_Fountains"

# Read SQL file and execute it
with conn.cursor() as cursor:
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [i[0] for i in cursor.description]
    data = pd.DataFrame(result, columns=columns)

# Fetch data from the SQLite database



print("Executing SQL script:")


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
        popup=row['fountain_name']
    ).add_to(m)

# Display the map
st_folium(m, width=700)