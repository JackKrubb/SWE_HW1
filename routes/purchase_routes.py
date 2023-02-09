import json

from flask import Blueprint, Response, jsonify, request
from flask_mysqldb import MySQL

from command_template.purchase_command import Purchase
from sql.sql_connection import Connection

purchase_blueprint = Blueprint("purchase", __name__, url_prefix="/")
INVALID_NUMBER_MSG = "Invalid number, please input the correct input"


def import_mysql() -> MySQL:
    """Import MySQL from another file.

    Args:

    Returns:
      return current mysql
    """
    from routes.get_mysql import get_mysql

    current_mysql = get_mysql()
    return current_mysql


@purchase_blueprint.route("/purchase/vending", methods=["GET"])
def get_purchase_from_vending() -> Response:
    """Get purchase records based on the vending machine given."""
    mysql = import_mysql()
    purchase_form = request.form
    vending_id = int(purchase_form["vending_id"])
    sql_connection = Connection(mysql)
    sql_connection.execute(Purchase.get_purchase_from_vending_machine(vending_id))
    purchases = sql_connection.fetch_all_data()
    purchases_json = jsonify(purchases).json
    for purchase in purchases_json:
        purchase["stock_state"] = json.loads(purchase["stock_state"])
    return purchases_json


@purchase_blueprint.route("/purchase/product", methods=["GET"])
def get_purchase_from_product() -> Response:
    """Get purchase records based on the product given."""
    mysql = import_mysql()
    purchase_form = request.form
    product_id = int(purchase_form["product_id"])
    sql_connection = Connection(mysql)
    sql_connection.execute(Purchase.get_purchase_from_product(product_id))
    purchases = sql_connection.fetch_all_data()
    purchases_json = jsonify(purchases).json
    for purchase in purchases_json:
        purchase["stock_state"] = json.loads(purchase["stock_state"])
    return purchases_json
