# page1.py
import sqlite3
import streamlit as st
from sqlalchemy import create_engine
import folium
from streamlit_folium import st_folium
import pandas as pd


if "shared" not in st.session_state:
   st.session_state["shared"] = True

# Create a temporary SQLite database
conn = sqlite3.connect('temp_database.db')

# Read SQL file and execute it
with open('waterworks.session.sql', 'r') as file:
   sql_script = file.read()

conn.execute(sql_script)

# Fetch data from the SQLite database
query = "SELECT name, longitude, latitude FROM  Water_Fountains"
data = pd.read_sql(query, conn)


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
        popup=row['name']
    ).add_to(m)

# Display the map
st_folium(m, width=700)