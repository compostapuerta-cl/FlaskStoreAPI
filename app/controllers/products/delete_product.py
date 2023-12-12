from app.models.product import Product
from app.models.category import Category
from utils.responses import response_message

class DeleteProduct:
    def __call__(self,request,category_name):

        if not request.is_json:
            return response_message(False, "The request payload is not in JSON format")
               
        product_name=request.json["product_name"]
        delete_product=Product.get_product_on_category(Category,product_name,category_name)
        if delete_product:
            if delete_product.delete():
                return response_message(True, "Successfull delete")
            else:
                return response_message(False, "Couldn't delete {product_name}")
        else:
            return response_message(True, f'Product {product_name} from category {category_name} not found')