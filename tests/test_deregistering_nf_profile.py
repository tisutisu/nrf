import requests
import pytest

base_url = "http://127.0.0.1:5000/nfprofile/"

@pytest.fixture
def cleanup():
    yield
    data = {'nfType': 'AMF', 'ip': '172.30.0.3', 'port': 8001}
    requests.put( base_url + "100", data)

def test_deregistering_nf_profile_when_exists(cleanup, nf_id="100"):
    response = requests.delete( base_url + nf_id)
    assert response.status_code == 204

def test_deregistering_nf_profile_which_does_not_exists(nf_id="1100"):
    response = requests.delete( base_url + nf_id)
    assert response.status_code == 404
