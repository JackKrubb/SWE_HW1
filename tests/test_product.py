from flask import Flask
from flask.testing import FlaskClient

API_ENDPOINT = "http://127.0.0.1:5000/"
PRODUCT_DOES_NOT_EXIST = "Product does not exist."


def test_all_product(app2: Flask, client: FlaskClient):
    with app2.app_context():
        all_product_response = client.get(API_ENDPOINT + f'{"product"}')
        assert all_product_response.status_code == 200


def test_one_product(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"product_id": 1}
        one_product_response = client.get(API_ENDPOINT + f'{"product/single"}', data=test_body)
        assert one_product_response.status_code == 200


def test_edit_product(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"product_name": "'chips'", "product_price": 15, "product_id": 1}
        edited_product_response = client.post(API_ENDPOINT + f'{"product/edit-product"}', data=test_body)
        assert edited_product_response.status_code == 200
        edited_product_response_json = edited_product_response.json
        if edited_product_response_json["message"] == PRODUCT_DOES_NOT_EXIST:
            assert edited_product_response_json["success"] is False
        else:
            assert edited_product_response_json["success"] is True


def test_edit_product2(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"product_name": "'chips'", "product_id": 1}
        edited_product_response = client.post(API_ENDPOINT + f'{"product/edit-product"}', data=test_body)
        edited_product_response_json = edited_product_response.json
        assert edited_product_response_json["success"] is False


def test_add_product(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"product_name": "'chips'", "product_price": 15}
        added_product_response = client.post(API_ENDPOINT + f'{"product/add-product"}', data=test_body)
        assert added_product_response.status_code == 200
        added_product_response_json = added_product_response.json
        assert added_product_response_json["success"] is True


def test_add_product2(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"product_name": 15, "product_price": 15}
        added_product_response = client.post(API_ENDPOINT + f'{"product/add-product"}', data=test_body)
        assert added_product_response.status_code == 200
        added_product_response_json = added_product_response.json
        assert added_product_response_json["success"] is False


def test_add_product3(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"product_name": "'chips'", "product_price": "'break'"}
        added_product_response = client.post(API_ENDPOINT + f'{"product/add-product"}', data=test_body)
        assert added_product_response.status_code == 200
        added_product_response_json = added_product_response.json
        assert added_product_response_json["success"] is False


def test_delete_product(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"product_id": 1}
        deleted_product_response = client.post(API_ENDPOINT + f'{"product/delete-product"}', data=test_body)
        assert deleted_product_response.status_code == 200
        deleted_product_response_json = deleted_product_response.json
        if deleted_product_response_json["message"] == PRODUCT_DOES_NOT_EXIST:
            assert deleted_product_response_json["success"] is False
        else:
            assert deleted_product_response_json["success"] is True
