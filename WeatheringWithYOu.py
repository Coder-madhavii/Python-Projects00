import requests
import json
import win32com.client as w


while(True):
    if __name__=="__main__":
        speak=w.Dispatch("SAPI.SpVoice")

        city=input("enter the name of the city : ")
    

        url=f"http://api.weatherapi.com/v1/current.json?key=2812516c90884b6597463931241704&q={city}&aqi=no"

        r=requests.get(url)
        weather_dic=json.loads(r.text)
        t=weather_dic["current"]["temp_c"]
        speak.speak(f"The current weather in {city} is {t} celcius")


