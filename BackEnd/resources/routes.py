from .auth import SignupApi, LoginApi, LogoutApi
from .product import ProductsApi, ProductApi

def initialize_routes(api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(LogoutApi, '/api/auth/logout')
    
    api.add_resource(ProductsApi, '/api/product')
    api.add_resource(ProductApi, '/api/product/<id>')   