import json
import requests
from win32com.client import Dispatch
def speak(str):
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("hello world")
    # url="https://newsapi.org/v2/top-headlines?country=in&apiKey=ca62a849cde14140a6769c45be203483"
    # news=requests.get(url).text
    # news=json.loads(news)
    # articles_list=news["articles"]
    # for articles in articles_list:
    #     print("Description:"+articles["description"])
    #     print("URL:"+articles["url"])
    #     speak(articles["description"])

