
import streamlit as st

from langchain_openai import OpenAI


# loading the OpenAI api key from .env (OPENAI_API_KEY="sk-********")
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

def answer_query(question):
    llm = OpenAI(model_name= "davinci-002", temperature= 0.5)
    answer = llm.invoke(question)
    return answer



st.set_page_config(page_title= "Simple AI app", page_icon= ":anchor:")
st.header("Demo")

input = st.text_input("Ask your question")
button = st.button("Click for answer")

if button:

    answer = answer_query(input)
    st.write(answer)





