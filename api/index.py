import os
from dotenv import load_dotenv
from api.models import db
from flask import Flask
from flask_migrate import Migrate
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/signup")
def signup():
    # take username and password and create new User in DB
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)