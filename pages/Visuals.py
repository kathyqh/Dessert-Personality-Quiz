# This creates the page for displaying data visualizations.

import streamlit as st
import json
import matplotlib.pyplot as plt
import os
import pandas as pd

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

st.markdown("""
<style>
.stApp {
    background-color: #FFF0F5;
}
</style>
""", unsafe_allow_html=True)


# PAGE TITLE
st.title("🍰 What Dessert Matches Your Personality?")


# PART 1: GRAPHS FROM data.json

with open("data.json", "r") as file:
    data = json.load(file)

flavors = []
counts = []

for item in data["data_points"]:
    flavors.append(item["label"])
    counts.append(item["value"])
st.subheader("Favorite Dessert Flavors 🍓")
st.bar_chart({"Flavor": flavors, "Count": counts},
             x="Flavor", y="Count")

st.subheader("Dessert Flavor Distribution 🥧")

if "num_flavors" not in st.session_state:
    st.session_state.num_flavors = 4

num = st.slider(
    "How many flavors would you like to see?",
    min_value=1,
    max_value=len(flavors),
    key="num_flavors"
)

fig, ax = plt.subplots()
ax.pie(counts[:num], labels=flavors[:num], autopct="%1.1f%%")
ax.set_title("Dessert Flavor Distribution")
st.pyplot(fig)
plt.close(fig)


# PART 2: GRAPHS FROM data.csv
st.divider()
st.header("🍰 Dessert Personality Statistics")

if os.path.exists("data.csv"):
    dessertData = pd.read_csv("data.csv")

    st.subheader("Which Dessert Personality is Most Popular? 🍓")
    dessertCounts = dessertData["dessert_result"].value_counts()
    st.bar_chart(dessertCounts)

    st.subheader("How Sweet Is Your Personality? 🍬")

    dessertChoices = ["All"] + dessertData["dessert_result"].unique().tolist()

    if "selectedDessert" not in st.session_state:
        st.session_state.selectedDessert = "All"

    selectedDessert = st.selectbox(
    "Choose a dessert personality:",
    dessertChoices,
    key="selectedDessert"
    )

    if selectedDessert == "All":
        filteredData = dessertData
    else:
        filteredData = dessertData[
            dessertData["dessert_result"] == selectedDessert
        ]

    fig, ax = plt.subplots()

    ax.hist(
        filteredData["sweet_tooth"],
        bins=range(1, 12),
        edgecolor="black"
    )

    ax.set_title("Sweet Tooth Levels")
    ax.set_xlabel("Sweet Tooth Level (1–10)")
    ax.set_ylabel("Number of Responses")

    st.pyplot(fig)
    plt.close(fig)

    
    st.metric("Mean Sweet Tooth Level", round(filteredData["sweet_tooth"].mean(), 2))
    st.metric("Median Sweet Tooth Level", round(filteredData["sweet_tooth"].median(), 2))

else:
    st.info("No data avaiable yet!")

    
