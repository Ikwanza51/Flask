from core import app
from flask import render_template
from .utils import get_latest_news

@app.route('/')
def say_hello():
    return render_template('index.html',user={'name':'popinder'})

@app.route('/news_latest')
def news():
    newsArticles=get_latest_news()
    print(newsArticles)
    # print(newsArticles['articles'])
    return "Positive"
    # return render_template('news.html',news_articles=news)