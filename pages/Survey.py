import streamlit as st
import pandas as pd
import os

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

st.markdown("""
<style>
.stApp {
    background-color: #FFF0F5;
}
</style>
""", unsafe_allow_html=True)


# PAGE TITLE AND USER DIRECTIONS
st.title("🍰 What Dessert Matches Your Personality?")
st.write("Let's find your sweet alter ego!")


st.image("Images/dessert.jpg", width=500)


# DATA INPUT FORM
with st.form("survey_form"):

    fridayNight = st.radio(
        "1. It's Friday night. Where are you?",
        [
            "At a cute cafe with friends",
            "In bed watching Netflix",
            "At a cosplay party",
            "In the library pretending to study"
        ]
    )

    redFlag = st.radio(
        "2. What's your biggest red flag?",
        [
            "I overthink everything",
            "I always procrastinate until the last minute",
            "I spend too much on little treats",
            "I pretend everything is fine"
        ]
    )

    stressResponse = st.radio(
        "3. How do you deal with stress?",
        [
            "Shop my stress away 💸",
            "Take a twelve-hour nap 😴",
            "Cry a little, then move on 😭",
            "Make a to-do list and panic 😨"
        ]
    )

    friendType = st.radio(
        "4. What kind of friend are you?",
        [
            "The therapist",
            "The mom/dad",
            "The funny one",
            "The quiet observer"
        ]
    )

    favFlavor = st.radio(
        "5. Pick your favorite ice cream flavor!",
        [
            "Strawberry",
            "Chocolate",
            "Matcha",
            "Vanilla"
        ]
    )
    
    sweetTooth = st.slider(
        "6. How much of a sweet tooth do you have?",
        min_value=1,
        max_value=10,
        value=5
    )
            
    submitted = st.form_submit_button("Submit Data")

    if submitted:
        desserts = [
            "Strawberry Shortcake",
            "Chocolate Lava Cake",
            "Matcha Tiramisu",
            "Creme Brulee"
        ]

        answers = [
            fridayNight,
            redFlag,
            stressResponse,
            friendType,
            favFlavor
        ]

        options = [
            [
                "At a cute cafe with friends",
                "In bed watching Netflix",
                "At a cosplay party",
                "In the library pretending to study"
            ],
            [   "I overthink everything",
                "I always procrastinate until the last minute",
                "I spend too much on little treats",
                "I pretend everything is fine"
            ],
            [   "Shop my stress away 💸",
                "Take a twelve-hour nap 😴",
                "Cry a little, then move on 😭",
                "Make a to-do list and panic 😨"
            ],
            [   "The therapist",
                "The mom/dad",
                "The funny one",
                "The quiet observer"
            ],
            [   "Strawberry",
                "Chocolate",
                "Matcha",
                "Vanilla"
            ]
        ]

        dessertImages = {
            "Strawberry Shortcake": "Images/strawberry.jpg",
            "Chocolate Lava Cake": "Images/chocolate.jpg",
            "Matcha Tiramisu": "Images/matcha.jpg",
            "Creme Brulee": "Images/creme_brulee.jpg"
        }

        scores = [0,0,0,0]

        for i in range(len(answers)):
            choiceIndex = options[i].index(answers[i])
            scores[choiceIndex] += 1

        dessertIndex = scores.index(max(scores))
        dessertResult = desserts[dessertIndex]

        if dessertResult in dessertImages:
            st.image(dessertImages[dessertResult], width=300)

        st.subheader("Your Dessert Personality Is... 🍰")
        st.success(dessertResult)
            
        # --- YOUR LOGIC GOES HERE ---
        # TO DO:
        # 1. Create a new row of data from 'category_input' and 'value_input'.
        # 2. Append this new row to the 'data.csv' file.
        #    - You can use pandas or Python's built-in 'csv' module.
        #    - Make sure to open the file in 'append' mode ('a').
        #    - Don't forget to add a newline character '\n' at the end.
        
        new_data = pd.DataFrame({
            "friday_night": [fridayNight],
            "red_flag": [redFlag],
            "stress_response": [stressResponse],
            "friend_type": [friendType],
            "favorite_flavor": [favFlavor],
            "sweet_tooth": [sweetTooth],
            "dessert_result": [dessertResult]
        })

        new_data.to_csv(
        "data.csv",
        mode="a",
        header=not os.path.exists("data.csv"),
        index=False
        )

        st.success("Your response has been saved!")

        st.divider()
        st.header("🍰 Dessert Quiz Responses")

        if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:
            currentData = pd.read_csv("data.csv")
            st.dataframe(currentData)
        else:
            st.info("No responses yet!")


# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
