from flask import Flask
from flask_restful import Resource, Api, reqparse

nf_db = [
        {'nfId': '100', 'nfType': 'AMF', 'ip': '172.30.0.3', 'port': 8001},
        {'nfId': '200', 'nfType': 'SMF', 'ip': '172.30.0.4', 'port': 8002}
]

def remove_entry(nf_db, nf_id):
    for i in range(len(nf_db)):
        if nf_db[i]['nfId'] == nf_id:
            del nf_db[i]
            return

def get_entry(nf_db, nf_id):
    for i in range(len(nf_db)):
        if nf_db[i]['nfId'] == nf_id:
            return nf_db[i]
            
class NFProfile(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nfId', required=True, type=str)
        parser.add_argument('nfType', required=True, type=str)
        parser.add_argument('ip', required=True, type=str)
        parser.add_argument('port', required=False, type=int)
        args = parser.parse_args()

        # Check if the nfId already exists
        nf_id_list = list(map(lambda x: x['nfId'], nf_db))

        if args['nfId'] in nf_id_list:
            return { 'message': f"NFID {args['nfId']} already exists" }, 409
        else:
            # Push the data to the NF DB
            nf_data = {'nfId': args['nfId'], 'nfType': args['nfType'], 'ip': args['ip'], 'port': args['port']}
            nf_db.append(nf_data)
            return nf_data, 200
    
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nfId', required=True, type=str)
        args = parser.parse_args()

        # Check if the nfId exists
        nf_id_list = list(map(lambda x: x['nfId'], nf_db))

        if args['nfId'] not in nf_id_list:
            return { 'message': f"NFID {args['nfId']} not found" }, 404
        else:
            # Delete the entry from NF DB
            remove_entry(nf_db, args['nfId'])
            return {'message' : f"NFID {args['nfId']} removed successfully"}, 200


if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(NFProfile, '/nfprofile')
    app.run(debug=True)
