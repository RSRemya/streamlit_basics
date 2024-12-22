import streamlit as st
# Title
st.title("Markdown Example in Streamlit")

# Subtitle
st.markdown("## This is a subtitle created using Markdown")

# Text with Emphasis
st.markdown("*This text is italicized* and **this text is bold**.")

# Bullet Points
st.markdown("""
### Features of Streamlit:
- Easy to use
- Interactive widgets
- Supports Markdown
""")

# Links
st.markdown("[Click here to visit Streamlit Documentation](https://docs.streamlit.io/)")

# Images
st.markdown("![Streamlit Logo](https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png)")

# Code Block
st.markdown("""
```python
# This is a code block
import streamlit as st

st.title("Hello, Streamlit!")""")