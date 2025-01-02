import streamlit
import requests
import json

def inspire():
  response = requests.get("https://zenquotes.io/api/random")
  responseData = json.loads(response.text)
  quote = "'" + responseData[0]['q'] + "' - " + responseData[0]['a']
  return quote

streamlit.set_page_config(page_title="StayZen", page_icon="🧘‍♂️")
streamlit.title("StayZen")
streamlit.write("## Random quotes 😊")
streamlit.write("## " + inspire())

if streamlit.button("Inspire me!"):
  streamlit.rerun()