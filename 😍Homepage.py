import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

# Add custom CSS styles for background and text colors
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f5;  /* Change this to your desired background color */
    }
    .stButton>button {
        background-color: #4CAF50; /* Green background for the submit button */
        color: white; /* White text for the button */
        border: None;
        border-radius: 30px;
        padding: 20px 40px;  /* Adjust padding for better button appearance */
        cursor: pointer;
        font-size: 300px; /* Increase font size */
        height: 60px; /* Set height for the button */
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    .win-message {
        color: #4CAF50; /* Green color for winning message */
        font-size: 24px; /* Optional: Increase font size for winning message */
    }
    .lose-message {
        color: #f44336; /* Red color for losing message */
        font-size: 24px; /* Optional: Increase font size for losing message */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎯 Let's Play a Game!")

st.sidebar.success("Select a page above.")

# Input option for number 1 to 5
if "my_input" not in st.session_state:
    st.session_state["my_input"] = 0

# Displaying the subheader for the input prompt
st.subheader("Enter a number between 1 and 5")

# Number input method
my_input = st.number_input("", min_value=1, max_value=5, step=1)
submit = st.button("Submit") 

if submit:
    st.session_state["my_input"] = my_input
    st.subheader(f"You have entered: {my_input}")

    # Generate a random number between 1 and 5 only after submission
    random_number = random.randint(1, 5)
    st.subheader(f"Generated random number: {random_number}")
   
    # Compare user input with random number
    if st.session_state["my_input"] == random_number:
        st.markdown("<h1 class='win-message'>✅ Hurrah! You have won the game! 🏆</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 class='lose-message'>❌ You have lost! ☠️</h1>", unsafe_allow_html=True)
        st.markdown("<h2 class='win-message'><br>Try Again! 😍</h2>", unsafe_allow_html=True)
else:
    # Only show this message if the user hasn't submitted yet
    st.subheader("Please enter a number and press Submit to play!")
