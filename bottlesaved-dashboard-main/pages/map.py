# page1.py
import streamlit as st
import pandas as pd
if "shared" not in st.session_state:
   st.session_state["shared"] = True

data = {
    'latitude': [37.7749, 34.0522, 40.7128],
    'longitude': [-122.4194, -118.2437, -74.0060],
    'city': ['San Francisco', 'Los Angeles', 'New York']
}
df = pd.DataFrame(data)

# Display the map
st.map(df)