import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Sidebar Example")

# Sidebar Widgets
st.sidebar.header("Sidebar Options")

# Dropdown menu
option = st.sidebar.selectbox(
    "Select an option:", 
    ["Option 1", "Option 2", "Option 3"]
)
st.write("You selected:", option)

# Text Input
user_input = st.sidebar.text_input("Enter your name:", "Type here...")
st.write(f"Hello, {user_input}!")

# Slider
age = st.sidebar.slider("Select your age:", 1, 100, 25)
st.write(f"Your age is: {age} years")

# Checkbox for additional information
if st.sidebar.checkbox("Show additional information"):
    st.subheader("Additional Information")
    st.write(f"Hi {user_input}, here's some data generated based on your selection:")
    
    # data
    data = pd.DataFrame({
        'Category': ['Chief Guest', 'CEO', 'Project Manager','HSE Manager'],
        'Values': ['Mr A', 'Mr B','Ms C', 'Mrs D'],
        'Hours of Speech':[0.5,1.0,1.0,1.5]

    })
    st.write(data)


# Radio Buttons
feedback = st.sidebar.radio(
    "How do you like the app so far?", 
    ["It's great!", "Could be better", "Not a fan"]
)
if feedback == "It's great!":
    st.success("Thank you for your positive feedback!")
elif feedback == "Could be better":
    st.info("We appreciate your suggestions!")
else:
    st.warning("We’ll work on improving the app.")

# Button for an action
if st.sidebar.button("Click Me!"):
    st.balloons()
    st.write("You clicked the button! 🎉")
else:
    st.write("Try clicking the button on the sidebar.")

# Dynamic Message Based on Selection
st.write("Here's a special message for you:")
if option == "Option 1":
    st.write("You chose Option 1! 🚀")
elif option == "Option 2":
    st.write("Option 2 is a fantastic choice! 🌟")
else:
    st.write("Option 3 is always a winner! 🏆")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("**Made with ❤️ using Streamlit**")