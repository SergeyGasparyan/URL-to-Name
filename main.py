import streamlit as st
import requests
from bs4 import BeautifulSoup


def find_title(url):
    url = 'https://www.google.com/search?q=' + url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    res = str(soup.find_all(class_="BNeawe vvjwJb AP7Wnd"))

    start_pos = res.index('AP7Wnd">') + 8
    end_pos = res.index('</div>')
    return res[start_pos:end_pos]


st.title("AI/ML Internship - phase2")
st.header("Extract company name from URL")
firstname = st.text_input('Enter URL')
st.sidebar.title('Source code')
st.sidebar.write('https://github.com/SergeyGasparyan/URL-to-Name')

if st.button("Submit"):
    result = find_title(firstname.title())
    st.success(result)
