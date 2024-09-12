import nltk
import streamlit as st
import speech_recognition as sr
from nltk.chat.util import Chat, reflections


pairs = [
    ['bonjour', ['Bonjour ! Comment puis-je vous aider ?']],
    ['comment ça va ?', ['Je vais bien, merci. Et vous ?']],
    ['au revoir', ['Au revoir ! À bientôt.']],
]

# Initialisez le chatbot avec les paires de dialogue
chatbot = Chat(pairs, reflections)


def transcrire_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Parlez maintenant...")
        audio = r.listen(source)
        try:
            texte = r.recognize_google(audio, language="fr-FR")
            st.write(f"Vous avez dit : {texte}")
            return texte
        except sr.UnknownValueError:
            st.write("Je n'ai pas compris l'audio.")
            return ""
        except sr.RequestError:
            st.write("Erreur avec le service de reconnaissance vocale.")
            return ""


def interagir_avec_chatbot(entree):
    if entree:
        reponse = chatbot.respond(entree)
        return reponse
    else:
        return "Je n'ai pas compris votre demande."


def application():
    st.title("Chatbot à commande vocale")

    # Sélection du mode d'entrée
    mode = st.selectbox("Choisissez le mode d'entrée :", ("Texte", "Voix"))

    if mode == "Texte":
        texte_input = st.text_input("Entrez votre texte ici :")
        if texte_input:
            reponse = interagir_avec_chatbot(texte_input)
            st.write(f"Chatbot : {reponse}")

    elif mode == "Voix":
        if st.button("Cliquez pour parler"):
            texte_input = transcrire_audio()
            if texte_input:
                reponse = interagir_avec_chatbot(texte_input)
                st.write(f"Chatbot : {reponse}")

if __name__ == "__main__":
    application()
