#!/usr/bin/env python3
"""Basic Babel setup
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)


class Config(object):
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def index():
    """Just rendering the template at /"""
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(debug=True)
