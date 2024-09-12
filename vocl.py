import streamlit as st
import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

from audio_recorder_streamlit import audio_recorder

audio_bytes = audio_recorder()
if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")

def is_microphone_available():
    try:
        p = pyaudio.PyAudio()
        if p.get_default_input_device_info():
            return True
    except:
        return False

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

    # Vérifier si le microphone est disponible
    if not is_microphone_available():
        st.error("Microphone not available. Please check your microphone or run this locally.")
        return

    # Ajouter un bouton pour déclencher la reconnaissance vocale
    if st.button("Start Recording"):
        text = transcribe_speech()
        st.write("Transcription: ", text)

main()
