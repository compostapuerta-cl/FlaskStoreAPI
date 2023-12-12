from app.models.user import User
from app.models.category import Category
from app.models.product import Product

from utils.responses import response_message

class CreateProduct:
    
    def __call__(self,request,category_name):

        if request.is_json:

            data = request.get_json()
            owner_email=data['owner_email']
            product_name=data['name']

            owner=User.get_by_email(owner_email)
            category=Category.get_category_by_name(category_name)
            
            if (owner and category):
                if Product.is_product_on_category(Category,product_name,category_name):
                    new_product=Product(
                        name=product_name,
                        price=data['price'],
                        units=data['units'],
                        owner=owner,
                        category=category
                    )          
                    return new_product.save()
                else:
                    return response_message(False, f"Product {product_name} already exists on {category_name}")      
            else:
                return response_message(False, "Owner or category doesn't exist")  
        else:
            return response_message(False, "The request payload is not in JSON format")