import streamlit as st
from openai import OpenAI
import random
import time

from utility import PromptCreation

st.set_page_config(page_title="SoulSpark", page_icon='❤️')
st.markdown("<h1 style='text-align: center; color: #8EE4AF;'>SoulSpark ❤️</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: #EDF5E1;'>Your ultimate AI date awaits!</h6>",
            unsafe_allow_html=True)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

print(st.session_state)
if "model" not in st.session_state:
    st.session_state["model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message["content"])

if prompt := st.chat_input("Hey there! Mind if we chat?"):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = PromptCreation.generic_prompt(client, st.session_state["model"], st.session_state.messages)
        # stream = client.chat.completions.create(
        #             model=st.session_state["model"],
        #             messages=[
        #                 {"role": msg["role"], "content": msg["content"]}
        #                 for msg in st.session_state.messages
        #             ], stream=True,)
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
