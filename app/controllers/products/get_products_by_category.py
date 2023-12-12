from flask import jsonify

from app.models.user import User
from app.models.product import Product
from app.models.category import Category
from app.models.schemas import ProductSchema

from utils.validators import validate_category
from utils.responses import response_message

class GetProductsByCategory:

    def __call__(self,category_name):
        if validate_category(category_name):
            query_products=Product.get_products_by_category(Category,User,category_name).all()
            if query_products:
                product_schema=ProductSchema(many=True,exclude=("category",))
                products_by_category=product_schema.dump(query_products)
                return jsonify({"Products": products_by_category})
            else:
                return response_message(False, f"Category {category_name} doesn't exist or doesn't have products yet")
        else:
            return response_message(False, f"{category_name} is not a valid category")