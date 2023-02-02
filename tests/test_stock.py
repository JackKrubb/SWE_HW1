from flask import Flask
from flask.testing import FlaskClient

API_ENDPOINT = "http://127.0.0.1:5000/"
STOCK_ERROR = "Stock error."
INVALID_NUMBER_MSG = "Invalid number, please input the correct input"


def test_all_stock(app2: Flask, client: FlaskClient):
    with app2.app_context():
        all_stock_response = client.get(API_ENDPOINT + f'{"stock"}')
        assert all_stock_response.status_code == 200


def test_one_stock(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"stocking_id": 1}
        one_stock_response = client.get(API_ENDPOINT + f'{"stock/single"}', data=test_body)
        assert one_stock_response.status_code == 200


def test_one_stock_one_vend(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"vending_id": 1, "product_id": 1}
        one_stock_one_vend_response = client.get(API_ENDPOINT + f'{"stock/single-stock"}', data=test_body)
        assert one_stock_one_vend_response.status_code == 200


def test_all_stock_one_vend(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"vending_id": 1}
        all_stock_one_vend_response = client.get(API_ENDPOINT + f'{"stock/single-vend"}', data=test_body)
        assert all_stock_one_vend_response.status_code == 200


def test_add_stock(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"vending_id": 1, "product_id": 1, "product_amount": 20}
        added_stock_response = client.post(API_ENDPOINT + f'{"stock/add-stock"}', data=test_body)
        assert added_stock_response.status_code == 200
        added_stock_response_json = added_stock_response.json
        if added_stock_response_json["message"] == STOCK_ERROR:
            assert added_stock_response_json["success"] is False
        else:
            assert added_stock_response_json["success"] is True


def test_add_stock2(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_invalid_body = {"vending_id": 1, "product_id": 1, "product_amount": "'chips'"}
        added_stock_response2 = client.post(API_ENDPOINT + f'{"stock/add-stock"}', data=test_invalid_body)
        added_stock_response2_json = added_stock_response2.json
        assert added_stock_response2_json["success"] is False


def test_add_stock3(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_invalid_body = {"vending_id": 10000, "product_id": 1, "product_amount": 15}
        added_stock_response3 = client.post(API_ENDPOINT + f'{"stock/add-stock"}', data=test_invalid_body)
        added_stock_response3_json = added_stock_response3.json
        if added_stock_response3_json["message"] == STOCK_ERROR:
            assert added_stock_response3_json["success"] is False
        else:
            assert added_stock_response3_json["success"] is True


def test_add_stock4(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_invalid_body = {"vending_id": 1, "product_id": 10000, "product_amount": 15}
        added_stock_response4 = client.post(API_ENDPOINT + f'{"stock/add-stock"}', data=test_invalid_body)
        added_stock_response4_json = added_stock_response4.json
        if added_stock_response4_json["message"] == STOCK_ERROR:
            assert added_stock_response4_json["success"] is False
        else:
            assert added_stock_response4_json["success"] is True


def test_edit_stock(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"stocking_id": 1, "product_amount": 15}
        edited_stock_response = client.post(API_ENDPOINT + f'{"stock/edit-stock"}', data=test_body)
        assert edited_stock_response.status_code == 200
        edited_stock_response_json = edited_stock_response.json
        if edited_stock_response_json["message"] == STOCK_ERROR:
            assert edited_stock_response_json["success"] is False
        else:
            assert edited_stock_response_json["success"] is True


def test_edit_stock2(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_invalid_body = {"stocking_id": 1, "product_amount": "'chips'"}
        edited_stock_response2 = client.post(API_ENDPOINT + f'{"stock/edit-stock"}', data=test_invalid_body)
        edited_stock_response2_json = edited_stock_response2.json
        assert edited_stock_response2_json["success"] is False


def test_delete_stock(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"stocking_id": 1}
        deleted_stock_response = client.post(API_ENDPOINT + f'{"stock/delete-stock"}', data=test_body)
        assert deleted_stock_response.status_code == 200
        deleted_stock_response_json = deleted_stock_response.json
        if deleted_stock_response_json["message"] == STOCK_ERROR:
            assert deleted_stock_response_json["success"] is False
        else:
            assert deleted_stock_response_json["success"] is True
