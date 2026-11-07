# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🏠",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE

st.markdown("""
<style>
.stApp {
    background-color: #FFF0F5;
}
</style>
""", unsafe_allow_html=True)



st.title("Web Development Lab02")

st.header("CS 1301")
st.subheader("Web Development - Section C")
st.subheader("Name: Yuqian Huang")

st.write("Welcome to my Dessert Personality Quiz! Discover which dessert matches your personality.")

st.write("Use the sidebar to explore the following pages:")

st.write("1. **Visuals:** Explore dessert flavor charts from a JSON file and dessert personality statistics from a CSV file.")

st.write("2. **Survey:** Answer a few fun questions to discover your dessert personality. Your responses will be saved and used to update the charts on the Visuals page.")

st.image("Images/desserts.jpg", width=350)

st.subheader("Welcome to the SweetSide! 🍓")

st.write(
    "Are you a Strawberry Shortcake, Chocolate Lava Cake, "
    "Matcha Tiramisu, or Creme Brulee?"
)

st.write(
    "Answer six fun questions to discover which dessert "
    "matches your personality!"
)

st.info("👈 Head to the Survey page to start your personality test!")

st.write("✨ Stay sweet and have fun! ✨")


# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
# st.image("images/welcome_image.png")
