import sys
sys.path.append("..")

import os
import uuid
from flask import Response, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from database.models import Product
from werkzeug.datastructures import FileStorage
from mongoengine.errors import FieldDoesNotExist
from settings import config

class ProductsApi(Resource):
    def get(self):
        try:
            products = Product.objects().to_json()
            return Response(products, mimetype="application/json", status=200)
        except Exception:
            return "An unexpected error has occurred", 500

    @jwt_required()
    def post(self):  
        try:
            parse = reqparse.RequestParser()
            parse.add_argument('img', type=FileStorage, location='files')
            parse.add_argument('name', type=str, location='form')
            parse.add_argument('price', type=float, location='form')
            parse.add_argument('description', type=str, location='form')
            
            body = {}
            
            args = parse.parse_args() 
            
            if args['img']:
                imgId = str(uuid.uuid1()) + '.png'
                img = args['img']
                path = os.path.join(config['UPLOAD_FOLDER'], imgId)
                img.save(path)
                body['imagePath'] = path
            
            body['name'] = args['name']
            body['price'] = args['price']
            body['description'] = args['description']
            
            
            product = Product(**body).save()
            
            return {'id': str(product.id)}, 200
        
        except FieldDoesNotExist as e:
            return str(e), 400 
        except Exception as e:
            return f"An unexpected error has occurred: {e}", 500

class ProductApi(Resource):
    def get(self, id):
        try:
            product = Product.objects.get(id=id).to_json()
            return Response(product, mimetype="application/json", status=200)
        except Exception:
            return "An unexpected error has occurred", 500

    @jwt_required()
    def put(self, id):
        try:
            body = request.get_json()
            Product.objects.get(id=id).update(**body)
            return 'OK', 200
        
        except FieldDoesNotExist as e:
            return str(e), 400 
        except Exception:
            return "An unexpected error has occurred", 500
            
    @jwt_required()
    def delete(self, id):
        try:
            Product.objects.get(id=id).delete()
            return 'OK', 200
        except Exception:
            return "An unexpected error has occurred", 500