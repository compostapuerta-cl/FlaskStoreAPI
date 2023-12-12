from flask import jsonify

from app.models.user import User
from app.models.schemas import UserSchema

from utils.validators import validate_email
from utils.responses import  response_message

class GetUser:
    def __call__(self,user_email):

        if validate_email(user_email):
            query_user=User.query.filter_by(active=True,email=user_email).first()
            if query_user:
                user_schema=UserSchema()
                user=user_schema.dump(query_user)
                return jsonify({'user': user})
            else:
                return response_message(False, f"{user_email} doesn't exists")
        else:
            return response_message(False, f"{user_email} is not a valid email")