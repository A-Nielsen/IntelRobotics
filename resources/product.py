from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from database.models import Product

class ProductsApi(Resource):
    def get(self):
        products = Product.objects().to_json()
        return Response(products, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):  
        try:
            body = request.get_json()
            product = Product(**body).save()
        
            return {'id': str(product.id)}, 200
        except Exception as e:
            return f"An Error Orccured: {e}"

class ProductApi(Resource):
    def get(self, id):
        try:
            product = Product.objects.get(id=id).to_json()
            return Response(product, mimetype="application/json", status=200)
        except Exception as e:
            return f"An Error Orccured: {e}"

    @jwt_required()
    def put(self, id):
        try:
            body = request.get_json()
            Product.objects.get(id=id).update(**body)
            return 'OK', 200
        except Exception as e:
            return f"An Error Orccured: {e}"
            
    @jwt_required()
    def delete(self, id):
        try:
            Product.objects.get(id=id).delete()
            return 'OK', 200
        except Exception as e:
            return f"An Error Orccured: {e}"