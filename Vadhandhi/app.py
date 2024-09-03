import streamlit as st
from text_process import process_text_input
from image_process import process_image_input
from audio_process import process_audio_input
# Constants
flag=0

# Streamlit UI
st.title("Fake News Verification System")
st.write("Enter a news keyword to search and verify its authenticity.")

# User chooses the type of input
input_type = st.selectbox("Choose your input type:", ("Text", "Image", "Audio"))


# Choose the appropriate function based on the user's input type
if input_type == "Text":
    process_text_input("",flag)
elif input_type == "Image":
    flag=1
    process_image_input()
elif input_type == "Audio":
    flag=1
    process_audio_input()