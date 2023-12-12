from flask import jsonify

from app.models.product import Product
from app.models.user import User
from app.models.schemas import ProductSchema

'''
We first get categories because we want to 
send products ordered by their categories:
that's why we don't query product but category
'''

class GetProducts:
    def __call__(self):

        query_products=Product.get_products(User)
        products_schema=ProductSchema(many=True)
        products=products_schema.dump(query_products)

        return jsonify({'Products': products})