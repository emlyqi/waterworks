# page1.py
import streamlit as st

import folium
from streamlit_folium import st_folium


if "shared" not in st.session_state:
   st.session_state["shared"] = True

m = folium.Map(location=[43.471041, -80.541412], zoom_start=15)

folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('CartoDB dark_matter').add_to(m)
folium.TileLayer('CartoDB positron').add_to(m)
folium.LayerControl().add_to(m)


# Sample data for locations
locations = [
    {"name": "fountain1", "lat": 43.471041, "lon": -80.541412},
    {"name": "fountain2", "lat": 43.471041, "lon": -80.530130},
    {"name": "fountain3", "lat": 43.471041, "lon": -80.490233},
]

# st.

# Optional: Add a custom CircleMarker for precision
for loc in locations:
    folium.CircleMarker(
        location=[loc['lat'], loc['lon']],
        radius=3,  # Adjust the size here
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        popup=loc['name']
    ).add_to(m)

# Display the map
st_folium(m, width=700)