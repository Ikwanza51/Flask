from core import app
from flask import render_template

@app.route('/')
def say_hello():
    return render_template('index.html',user={'name':'popinder'})
