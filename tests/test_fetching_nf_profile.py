import requests
import pytest

base_url = "http://127.0.0.1:5000/nfprofile/"

@pytest.fixture
def setup():
    print("Inside Setup")

def test_fetching_existing_nf_profile(nf_id="100"):
    response = requests.get( base_url + nf_id)
    assert response.status_code == 200

def test_fetching_nf_profile_which_does_not_exist(nf_id="800"):
    response = requests.get( base_url + nf_id)
    assert response.status_code == 404

