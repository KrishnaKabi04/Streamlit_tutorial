import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import time, datetime

st.set_page_config(page_title= "Test",layout= 'wide')
st.header('Basics of Streamlit ')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')


st.write('Hello, *World!* :sunglasses:')
st.write(1234)

col1, col2 = st.columns(2)

with col1:
    df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
    st.write(df)

    df2 = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
    c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.write(c)

with col2:
    st.write('Interactive plot')
    d = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']).interactive()
    st.write(d)


    st.text("markdown example: ")
    st.markdown('Streamlit is **_really_ cool**.')


    st.text("caption example: ")
    st.caption('This is a string that explains something above.')

    st.text("code example:")
    code = '''def hello():
     print("Hello, Streamlit!")'''
    st.code(code, language='python')
    
    st.header('st.checkbox')
    st.write ('What would you like to order?')

    icecream = st.checkbox('Ice cream')
    coffee = st.checkbox('Coffee')
    cola = st.checkbox('Cola')

    if icecream:
        st.write("Great! Here's some more 🍦")
    if coffee: 
        st.write("Okay, here's some coffee ☕")
    if cola:
        st.write("Here you go 🥤")

with col1:
    st.subheader('Subheader: Slider example')
    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')

    st.text("Rangeslider example:")
    values = st.slider('Select a range of values',  0.0, 100.0, (25.0, 75.0))
    st.write('Values:', values)

    st.text("Rangestime example:")
    appointment = st.slider( "Schedule your appointment:", value=(time(11, 30), time(12, 45)))
    st.write("You're scheduled for:", appointment)

    st.text("Dateime example:")
    start_time = st.slider("When do you start?", value=datetime(2020, 1, 1, 9, 30),format="MM/DD/YY - hh:mm")
    st.write("Start time:", start_time)
