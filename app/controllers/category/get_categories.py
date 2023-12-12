from flask import jsonify

from app.models.category import Category
from app.models.schemas import CategorySchema

class GetCategories:

    def __call__(self):

        query_categories=Category.get_categories()
        category_schema=CategorySchema(many=True)
        categories=category_schema.dump(query_categories)

        return jsonify({"categories": categories})