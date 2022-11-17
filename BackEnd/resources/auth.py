from flask import request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from database.models import User, Blocked_Tokens
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, DoesNotExist, ValidationError

class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user =  User(**body)
            user.hash_password()
            user.save()
            token = create_access_token(identity=str(user.id))
            return {'token': token}, 200
        
        except FieldDoesNotExist as e:
            return str(e), 400 
        except ValidationError:
            return "Email/Username is already used or email is formatted incorrectly", 400
        except Exception:
            return "An unexpected error has occurred", 500
        
        
class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                return "Unauthorized", 401
    
            token = create_access_token(identity=str(user.id))
            return {'token': token}, 200
        
        except DoesNotExist:
            return "Unauthorized", 401
        except Exception:
            return "An unexpected error has occurred", 500
        
        
class LogoutApi(Resource):
    @jwt_required()
    def delete(self):
        try:
            jti = get_jwt()["jti"]
            Blocked_Tokens(jti=jti).save()

            return 'Token revoked', 200
        
        except Exception:
            return "An unexpected error has occurred", 500