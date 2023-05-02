import requests #for getting requests from api
from decouple import config # To use environment variable
import json

Newsapi = config('News_Api_Key')
Country = 'in'

def get_latest_news():
    # news_data = requests.get('https://newsapi.org/v2/top-headlines?country={Country}&apiKey={Newsapi}').json()
    news_data = requests.get('https://newsapi.org/v2/top-headlines?country={Country}&apiKey=7811516491a4458e993e9bb0c9e1860e').json()
    if(news_data['status'] == 'ok'):
        return news_data
    # news_data = json.load(news_data)
    return "Error"