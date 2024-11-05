import streamlit as st
import pandas

# Define layout
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Alex")
    content = """
    
    Cyber Security student
    
    """

    st.info(content)

content2 = """

    Below you can find some of the apps i have built in Python. 
    Feel free to contact me!

    """

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# Get data
df = pandas.read_csv("data.csv", sep=";")

# Divide the page into two and loop through dataset to display images, description and link to project
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

