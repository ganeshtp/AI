import streamlit as st

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

import json

# loading the OpenAI api key from .env (OPENAI_API_KEY="sk-********")
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)


def callback():
    st.session_state.button1_clicked = True

def clear_session():
    # Delete all the items in Session state
    for key in st.session_state.keys():
        del st.session_state[key]



st.title("Welcome to the Quiz :thumbsup:")

if "button1_clicked" not in st.session_state:
    st.session_state.button1_clicked = False

if "GPT_RUN" not in st.session_state:
    st.session_state.GPT_RUN = False

if st.session_state.button1_clicked == False:
    st.session_state['subject'] = st.sidebar.text_input("Enter subject to generate question")
    st.session_state.grade = st.sidebar.slider('Grade', min_value =1, max_value= 10)


button = st.sidebar.button("Generate question", on_click= callback)
if button or st.session_state.button1_clicked == True:
    subject = st.session_state['subject']
    grade = st.session_state.grade
    # Define a template for the prompt
    template = '''You are an experienced quiz master.
    Please generate 10 questions with 4 options to choose based on the subjext "{subject}" for a person who is studying in {grade} and give the output in json format.'''

    # Create a PromptTemplate object from the template
    prompt_template = PromptTemplate.from_template(template=template)

    # Fill in the variable: subject and grade
    prompt = prompt_template.format(subject = subject, grade=grade)

    if st.session_state.GPT_RUN == False:
        llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)
        output = llm.invoke(prompt)
        print("-" * 50)

        st.session_state['json_object'] = json.loads(output.content)
        print(st.session_state['json_object'])
        print("-------------------------------")
        st.session_state.GPT_RUN = True
    
    ans = []
    for i in range(len(st.session_state['json_object']['questions'])):
        #temp = "question"+str(i+1)
        temp = "questions"
        answer = st.radio(st.session_state['json_object'][temp][i]['question'], 
                st.session_state['json_object'][temp][i]['options'],
                key=i)
        ans.append(answer)
    print(ans)
    submit_button = st.button(label='Submit')
    if submit_button:
        st.session_state.button1_clicked = True
        count = 0
        for i in range(len(st.session_state['json_object']['questions'])):
            if ans[i] == st.session_state['json_object']["questions"][i]['answer']:
                count += 1
        print(f"You have answered  {count} out of 10 correctly")
        st.write("You have answered ", count, "out of 10 correctly")
button = st.sidebar.button("Rerun app", on_click = clear_session)

