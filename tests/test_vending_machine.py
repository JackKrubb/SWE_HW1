import requests

API_ENDPOINT = "http://127.0.0.1:5000/"


def test_get_all_vending_machines():
    all_vending_machines_response = requests.get(API_ENDPOINT + f'{"vending"}')
    assert all_vending_machines_response.status_code == 200
