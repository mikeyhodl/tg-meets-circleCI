"""
flask app
"""
from flask import Flask

app = Flask('app')

@app.route('/')
def hello_world():
    """
    btc bot
    """
    return '<h1>Hi</h1>'

app.run(host='0.0.0.0', port=8080)
