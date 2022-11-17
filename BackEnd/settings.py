import os
import secrets
import datetime
from dotenv import dotenv_values

config = dotenv_values()

config['UPLOAD_FOLDER'] = os.path.dirname(os.path.realpath(__file__)) + r'\images'

JWT_SECRET_KEY = secrets.token_hex(16)
SECRET_KEY = secrets.token_hex(16)
JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=60)
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=60)
CORS_HEADERS = 'Content-Type'
MONGODB_SETTINGS = {
    'host': f"mongodb+srv://{config['user']}:{config['pwd']}@cluster0.geaqzsr.mongodb.net/?retryWrites=true&w=majority"
}
PROPAGATE_EXCEPTIONS = True