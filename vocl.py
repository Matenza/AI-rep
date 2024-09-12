import streamlit as st
import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

# Session state
if 'text' not in st.session_state:
	st.session_state['text'] = 'Listening...'
	st.session_state['run'] = False

# Audio parameters 
st.sidebar.header('Audio Parameters')

FRAMES_PER_BUFFER = int(st.sidebar.text_input('Frames per buffer', 3200))
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = int(st.sidebar.text_input('Rate', 16000))
p = pyaudio.PyAudio()

# Open an audio stream with above parameter settings
stream = p.open(
   format=FORMAT,
   channels=CHANNELS,
   rate=RATE,
   input=True,
   frames_per_buffer=FRAMES_PER_BUFFER
)

# Start/stop audio transmission
def start_listening():
	st.session_state['run'] = True

def download_transcription():
	read_txt = open('transcription.txt', 'r')
	st.download_button(
		label="Download transcription",
		data=read_txt,
		file_name='transcription_output.txt',
		mime='text/plain')

def stop_listening():
	st.session_state['run'] = False

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
