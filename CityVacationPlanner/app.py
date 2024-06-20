
import streamlit as st

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

import json


# loading the OpenAI api key from .env (OPENAI_API_KEY="sk-********")
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)




st.title("City Vacation Planner :thumbsup:")


city = st.sidebar.text_input("Enter city")
age = st.sidebar.slider('Age')

if not city:
    city = 'paris'

if not age:
    age = 40

# Define a template for the prompt
template = '''You are an experienced travel advisory.
 Please share the places to visit in "{city}" for a person who is {age} years old and give the output in json format.'''

# Create a PromptTemplate object from the template
prompt_template = PromptTemplate.from_template(template=template)

# Fill in the variable: city and age
prompt = prompt_template.format(city = city, age=age)
#prompt  # Returns the generated prompt


llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)
output = llm.invoke(prompt)
print("-" * 50)

json_object = json.loads(output.content)
print(json_object)
print("-" * 50)
#data = output.content
print(type(json_object))
map_lat_long = []
place = []

#print(data)
#print(json_object['age'])
#print("-" * 50)
#print(json_object['destination'])
#print("-" * 50)
#print(json_object['places_to_visit'])
#print("-" * 50)
#st.write(output.content)
for i in range(len(json_object['places_to_visit'])):
    #print(data['places_to_visit'][i])
    place.append(json_object['places_to_visit'][i]['name'])
    # Import the required library
    from geopy.geocoders import Nominatim

    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="MyApp")

    loc = place[i] + ', ' + city
    print(loc)
    location = geolocator.geocode(loc)
    if location:
        map_lat_long.append([location.latitude, location.longitude])


import pandas as pd
import numpy as np

df = pd.DataFrame(
    map_lat_long,
    columns=['lat', 'lon'])

st.map(df)





