import streamlit 

streamlit.title('What is going on here?')

streamlit.header('Breakfast Favourites')
streamlit.text('🥣 🥗 🐔 🥑🍞')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
