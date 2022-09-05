from flask import Flask
import firebase_admin
from firebase_admin import credentials, initialize_app

if not firebase_admin._apps:
    cred = credentials.Certificate(r'api/key.json')
    default_app = initialize_app(cred)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] =  "Test123"
    
    from .product import product
    
    app.register_blueprint(product, url_prefix='/product')
    
    return app