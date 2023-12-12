from app.models.user import User
from utils.validators import validate_email
from utils.responses import response_message

class DeleteUser:
    def __call__(self,user_email):
        if not validate_email(user_email):
            return response_message(False, "{user_email} is not a valid email")
        delete_user=User.query.filter_by(active=True,email=user_email).first()
        if delete_user:
            if delete_user.delete():
                return response_message(True, "Successfull delete")
            else:
                return response_message(True, "Couldn't delete {delete_user}")
        else:
            return response_message(False, "Not found user with email {user_email}")