from flask import Flask
from flask.testing import FlaskClient

API_ENDPOINT = "http://127.0.0.1:5000/"
VEND_DOES_NOT_EXIST = "Vending machine does not exist."


def test_all_vending(app2: Flask, client: FlaskClient):
    with app2.app_context():
        all_vending_machines_response = client.get(API_ENDPOINT + f'{"vending"}')
        assert all_vending_machines_response.status_code == 200


def test_one_vending(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"vending_id": 1}
        one_vending_machines_response = client.get(API_ENDPOINT + f'{"vending/single"}', data=test_body)
        assert one_vending_machines_response.status_code == 200


def test_create_vending(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"vending_location": "'abc'"}
        created_vending_machines_response = client.post(API_ENDPOINT + f'{"vending/create-vending"}', data=test_body)
        assert created_vending_machines_response.status_code == 200
        created_vending_machines_response_json = created_vending_machines_response.json
        if created_vending_machines_response_json["message"] == VEND_DOES_NOT_EXIST:
            assert created_vending_machines_response_json["success"] is False
        else:
            assert created_vending_machines_response_json["success"] is True


def test_create_vending2(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"vending_location": 15}
        created_vending_machines_response = client.post(API_ENDPOINT + f'{"vending/create-vending"}', data=test_body)
        assert created_vending_machines_response.status_code == 200
        created_vending_machines_response_json = created_vending_machines_response.json
        assert created_vending_machines_response_json["success"] is False


def test_edit_vending(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"vending_location": "'new_abc'", "vending_id": 1}
        edited_vending_machine_response = client.post(API_ENDPOINT + f'{"vending/edit-vending"}', data=test_body)
        assert edited_vending_machine_response.status_code == 200
        edited_vending_machine_response_json = edited_vending_machine_response.json
        if edited_vending_machine_response_json["message"] == VEND_DOES_NOT_EXIST:
            assert edited_vending_machine_response_json["success"] is False
        else:
            assert edited_vending_machine_response_json["success"] is True


def test_edit_vending2(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"vending_location": 15, "vending_id": 1}
        edited_vending_machine_response = client.post(API_ENDPOINT + f'{"vending/edit-vending"}', data=test_body)
        assert edited_vending_machine_response.status_code == 200
        edited_vending_machine_response_json = edited_vending_machine_response.json
        assert edited_vending_machine_response_json["success"] is False


def test_delete_vending(app2: Flask, client: FlaskClient):
    with app2.app_context():
        test_body = {"vending_id": 1}
        deleted_vending_machine_response = client.post(API_ENDPOINT + f'{"vending/delete-vending"}', data=test_body)
        assert deleted_vending_machine_response.status_code == 200
        deleted_vending_machine_response_json = deleted_vending_machine_response.json
        if deleted_vending_machine_response_json["message"] == VEND_DOES_NOT_EXIST:
            assert deleted_vending_machine_response_json["success"] is False
        else:
            assert deleted_vending_machine_response_json["success"] is True
