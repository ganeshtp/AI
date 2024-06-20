import streamlit as st

from langchain_openai import ChatOpenAI

import re

# loading the OpenAI api key from .env (OPENAI_API_KEY="sk-********")
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)


from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


st.set_page_config(page_title="Simple conversation app Demo", page_icon=":robot:")
st.header("Hey, I'm your Chat assistant")



if "sessionMessages" not in st.session_state:
     st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assistant.")
    ]



def load_answer(question):

    st.session_state.sessionMessages.append(HumanMessage(content=question))

    assistant_answer  = chat.invoke(st.session_state.sessionMessages )

    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))

    return assistant_answer.content


def get_text():
    input_text = st.text_input("You: ")
    return input_text


chat = ChatOpenAI(temperature=0)

prompt = st.chat_input("Say something")
while True:
    
    if prompt:
        st.write(f"User: {prompt}")
        assistant_answer  = load_answer(prompt)
        st.write(f"AI: {assistant_answer}")


