from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required
from user import UserRegister, authenticate, identity



app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'super-secret'
jwt = JWT(app=app, authentication_handler=authenticate, identity_handler= identity)

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run()