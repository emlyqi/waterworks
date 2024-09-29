import streamlit as st


if "shared" not in st.session_state:
   st.session_state["shared"] = True

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'register'

# Define a function to navigate between pages
def navigate_to(page_name):
    st.session_state.page = page_name

# register Page
if st.session_state.page == 'register':
    st.image("./assets/register.png")
    st.text_input("WatIAM: ")
    st.text_input("password: ")
    st.text_input("confirm password: ")
    if st.button('or login'):
        navigate_to('login')
    if st.button('Join!'):
        navigate_to('steve')

# login
elif st.session_state.page == 'login':
    st.image("./assets/login.png")
    if st.button('or register now'):
        navigate_to('register')

# steve
elif st.session_state.page == 'steve':
    st.image("./assets/steve.png")
    if st.button('add a new rating now'):
        navigate_to('rate_steve')

# rate steve
elif st.session_state.page == 'rate_steve':
    st.image("./assets/rate_steve.png")
    rate_appearance = st.selectbox("appearance: ",[1,2,3,4,5])
    rate_texture = st.selectbox("texture: ",[1,2,3,4,5])
    rate_taste = st.selectbox("taste: ",[1,2,3,4,5])
    rate_colour = st.selectbox("colour: ",[1,2,3,4,5])
    if st.button('submit'):
        navigate_to('steve')
