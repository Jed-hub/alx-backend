#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


class Config(object):
    """
    Configuration of available languages in the app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'

@app.route('/', strict_slashes=False)
def hello_world():
    """
    Hello world
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
