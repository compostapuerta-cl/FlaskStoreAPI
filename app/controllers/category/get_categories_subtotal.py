from flask import jsonify

from app.models.category import Category
from app.models.product import Product
from app.models.user import User
from app.models.schemas import CategorySchema

class GetCategoriesSubtotal:

    def __call__(self):
        
        query_categories=Category.get_subtotal_costs_category(Product,User)
        category_schema=CategorySchema(many=True)
        subtotals=category_schema.dump(query_categories)

        for i in range(len(query_categories)):
            subtotals[i]["subtotal"]=query_categories[i][2]

        return jsonify({"Subtotal": subtotals})