## Pre-requisites 

1. Python3
2. Install all the dependecies using `pip install -r requirements.txt`

## Running the application on development mode

`python3 src/nrfApp.py`

## Running the tests

`python3 -m pytest tests/`

## Running on docker

```
docker pull quay.io/susdas/nrf_image:latest
docker build -t nrf_image:latest .
docker run -p 5000:5000 -d nrf_image:latest
```
## GET/PUT/DELETE 
```
[GET]
curl -X GET http://localhost:5000/nfprofile/100

[PUT]
curl -d "nfType=UDM&ip=10.10.10.10&port=2000" -X PUT http://localhost:5000/nfprofile/300
curl -d "nfType=UDM&ip=11.11.11.11" -X PUT http://localhost:5000/nfprofile/400

[DELETE]
curl -X DELETE http://localhost:5000/nfprofile/400
```

