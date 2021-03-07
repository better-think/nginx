from flask import Flask, session
from flask_babel import Babel
from webconfig import APP_SECRET
from apps.foods import foods_page
from apps.users import users_page, login_manager
from apps import helper
from apps.helper import current_language
from db import db
app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = APP_SECRET
app.config.from_pyfile('webconfig.py')
app.register_blueprint(foods_page)
app.register_blueprint(users_page)
app.jinja_env.filters['trans_val'] = helper.trans_val
app.jinja_env.filters['format_number'] = helper.format_number
app.jinja_env.filters['format_date'] = helper.format_date
db.init_app(app)
login_manager.init_app(app)
babel = Babel(app)
@babel.localeselector
def get_locale():
    return current_language()
@app.context_processor
def inject_locale():
    return {'current_language': get_locale()}