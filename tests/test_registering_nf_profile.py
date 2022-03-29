import requests
import pytest

base_url = "http://127.0.0.1:5000/nfprofile/"

@pytest.fixture
def cleanup():
    requests.delete( base_url + "300")
    requests.delete( base_url + "400")
    yield
    requests.delete( base_url + "300")
    requests.delete( base_url + "400")

def test_registering_nf_profile_with_port(cleanup, nf_id="300"):
    data = {'nfType': 'UDM', 'ip': '10.10.10.10', 'port':1000}
    response = requests.put( base_url + nf_id, data)
    assert response.status_code == 201

def test_registering_nf_profile_without_port(cleanup, nf_id="400"):
    data = {'nfType': 'PCF', 'ip': '11.11.11.11'}
    response = requests.put( base_url + nf_id, data)
    assert response.status_code == 201

def test_registering_nf_profile_with_id_which_already_exists(nf_id="100"):
    data = {'nfType': 'PCF', 'ip': '11.11.11.11'}
    response = requests.put( base_url + nf_id, data)
    assert response.status_code == 409
