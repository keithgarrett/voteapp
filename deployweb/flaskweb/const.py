from flask import Flask, abort
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

users = [
    {"email": "john@gmail.com", "name": "John", "id": 1},
    {"email": "george@gmail.com", "name": "george", "id": 2},
    {"email": "nick@gmail.com", "name": "nick", "id": 3},
]

def get_user_by_id(user_id):
    for x in users:
        if x.get("id") == int(user_id):
            return x

class Users(Resource):
    def get(self):
        return { 'users': users}

class User(Resource):
    def get(self, id):
        user = get_user_by_id(id)
        if not user:
            return {"error": "User not found"}
        return user


api.add_resource(User,'/user/<int:id>')
api.add_resource(Users,'/users')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


#from flask import Flask
#app = Flask(__name__)
#
#@app.route("/const")
#def hello():
#    return "Hello World!"

