from flask import Flask
from flask_restful import Resource, Api, reqparse
import mysqlDB

app = Flask(__name__)
api = Api(app)

db = mysqlDB.open_connection()
cursor = db.cursor()

nf_db = [
        {'nfId': '100', 'nfType': 'AMF', 'ip': '172.30.0.3', 'port': 8001},
        {'nfId': '200', 'nfType': 'SMF', 'ip': '172.30.0.4', 'port': 8002}
]

@app.route('/')
def profiles():
    data = mysqlDB.fetch_all(cursor)
    return data, 200

class NFProfile(Resource):

    def get(self, nf_id):

        # Check if the nfId already exists
        nf_id_list = mysqlDB.get_all_ids(cursor)

        if nf_id not in nf_id_list:
            return { 'message': f"NFID {nf_id} not found" }, 404
        else:
            nf_data = mysqlDB.fetch_with_id(cursor, nf_id)
            return nf_data, 200
        

    def put(self, nf_id):
        parser = reqparse.RequestParser()
        parser.add_argument('nfType', required=True, type=str)
        parser.add_argument('ip', required=True, type=str)
        parser.add_argument('port', required=False, type=int)
        args = parser.parse_args()

        # Check if the nfId already exists
        nf_id_list = mysqlDB.get_all_ids(cursor)

        if nf_id in nf_id_list:
            return { 'message': f"NFID {nf_id} already exists" }, 409
        else:
            # Push the data to the NF DB
            nf_data = (nf_id, args['nfType'], args['ip'], args['port'])
            mysqlDB.insert_data(db, cursor, nf_data)
            return {'message': f"Successfully created the profile"}, 201
    
    def delete(self, nf_id):
        # Check if the nfId exists
        nf_id_list = mysqlDB.get_all_ids(cursor)

        if nf_id not in nf_id_list:
            return { 'message': f"NFID {nf_id} not found" }, 404
        else:
            # Delete the entry from NF DB
            mysqlDB.delete_data(db, cursor, nf_id)
            return {'message' : f"NFID {nf_id} removed successfully"}, 204

if __name__ == '__main__':
    api.add_resource(NFProfile, '/nfprofile/<string:nf_id>')
    app.run(debug=True, host="0.0.0.0")
