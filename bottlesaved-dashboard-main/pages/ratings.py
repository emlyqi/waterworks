import streamlit as st;

if "shared" not in st.session_state:
   st.session_state["shared"] = True

st.image(
   st.image("./assets/mapSearch.png")
)