from flask import jsonify

from app.models.user import User
from app.models.schemas import ProductSchema
from utils.validators import validate_email

class GetProductsByOwner:

    def __call__(self,owner_email):

        if validate_email(owner_email):
            query_products=User.get_products_by_user(owner_email)
            if not query_products:
                return {"message": f"{owner_email} doesn't have products yet"}
            else:
                product_schema=ProductSchema(many=True,exclude=("owner",))
                products=product_schema.dump(query_products)
                return jsonify({"Products": products})
        else:
            return jsonify({"message": f"{owner_email} is not a valid email"})