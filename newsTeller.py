import json
import requests_with_caching
import requests
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("hello world")
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=ca62a849cde14140a6769c45be203483"
    news=requests_with_caching.get(url,temp_cache_file="newTeller.txt").text
    news=json.loads(news)
    print(news["status"])