## Pre-requisites 

1. Python3
2. Install all the dependecies using `pip install -r src/requirements.txt`

## Running the application on development mode

`python3 nrfApp.py`

## PUT/DELETE 
```
[PUT]
curl -d "nfId=300&nfType=UDM&ip=10.10.10.10&port=2000" -X PUT http://localhost:5000/nfprofile
curl -d "nfId=400&nfType=UDM&ip=11.11.11.11" -X PUT http://localhost:5000/nfprofile

[DELETE]
curl -d "nfId=400" -X DELETE http://localhost:5000/nfprofile
```

