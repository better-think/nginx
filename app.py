from flask import Flask, session
from flask_babel import Babel
from webconfig import APP_SECRET
from apps.foods import foods_page
from apps.users import users_page, login_manager
from apps import helper
from apps.helper import current_language
from db import db
# from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.middleware.dispatcher import DispatcherMiddleware


app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = APP_SECRET
app.config["APPLICATION_ROOT"] = "/recipe"
app.config.from_pyfile('webconfig.py')
app.wsgi_app = DispatcherMiddleware(simple, {'/recipe': app.wsgi_app})

app.jinja_env.filters['trans_val'] = helper.trans_val
app.jinja_env.filters['format_number'] = helper.format_number
app.jinja_env.filters['format_date'] = helper.format_date


def simple(env, resp):
    resp(b'200 OK', [(b'Content-Type', b'text/plain')])
    return [b'Hello WSGI World']


app.register_blueprint(foods_page)
app.register_blueprint(users_page)

db.init_app(app)
login_manager.init_app(app)
babel = Babel(app)
@babel.localeselector
def get_locale():
    return current_language()
@app.context_processor
def inject_locale():
    return {'current_language': get_locale()}