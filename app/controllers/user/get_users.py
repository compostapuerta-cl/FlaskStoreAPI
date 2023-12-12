from flask import jsonify

from app.models.user import User
from app.models.schemas import UserSchema

class GetUsers:
    def __call__(self):
        query_users=User.query.filter_by(active=True).all()
        user_schema=UserSchema(many=True)
        users=user_schema.dump(query_users)
        return jsonify({'users': users})