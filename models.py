

from datetime import datetime

from flask import current_app

from flask_sqlalchemy import SQLAlchemy






db = SQLAlchemy()



 


class User(  db.Model ):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(100))
    
    email = db.Column(db.String(100), default=None)

    phone_number = db.Column(db.String(10))

    birth_day = db.Column(db.DateTime)

    password = db.Column(db.String(200))






