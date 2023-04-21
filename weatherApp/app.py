import streamlit as st
import requests 
import json
from json import load
from bs4 import BeautifulSoup



if __name__ == "__main__":
    url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
    st.set_page_config(page_title="Weather App",page_icon='🌤️',layout="centered")
    st.title("Weather App")
    # Rapid Api Request :
    with st.sidebar:
        City = st.text_input("Enter City",help="City Name")
        st.color_picker('pick')
    with open('./style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    # Query :
    querystring = {"city":str(City)}
    # check if the user has entered the city:
    if City !="":
        headers = {
            "X-RapidAPI-Key": "158f334979msh4255f0debf10cb9p1ab5f3jsn2f24021b66fa",
            "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
        }
        # Response :
        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code == requests.codes.ok:
            # st.success(response.status_code)
            data = response.text
            response_dict = json.loads(data)

            # Data :
            cloud_pct = response_dict['cloud_pct']
            temp = response_dict['temp']
            feels_like = response_dict['feels_like']
            humidity = response_dict['humidity']
            min_temp = response_dict['min_temp']
            max_temp = response_dict['max_temp']
            wind_speed = response_dict['wind_speed']
            wind_degrees = response_dict['wind_degrees']
            sunrise = response_dict['sunrise']
            sunset = response_dict['sunset']
            col1, col2, col3 = st.columns(3)
            col1.metric("Temperature", str(temp), "1.2 °F")
            col2.metric("Wind", str(wind_speed), "-8%")
            col3.metric("Humidity", str(humidity), str(wind_degrees)+"°")
        else:
            msg = "Error:"+str(response.status_code)
            st.error(msg)
            exit()
