import os
from dotenv import load_dotenv
from api.models import db, User
from flask import Flask, request
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bcrypt = Bcrypt(app)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/signup", methods=['POST'])
def signup():
    hash: bytes = bcrypt.generate_password_hash(str(request.form['password'])) # type: ignore
    user = User(
        username=request.form['username'],
        pw_hash=hash
    )
    db.session.add(user)
    db.session.commit()
    return "<p>User created!</p>"

if __name__ == '__main__':
    app.run(debug=True)