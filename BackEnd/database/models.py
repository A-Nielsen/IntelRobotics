from .db import db
from datetime import datetime
import mongoengine_goodjson as gj
from flask_bcrypt import generate_password_hash, check_password_hash

class User(gj.Document):
    password = db.StringField(required=True, min_length=4)
    email = db.EmailField(required=True, unique=True)
    
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Product(gj.Document):
    name = db.StringField(required=True)
    price = db.DecimalField(required=True, precision=2, min_value=0)
    description = db.StringField()
    imagePath = db.StringField()
    
class Blocked_Tokens(gj.Document):
    jti = db.UUIDField(primary_key=True, required=True, binary=False)
    created = db.DateTimeField(default=datetime.utcnow)