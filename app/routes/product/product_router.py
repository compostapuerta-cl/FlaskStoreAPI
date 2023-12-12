from flask import request

from . import  product_bp
from app.controllers.products.create_product import CreateProduct
from app.controllers.products.get_products import GetProducts
from app.controllers.products.get_products_by_category import GetProductsByCategory
from app.controllers.products.get_products_by_owner import GetProductsByOwner
from app.controllers.products.delete_product import DeleteProduct

@product_bp.route("/product/<category_name>", methods=["POST","DELETE"])
def post_product(category_name):
    if request.method=="POST":
        create_product=CreateProduct()
        return create_product(request,category_name)
    elif request.method=="DELETE":
        delete_product=DeleteProduct()
        return delete_product(request,category_name)
        
@product_bp.route("/products",methods=["GET"])
def get_products():
    get_products=GetProducts()
    return get_products()
    
@product_bp.route("/products/category/<category_name>",methods=["GET"])
def get_products_by_category(category_name):
    get_products_by_category=GetProductsByCategory()
    return get_products_by_category(category_name)

@product_bp.route("/products/owner/<owner_email>",methods=["GET"])
def get_products_by_owner(owner_email):
    get_products_by_owner=GetProductsByOwner()
    return get_products_by_owner(owner_email)

'''

@product_bp.route("/products/user/join",methods=["GET"])
def get_products_join():
    results=Product.join_user()
    for result in results:
        print(result)
    return {"msg": "printed in console"}

'''