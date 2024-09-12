import streamlit as st
import speech_recognition as sr
from setuptools._distutils.version import LooseVersion
r = sr.Recognizer()

def transcribe_speech():
    # Initialize recognizer class
    
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        r.pause_threshold=0.6
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # using Google Speech Recognition
            text = r.recognize_google(audio_text,language='en-us')
            return text
        except:
            return "Sorry, I did not get that."



def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech()
        st.write("Transcription: ", text)

main()
   
