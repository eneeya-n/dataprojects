import streamlit as st
import speech_recognition as sr


import pandas as pd
import re
from IPython.display import Markdown
import pathlib
import textwrap




import google.generativeai as genai




from IPython.display import display
from IPython.display import Markdown
import streamlit as st


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
import os
import re
os.environ['GOOGLE_API_KEY']="AIzaSyDyjbk9QFtz-h8p-NMY1Zk0aD7dPYxVA_0"
genai.configure(api_key="AIzaSyDyjbk9QFtz-h8p-NMY1Zk0aD7dPYxVA_0")
model = genai.GenerativeModel('gemini-pro')




def generate_responses1(a):
    model = genai.GenerativeModel('gemini-pro')
    answer = model.generate_content(f"give feedback for the question difference between group by and having and give marks out of 10 for the answer{a}")
    return Markdown(answer.text).data


def generate_responses2(a):
    model = genai.GenerativeModel('gemini-pro')
    answer = model.generate_content(f"give feedback for the question different types of joins and give marks out of 10 for the answer{a}")
    return Markdown(answer.text).data

# Function to recognize speech from audio input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source: 
        st.write("Please speak, then click 'Stop' when finished recording:")
        audio = recognizer.listen(source)
        #st.write("Recording stopped. Transcribing...")

    try:
        user_input = recognizer.recognize_google(audio)
        return user_input
    except sr.UnknownValueError:
        st.error("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        st.error(f"Could not request results; {e}")



# Streamlit app layout
st.title("Speech-based Chatbot")

st.subheader("Tell me the difference between group by and having")

# Button to start recording
if st.button("Start Recording - Q1"):
    user_input1 = recognize_speech()
    if user_input1:
        st.write("You said:", user_input1)
        st.write("You answer:", generate_responses1(user_input1))


st.subheader("Tell me the different types of Joins")
if st.button("Start Recording - Q2"):
    user_input2 = recognize_speech()
    if user_input2:
        st.write("You said:", user_input2)
        st.write("You answer:", generate_responses2(user_input2))
