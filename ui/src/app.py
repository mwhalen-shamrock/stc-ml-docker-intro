import os
import requests

import streamlit as st
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("API_HOSTNAME")
prediction_endpoint = "/predict"
query_endpoint = "/query"

st.title("A Simple Application")

button = st.button("Call the API")

if button:
    response = requests.post(url + prediction_endpoint, json={'feature_a': 1, 'feature_b': 2})

    st.write(response.text)


sql_query = st.text_input("Enter your SQL query")
query_button = st.button("Query the database")

if query_button:
    response = requests.post(url + query_endpoint, json={"query": sql_query})
    st.write(response.text)