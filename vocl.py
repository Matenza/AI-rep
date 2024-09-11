import streamlit as st
import speech_recognition as sr

r = sr.Recognizer()

def transcribe_speech():
    # Lire depuis le microphone
    with sr.Microphone() as source:
        st.info("Speak now...")
        r.pause_threshold = 0.6
        # Écouter et stocker dans la variable audio_text
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # Utilisation de Google Speech Recognition
            text = r.recognize_google(audio_text, language='en-us')
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Could not request results from Google Speech Recognition service."

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # Ajouter un bouton pour déclencher la reconnaissance vocale
    if st.button("Start Recording"):
        text = transcribe_speech()
        st.write("Transcription: ", text)

main()
