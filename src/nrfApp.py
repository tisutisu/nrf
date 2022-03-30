from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

nf_db = [
        {'nfId': '100', 'nfType': 'AMF', 'ip': '172.30.0.3', 'port': 8001},
        {'nfId': '200', 'nfType': 'SMF', 'ip': '172.30.0.4', 'port': 8002}
]

@app.route('/')
def profiles():
    profiles = {}
    for nf_data in nf_db:
        nf_id = get_value_from_dict_except_key(nf_data, 'nfId')
        profiles[nf_id] = nf_data
    return profiles

def get_value_from_dict_except_key(dictionary, key):
    new_dict = {}
    for k, v in dictionary.items():
        if k == key:
            value = dictionary[key]
        else:
            new_dict[k] = v
    return value

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

    def get(self, nf_id):

        # Check if the nfId already exists
        nf_id_list = list(map(lambda x: x['nfId'], nf_db))

        if nf_id not in nf_id_list:
            return { 'message': f"NFID {nf_id} not found" }, 404
        else:
            nf_data = get_entry(nf_db, nf_id)
            return nf_data, 200
        

    def put(self, nf_id):
        parser = reqparse.RequestParser()
        parser.add_argument('nfType', required=True, type=str)
        parser.add_argument('ip', required=True, type=str)
        parser.add_argument('port', required=False, type=int)
        args = parser.parse_args()

        # Check if the nfId already exists
        nf_id_list = list(map(lambda x: x['nfId'], nf_db))

        if nf_id in nf_id_list:
            return { 'message': f"NFID {nf_id} already exists" }, 409
        else:
            # Push the data to the NF DB
            nf_data = {'nfId': nf_id, 'nfType': args['nfType'], 'ip': args['ip'], 'port': args['port']}
            nf_db.append(nf_data)
            return nf_data, 201
    
    def delete(self, nf_id):
        # Check if the nfId exists
        nf_id_list = list(map(lambda x: x['nfId'], nf_db))

        if nf_id not in nf_id_list:
            return { 'message': f"NFID {nf_id} not found" }, 404
        else:
            # Delete the entry from NF DB
            remove_entry(nf_db, nf_id)
            return {'message' : f"NFID {nf_id} removed successfully"}, 204

if __name__ == '__main__':
    api.add_resource(NFProfile, '/nfprofile/<string:nf_id>')
    app.run(debug=True, host="0.0.0.0")
