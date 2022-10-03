import os
from dotenv import dotenv_values

config = dotenv_values(".env")

config['UPLOAD_FOLDER'] = os.path.dirname(os.path.realpath(__file__)) + r'\images'

JWT_SECRET_KEY = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
CORS_HEADERS = 'Content-Type'
MONGODB_SETTINGS = {
    'host': f"mongodb+srv://{config['user']}:{config['pwd']}@cluster0.geaqzsr.mongodb.net/?retryWrites=true&w=majority"
}
PROPAGATE_EXCEPTIONS = True