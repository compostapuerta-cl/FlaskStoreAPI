from flask import request

from . import category_bp

from app.controllers.category.create_category import CreateCategory
from app.controllers.category.get_categories import GetCategories
from app.controllers.category.get_categories_subtotal import GetCategoriesSubtotal

@category_bp.route("/category",methods=["POST"])
def post_category():
    create_category=CreateCategory()
    return create_category(request)

@category_bp.route("/categories",methods=["GET"])
def get_categories():
    get_categories=GetCategories()
    return get_categories()

@category_bp.route("/categories/subtotal",methods=["GET"])
def get_categories_subtotal():
    get_categories_subtotal=GetCategoriesSubtotal()
    return get_categories_subtotal()