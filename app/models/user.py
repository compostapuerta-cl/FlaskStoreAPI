from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy import desc
from marshmallow import fields
from datetime import date

from app import db, ma

from .user_info import UserInfo
from utils.validators import validate_user, validate_user_info

class User(db.Model):
    
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    email=db.Column(db.String,nullable=False,unique=True)
    role=db.Column(db.String,nullable=False)
    active=db.Column(db.Boolean,default=True)
    password=db.Column(db.String,nullable=False)

    products=db.relationship(
        'Product',
        back_populates="owner",
        cascade="all, delete, delete-orphan",
        lazy='dynamic'
    )

    info=db.relationship(
        "UserInfo",
        uselist=False,
        back_populates="user",
        cascade='all, delete, delete-orphan',
        lazy="select"
    )

    def __repr___(self):
        return f"{self.id}) {self.name} - {self.email}"

    def save(self,age,job,city,gender):

        if (validate_user(self.name,self.email,self.role,self.active,self.password) 
                and validate_user_info(self.name,age,job,city,gender)):
            try:
                db.session.add(self)
                db.session.flush()

                new_user_info=UserInfo(
                    age=age,
                    gender=gender,
                    job=job,
                    creation_date=date.today(),
                    city=city,
                    user_id=self.id
                )

                db.session.add(new_user_info)
                db.session.commit()
                return True
            except IntegrityError as e:
                print(e)
                db.session.rollback()
                return False
            except DataError as e:
                print(e)
                db.session.rollback()
                return False
        else:
            return False
    
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
    def get_by_email(email):
        user=User.query.filter(User.email==email,User.active==True).first()
        return user
    
    @staticmethod
    def get_users_like(name):
        users=User.query.filter(User.name.ilike(f'%{name}%'),User.active==True).order_by(desc(User.id)).all()
        return users

    @staticmethod
    def get_products_by_user(email):
        user=User.query.filter(User.email==email,User.active==True).first()
        if user:
            products=user.products.all()
            return products
        return False

