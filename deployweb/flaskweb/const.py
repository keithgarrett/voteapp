from flask import Flask, abort, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app, prefix="/elections")

consts = [
    {"const": "Cambridge", "parties": {1:"Rebooting Democracy", 2: "Labour"}, "postcode": "CAM1"},
    {"const": "Manchester", "parties": {"Labour, Green", "postcode": "MANC1"},
]

def get_const_by_postcode(postcode):
    for x in consts:
        if x.get("postcode") == postcode:
            return x

class Consts(Resource):
    def get(self):
        return { 'consts': consts}

class Const(Resource):
    #def get(self, postcode):
    def get(self):
        postcode = request.args.get('p');
        const = get_const_by_postcode(postcode)
        if not const:
            return {"error": "Constituency not found"}
        return const


api.add_resource(Const,'/postcode')
#api.add_resource(Const,'/postcode/<postcode>')
api.add_resource(Consts,'/consts')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


#from flask import Flask
#app = Flask(__name__)
#
#@app.route("/const")
#def hello():
#    return "Hello World!"

