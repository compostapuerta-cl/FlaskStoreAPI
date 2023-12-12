from flask import jsonify

from app.models.user import User
from app.models.schemas import UserSchema
from utils.responses import response_message

class GetUsersLike:
    def __call__(self,term):
        query_user=User.get_users_like(term)
        if query_user:
            user_schema=UserSchema(many=True)
            user=user_schema.dump(query_user)
            return jsonify({'users': user})
        else:
            return response_message(False, f"No users like {term}")
     