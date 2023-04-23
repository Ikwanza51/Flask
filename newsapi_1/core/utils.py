import requests #for getting requests from api
from decouple import config # To use environment variable

Newsapi = config('News_Api_Key')
Country = 'in'

def get_latest_news():
    news_data = requests.get('https://newsapi.org/v2/top-headlines?country={Country}&apiKey={Newsapi}').json()
    print(type(news_data))
    return news_data["articles"]