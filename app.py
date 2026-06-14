import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(
    page_title="Python AI Assistant",
    page_icon="🤖"
)

st.title("🤖 Python AI Assistant")
st.write("An intelligent assistant built with Python and Artificial Intelligence.")

if not api_key:
    st.warning("Please add your OPENAI_API_KEY in the .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=st.session_state.messages
    )

    answer = response.choices[0].message.content

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)
