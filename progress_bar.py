import streamlit as st
import time

st.title("Progress Bar Example")

progress_bar = st.progress(0)
for percent in range(100):
    time.sleep(0.05)
    progress_bar.progress(percent + 1)

st.write("Progress Completed!")