from flask.testing import FlaskClient

API_ENDPOINT = "http://127.0.0.1:5000/"


def test_all_vending_purchase(client: FlaskClient):
    test_body = {"vending_id": 3}
    all_vending_purchase_response = client.get(API_ENDPOINT + f'{"purchase/vending"}', data=test_body)
    assert all_vending_purchase_response.status_code == 200


def test_all_product_purchase(client: FlaskClient):
    test_body = {"product_id": 1}
    all_product_purchase_response = client.get(API_ENDPOINT + f'{"purchase/product"}', data=test_body)
    assert all_product_purchase_response.status_code == 200
