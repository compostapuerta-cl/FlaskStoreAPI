import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv

db=SQLAlchemy()
ma = Marshmallow()

swagger_url='/swagger'
api_url='/static/flask_store.yaml'

def create_app():

    app=Flask(__name__)

    load_dotenv()   
    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("DATABASE")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['DEBUG']=True
    
    db.init_app(app)
    ma.init_app(app)

    migrate=Migrate(app,db)
    manager=Manager(app)

    from .routes.user import user_bp
    app.register_blueprint(user_bp)

    from .routes.product import product_bp
    app.register_blueprint(product_bp)

    from .routes.category import category_bp
    app.register_blueprint(category_bp)

    swagger_bp=get_swaggerui_blueprint(
        swagger_url,
        api_url,
        config={
            'app_name': "Flask-StoreAPI"
        }
    )

    app.register_blueprint(swagger_bp,url_prefix=swagger_url)

    migrate.init_app(app,db)
    manager.add_command('db',MigrateCommand)

    return manager