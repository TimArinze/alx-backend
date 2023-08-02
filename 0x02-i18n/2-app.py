#!/usr/bin/env python3
"""Get locale from request
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """Config Class"""
    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Just rendering the template at /"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
