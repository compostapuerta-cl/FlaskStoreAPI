from sqlalchemy.exc import IntegrityError
from marshmallow import fields

from app import db, ma

from utils.validators import validate_product
from utils.responses import response_message

class Product(db.Model):
    
    __tablename__='products'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    price=db.Column(db.Float,nullable=False)
    units=db.Column(db.Integer,nullable=False)

    owner_id=db.Column(db.Integer,db.ForeignKey('users.id',ondelete='cascade'))
    owner=db.relationship("User", back_populates="products")

    category_id=db.Column(db.Integer,db.ForeignKey('categories.id',ondelete='cascade'))
    category=db.relationship("Category", back_populates="products")

    def __repr__(self):
        return f'{self.id}) {self.name}: ${self.price} - {self.units} unit(s)'
    
    def save(self):
        if validate_product(self.name,self.price,self.units):
            try:
                db.session.add(self)    
                db.session.commit()
                return response_message(True, f"product {self.name} has been created successfully.")
            except IntegrityError as e:
                db.session.rollback()
                return {
                    "ok": False,
                    "message": f"product {self.name} couldn't be created",
                    "errors": e
                }
        else:
            return response_message(False, f"product {self.name} could not be created")
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except IntegrityError as e:
            print(e)
            db.session.rollback()
            return False
    
    @staticmethod
    def get_products(User):
        products=Product.query.filter(User.active==True).join(User).order_by(Product.id)          
        return products
    
    @staticmethod
    def get_products_by_category(Category,User,category_name):
        products=Product.query.filter(Category.name==category_name,User.active==True)\
                    .join(User).join(Category)
        return products

    '''
    This query returns, using a join between category and products,
    the products whose name is equal to product_name. If the name is equal,
    then the product will not be created because the product.name have to be unique
    within every category.
    '''
    @staticmethod
    def get_product_on_category(Category,product_name,category_name):
        products=Product.query.filter(Category.name==category_name,
                    Product.name==product_name)\
                    .join(Category).first()
        return products
        
    @staticmethod
    def is_product_on_category(Category,product_name,category_name):
        products=Product.get_product_on_category(Category,product_name,category_name)             
        if not products:
            return True 
        else:
            return False