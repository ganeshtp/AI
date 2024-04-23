import streamlit as st


from langchain_openai import OpenAI

import os
os.environ["OPENAI_API_KEY"] = "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"

st.set_page_config(page_title="Simple Application Demo", page_icon=":shark:")
st.header("Demo")

question = st.text_input("Question plz:", key="input")

llm = OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0)

    #Last week langchain has recommended to use invoke function for the below please :)
answer=llm.invoke(question)

ack = st.button("Query")

if ack:

    st.subheader("Answer:")

    st.write(answer)

