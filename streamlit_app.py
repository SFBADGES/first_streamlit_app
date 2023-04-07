
import streamlit
streamlit.title('My Mom\'s New Healthy Diner')

import streamlit
streamlit.header('Breakfast Favorites')

streamlit.text(' 🍚Omega 3 & Blue Berry Oatmeal')
streamlit.text(' 🧋 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🍞Avocado Toast')
streamlit.header('🍌 🍓Build Your Own Fruit Smoothie🥝🍇 ')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), key = 'Lime')
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','apple')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# uses pandas to return just text without quotation marks, commas, etc.
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# this commands calls the variable listed above and places it in a dataframe/more readerly form
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
fruit_additions = streamlit.text_input('What fruit would you like information about?')
streamlit.write('The user entered ', fruit_additions)
