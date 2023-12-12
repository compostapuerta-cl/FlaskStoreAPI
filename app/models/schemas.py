from app import ma

from .user import User
from .user_info import UserInfo
from .product import Product
from .category import Category

class UserInfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=UserInfo

class UserSchema(ma.SQLAlchemyAutoSchema):
    info = ma.Nested(UserInfoSchema)
    class Meta:
        model=User()
        exclude=("password","active")

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Category

class ProductSchema(ma.SQLAlchemyAutoSchema):
    owner=ma.Nested(UserSchema(only=("name","email")))
    category=ma.Nested(CategorySchema)
    class Meta:
        model=Product