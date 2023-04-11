
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Mom\'s New Healthy Diner')


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

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)            
      
except URLError as e:
   streamlit.error()                 


#fruit_choice = streamlit.text_input('What fruit would you like information about?','apple')
#streamlit.write('The user entered ', fruit_choice)


#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)




# uses pandas to return just text without quotation marks, commas, etc.
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# this commands calls the variable listed above and places it in a dataframe/more readerly form
#streamlit.dataframe(fruityvice_normalized)



streamlit.header("View Our Fruit List--Add Your Favorites:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('Get Fruit List'): 
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)



def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('" + new_fruit + "')")
    return "Thanks for adding " + new_fruit
  
add_my_fruit = streamlit.text_input("What fruit would you like to add?")
if streamlit.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit) 
  my_cnx.close()
  streamlit.text(back_from_function)
  
streamlit.stop()

fruit_additions = streamlit.text_input('What fruit would you like information about?')
streamlit.write('Thank you for adding', fruit_additions)


