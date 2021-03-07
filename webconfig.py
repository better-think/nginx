from config import get_config_value
TESTING = False
FLASK_DEBUG = True
UPLOAD_FOLDER = 'uploads'
APP_SECRET = 'iS37^@z8K6dWwmuWQY'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = get_config_value('database', 'uri')
DEFAULT_LOCALE='en'
APPLICATION_ROOT="/recipe"