import os
import requests

import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_HOST = os.environ.get("HOST", "0.0.0.0")
API_PORT = int(os.environ.get("PORT", 8080))
URL = f"http://{API_HOST}:{API_PORT}/"

st.set_page_config(page_title="InstiGPT Prototype")

st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        with st.status("Generating an answer..."):
            data = {"query": prompt}
            response = requests.post(URL, json=data)
        if response.status_code == 200:
            msg = {"role": "assistant", "content": response.json()}
            st.write(msg["content"])
            st.session_state.messages.append(msg)
        else:
            st.error(f"Failed to send data to API. Status code: {response.status_code}")
