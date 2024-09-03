from text_process import process_text_input
import speech_recognition as sr
import streamlit as st

# Function to process audio input
def process_audio_input():
    flag=1
    uploaded_audio = st.file_uploader("Upload an audio file containing speech", type=["wav", "mp3", "m4a"])

    if uploaded_audio is not None:
        st.audio(uploaded_audio, format="audio/wav")

        with st.spinner("Processing audio..."):
            recognizer = sr.Recognizer()
            audio_file = sr.AudioFile(uploaded_audio)

            with audio_file as source:
                audio_data = recognizer.record(source)
                try:
                    # Use speech recognition to extract text from audio
                    extracted_text = recognizer.recognize_google(audio_data)
                    st.write("**Extracted Text from Audio:**")
                    st.write(extracted_text)

                    # Continue processing with the extracted text
                    if extracted_text.strip():
                        process_text_input(extracted_text,flag)
                except sr.UnknownValueError:
                    st.error("Could not understand the audio. Please try again with a clearer audio file.")
                except sr.RequestError:
                    st.error("Could not request results from Google Speech Recognition service; check your network connection.")