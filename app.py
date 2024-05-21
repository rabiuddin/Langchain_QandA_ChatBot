from langchain_openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

#This load the secret key
load_dotenv()

#This function will get the response from the OpenAI API
def get_openai_response(question):
    llm = OpenAI(openai_api_key = os.environ["OPENAI_API_KEY"],model="gpt-3.5-turbo-instruct", temperature=0.6 )
    response = llm.invoke(question)

    return response


st.set_page_config(page_title="Q&A Demo", page_icon="🔗")
st.header("Langchain Application")

input = st.text_input("Enter the question: ", key="input")

submit = st.button("Ask the Question")

#If the submit button is clicked and the input is not empty
if submit and input:
    response = get_openai_response(input)
    st.subheader("The response is: ")
    st.write(response)