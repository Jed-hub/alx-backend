#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, g, request, render_template
from flask_babel import Babel, _
from typing import Union


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    Configuration of available languages in the app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request(login_as: int = None):
    """
    Before other functions
    """
    user: dict = get_user()
    print(user)
    g.user = user


def get_user() -> Union[dict, None]:
    """
    Return user from the dict
    """
    login_user = request.args.get('login_as', None)

    if login_user is None:
        return None

    user: dict = {}
    user[login_user] = users.get(int(login_user))

    return user[login_user]


@babel.localeselector
def get_locale():
    """
    Determine the best match with our supported language
    """
    locale = request.args.get('locale', None)

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """
    Hello world
    """
    login = False
    if g.get('user') is not None:
        login = True

    return render_template('5-index.html', login=login)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
