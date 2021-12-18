import psycopg2
from flask import Flask, abort, request
from flask_restful import Api, Resource

connection = psycopg2.connect(user="postgres",
                          password="postgres",
                          host="db",
                          port="5432",
                          database="postcodes")

cur = connection.cursor()

app = Flask(__name__)

@app.route('/vote', methods=['POST'])
def vote():
    email = request.form.get('email')
    postcode = request.form.get('postcode')
    vote = request.form.get('vote')
    election_code = request.form.get('election_code')


    print ("Got email:" + email )
    print ("Got postcode:" + postcode )
    print ("Got election_code:" + election_code )
    print ("Got vote:" + vote )
    return 'Hello World!'

@app.route('/elections/postcode', methods=['GET'])
def contacts():
    postcode = str(request.args.get('p'))
    print(postcode)
    try:
        #Get the constituency
        cur.execute("""select postcode, constituency_code, constituency_name from postcodes LEFT OUTER  JOIN constituencies ON (postcodes.constituency = constituency_code) where postcode=%s LIMIT 1""", (postcode,))
        rows = cur.fetchall()
        #my_list = []
        #for row in rows:
        #    my_list.append(row[2])
        row = rows[0]
        concode = str(row[1])
        myreturn={"postcode":str(row[0]),
                  "concode":str(row[1]),
                  "con":str(row[2])}

        # Get the list of elections and then parties
        cur.execute("""select election_code, election_name from elections where constituency_code=%s;""", (concode,))
        election_rows = cur.fetchall()
        elections = {}
        for election in election_rows:
            electiondict = {}
            electiondict["name"]=election[1]
            electiondict["code"]=election[0]
            cur.execute("""select parties.party_code,party_name from parties INNER JOIN partieslink ON parties.party_code = partieslink.party_code INNER JOIN elections ON elections.election_code = partieslink.election_code where elections.election_code=%s;""", (election[0],))
            parties_rows = cur.fetchall()
            parties = {}
            for party in parties_rows:
                parties[party[0]] = party[1]
                
            electiondict["parties"]=parties

        myreturn["elections"] = electiondict
        print (myreturn)
            


        return myreturn
    except Exception as e:
        print (e)
        return []

if __name__ == '__main__':
    app.run()



#cursor = connection.cursor()
#
#app = Flask(__name__)
#api = Api(app, prefix="/elections")
#
#api.add_resource(Const,'/postcode')
#
#
#
#
#
#consts = [
#    {"const": "Cambridge", "parties": {1:"Rebooting Democracy", 2: "Labour"}, "postcode": "CAM1"},
#    {"const": "Manchester", "parties": {1:"Labour", 2: "Green"}, "postcode": "MANC1"} ]
#
#def get_const_by_postcode(postcode):
#    try:
#        print("Connected to DB")
#    except (Exception, psycopg2.Error) as error:
#        print("Error while fetching data from PostgreSQL", error)
##    for x in consts:
##        if x.get("postcode") == postcode:
##            return x
#
#class Consts(Resource):
#    def get(self):
#        return { 'consts': consts}
#
#class Const(Resource):
#    #def get(self, postcode):
#    def get(self):
#        postcode = request.args.get('p');
#        const = get_const_by_postcode(postcode)
#        if not const:
#            return {"error": "Constituency not found"}
#        return const
#
#
##    api.add_resource(Consts,'/consts')
#
#if __name__ == '__main__':
#    api.run(debug=True, host='0.0.0.0')
#


