import streamlit as st

# Title and Introduction
st.title("Interactive Widgets Example")

# Text Input
st.subheader("Personal Information")
name = st.text_input("Enter your name:", "Type here...")
st.write("Hello, ", name)

# Slider for Age
age = st.slider("How old are you?", 0, 100, 25)
if age < 18:
    st.warning("You're a minor!")
elif 18 <= age < 60:
    st.info("You're an adult!")
else:
    st.success("You're a senior citizen!")

# Dropdown for Location Selection
locations = ['New Delhi', 'Riyadh', 'Muscat', 'Doha', 'Dubai', 'Cairo']
location = st.selectbox("Select Your Location", locations)
st.write(f"You are currently in **{location}**.")

# Number Input for Journey Hours
hours = st.number_input("Hours of Journey", min_value=1.0, step=0.5)
st.write(f"Your journey will take approximately **{hours} hours**.")

# Additional Widgets
st.subheader("Additional Preferences")
# Radio Buttons for Travel Mode
travel_mode = st.radio("Select your mode of travel:", ["Car", "Train", "Plane", "Ship"])
st.write(f"You prefer to travel by **{travel_mode}**.")

# Multi-Select for Accompanying People
companions = st.multiselect(
    "Who are you traveling with?",
    ["Family", "Friends", "Colleagues", "Alone"]
)
if companions:
    st.write("You are traveling with: ", ", ".join(companions))
else:
    st.write("You are traveling alone.")

# Checkbox for Confirming Booking
confirm_booking = st.checkbox("Confirm your booking?")
if confirm_booking:
    st.success("Your booking has been confirmed!")
else:
    st.warning("Please confirm your booking.")

# Dynamic Results Based on Inputs
st.subheader("Summary of Your Inputs")
st.write(f"**Name:** {name}")
st.write(f"**Age:** {age}")
st.write(f"**Location:** {location}")
st.write(f"**Journey Duration:** {hours} hours")
st.write(f"**Mode of Travel:** {travel_mode}")
if companions:
    st.write(f"**Accompanying:** {', '.join(companions)}")
else:
    st.write("**Accompanying:** None")

if confirm_booking:
    st.write("Thank you for confirming your booking! Have a safe journey!")

# Footer
st.markdown("---")
st.write("**Made with ❤️ using Streamlit**")
