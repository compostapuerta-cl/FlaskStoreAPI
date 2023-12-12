from app import db, ma

class UserInfo(db.Model):
    
    __tablename__="users_info"

    id=db.Column(db.Integer,primary_key=True)
    gender=db.Column(db.String,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    creation_date=db.Column(db.Date,nullable=False)
    job=db.Column(db.String,nullable=False)
    city=db.Column(db.String,nullable=False)

    user_id=db.Column(db.Integer,db.ForeignKey('users.id',ondelete='cascade'),unique=True)
    user=db.relationship("User", back_populates="info")    