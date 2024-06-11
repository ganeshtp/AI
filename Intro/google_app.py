import streamlit as st


from langchain_google_genai import GoogleGenerativeAI


# loading the Google api key from .env (GOOGLE_API_KEY="********")
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

def answer_query(question):
    llm = GoogleGenerativeAI(model= "gemini-pro", temperature= 0.5)
    answer = llm.invoke(question)
    return answer



st.set_page_config(page_title= "Simple AI app", page_icon= ":anchor:")
st.header("Demo")

input = st.text_input("Ask your question")
button = st.button("Click for answer")

if button:

    answer = answer_query(input)
    st.write(answer)
