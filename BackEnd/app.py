import logging
from datetime import date
from flask import Flask
from database.db import initialize_db
from resources.routes import initialize_routes
from database.models import Blocked_Tokens
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

logging.basicConfig(filename=f'logs\{date.today()}.log', level=logging.DEBUG)
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config.from_pyfile('settings.py')

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
    
initialize_db(app)
initialize_routes(api)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]

    if Blocked_Tokens.objects(jti=jti):
        return True
    else:
        return False

app.run(host="0.0.0.0")








