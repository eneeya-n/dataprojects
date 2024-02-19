!pip install pymysql
import streamlit as st
import pandas as pd
import pymysql
import speech_recognition as sr
import pandas as pd
import re
from IPython.display import Markdown
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import streamlit as st

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
import os
import re
os.environ['GOOGLE_API_KEY']="AIzaSyDyjbk9QFtz-h8p-NMY1Zk0aD7dPYxVA_0"
genai.configure(api_key="AIzaSyDyjbk9QFtz-h8p-NMY1Zk0aD7dPYxVA_0")
model = genai.GenerativeModel('gemini-pro')


def generate_responses1(a):
    model = genai.GenerativeModel('gemini-pro')
    answer = model.generate_content(f"give sql query for the question {a} usig the tables inside the {result}")
    return Markdown(answer.text).data

conn=pymysql.connect(host = '127.0.0.1',user='root',passwd='admin@123',database = "youtube")
        # Use Pandas to execute SQL queries
result = pd.read_sql_query("select * from car_prices", conn)

# Streamlit App
def main():
    st.title("SQL Query Runner")

    # Text area for user input
    query = st.text_area("Enter your Question here:", "Iam ready to help you")

    # Run Query button
    if st.button("get answer"):
        if query.strip() != "":
            result = generate_responses1(query)
            if isinstance(result, pd.DataFrame):
                st.success("Query executed successfully!")
                st.dataframe(result)
            else:
                st.error(result)
        else:
            st.warning("Please enter a valid SQL query.")

if __name__ == "__main__":
    main()
