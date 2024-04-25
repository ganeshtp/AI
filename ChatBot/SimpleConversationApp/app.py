import streamlit as st

from langchain_openai import ChatOpenAI

import re

import os
os.environ["OPENAI_API_KEY"] = "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"


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




user_input=get_text()
submit = st.button('Generate')  



if submit:
    
    response = load_answer(user_input)
    st.subheader("Answer:")


    st.write(response)
    message = str(st.session_state.sessionMessages)
    #print(message)
    ele = message.split("),")
    #print(ele)
    msg =""
    for i in ele:
        s1, s2, s3= re.split('\(|=', i)
        s3 = s3.replace(")", "")
        s3 = s3.replace("]", "")
        msg += s3
        msg += "\n"
    st.text_area("Conversation ", msg)
    
