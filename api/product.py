from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
product_Ref = db.collection('product')

product = Blueprint('product', __name__)

@product.route('/add', methods=['POST'])
def create():
    try:
        product_Ref.document().set(request.json)
        return jsonify({'success': True}), 200
    except Exception as e:
        return f"An Error Orccured: {e}"

@product.route('/list', methods=['GET'])
def read():
    try:
        all_products = [doc.to_dict() for doc in product_Ref.stream()]
        return jsonify(all_products), 200
    except Exception as e:
        return f"An Error Orccured: {e}"