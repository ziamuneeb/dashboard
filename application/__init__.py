from flask import Flask
from flask_sqlalchemy import SQLAlchemy


pw = '12345678'
url = 'database-todo.cnpkypdmefa8.eu-west-2.rds.amazonaws.com'

app = Flask(__name__)

app.config['SECRET_KEY'] = "1234"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db = SQLAlchemy(app)
db.create_all()

from application import routes
