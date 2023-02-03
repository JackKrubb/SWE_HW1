from flask import Blueprint, jsonify, request
from flask_mysqldb import MySQL
from MySQLdb.constants.FIELD_TYPE import JSON

from command_template.product_command import Product
from command_template.stock_command import Stock
from command_template.vending_machine_command import VendingMachine
from sql.sql_connection import Connection

stock_blueprint = Blueprint("stock", __name__, url_prefix="/")
INVALID_NUMBER_MSG = "Invalid number, please input the correct input"
STOCK_ERROR = "Stock error."


def import_mysql() -> MySQL:
    """Import MySQL from another file.

    Args:

    Returns:
      return current mysql
    """
    from routes.get_mysql import get_mysql

    current_mysql = get_mysql()
    return current_mysql


def num_is_invalid(num: str) -> bool:
    """Check if number is invalid.

    Args:
        num (int): input number

    Returns:
      true if number is negative, or it is not a number, false otherwise
    """
    if not num.isdigit():
        return True
    else:
        return False


@stock_blueprint.route("/stock", methods=["GET"])
def all_stock() -> JSON:
    """Return all stocks in all vending machines.

    Args:

    Returns:
     JSON of all stocks
    """
    mysql = import_mysql()
    sql_connection = Connection(mysql)
    sql_connection.execute(Stock.get_all_stocks())
    stock = sql_connection.fetch_all_data()
    return jsonify(stock)


@stock_blueprint.route("/stock/single-stock", methods=["GET"])
def one_stock_one_vend() -> JSON:
    """Return one stock from one vending machine.

    Args:

    Returns:
     JSON of the stock of that vending machine, otherwise, None
    """
    mysql = import_mysql()
    stock_form = request.form
    vending_id = int(stock_form["vending_id"])
    product_id = int(stock_form["product_id"])

    sql_connection = Connection(mysql)
    sql_connection.execute(Stock.get_one_stock_from_one_vend(product_id, vending_id))
    stock = sql_connection.fetch_one_data()
    return jsonify(stock)


@stock_blueprint.route("/stock/single", methods=["GET"])
def one_stock() -> JSON:
    """Return one stock from one vending machine.

    Args:

    Returns:
     JSON of the stock of that vending machine, otherwise, None
    """
    mysql = import_mysql()
    stock_form = request.form
    stocking_id = int(stock_form["stocking_id"])

    sql_connection = Connection(mysql)
    sql_connection.execute(Stock.get_stock_by_id(stocking_id))
    stock = sql_connection.fetch_one_data()
    return jsonify(stock)


@stock_blueprint.route("/stock/single-vend", methods=["GET"])
def all_stock_one_vend() -> JSON:
    """Return all stocks from one vending machine.

    Args:

    Returns:
     JSON of all the stocks of that vending machine, otherwise, None
    """
    mysql = import_mysql()
    stock_form = request.form
    vending_id = int(stock_form["vending_id"])

    sql_connection = Connection(mysql)
    sql_connection.execute(Stock.get_all_stock_from_one_vend(vending_id))
    stock = sql_connection.fetch_all_data()
    return jsonify(stock)


@stock_blueprint.route("/stock/add-stock", methods=["POST"])
def add_stock() -> JSON:
    """Add stock into the database.

    Args:

    Returns:
     JSON message if invalid number, otherwise, return JSON of all stocks
    """
    mysql = import_mysql()
    stock_form = request.form
    vending_id = int(stock_form["vending_id"])
    product_id = int(stock_form["product_id"])
    if num_is_invalid(stock_form["product_amount"]):
        return jsonify(success=False, message=INVALID_NUMBER_MSG)
    product_amount = int(stock_form["product_amount"])
    sql_connection = Connection(mysql)
    product_id_exist = sql_connection.execute(Product.get_product_by_id(product_id))
    if product_id_exist == 0:
        return jsonify(success=False, message=STOCK_ERROR)
    vending_id_exist = sql_connection.execute(VendingMachine.get_vending_machine_by_id(vending_id))
    if vending_id_exist == 0:  # pragma: no cover
        return jsonify(success=False, message=STOCK_ERROR)
    num_of_stock_in_vend = sql_connection.execute(Stock.get_one_stock_from_one_vend(product_id, vending_id))
    if num_of_stock_in_vend > 0:  # pragma: no cover
        stock = sql_connection.fetch_one_data_without_close()
        stocking_id = int(stock["stocking_id"])
        new_product_amount = int(stock["product_amount"]) + int(product_amount)
        sql_connection.execute(Stock.edit_stock_by_id(new_product_amount, stocking_id))
        sql_connection.commit()
        return jsonify(success=True, message="Stock has been successfully added.")
    elif num_of_stock_in_vend == 0:  # pragma: no cover
        sql_connection.execute(Stock.add_stock(vending_id, product_id, product_amount))
        sql_connection.commit()
        return jsonify(success=True, message="Stock has been successfully added.")
    else:  # pragma: no cover
        return jsonify(success=False, message=STOCK_ERROR)


@stock_blueprint.route("/stock/edit-stock", methods=["POST"])
def edit_stock() -> JSON:
    """Edit a stock.

    Args:

    Returns:
     JSON of message if invalid number, otherwise, return JSON of all sstocks.
    """
    mysql = import_mysql()
    stock_form = request.form
    stocking_id = int(stock_form["stocking_id"])
    sql_connection = Connection(mysql)
    stock_exist = sql_connection.execute(Stock.get_stock_by_id(stocking_id))
    if stock_exist == 0:
        return jsonify(success=False, message=STOCK_ERROR)
    if num_is_invalid(stock_form["product_amount"]):  # pragma: no cover
        return jsonify(success=False, message=INVALID_NUMBER_MSG)
    new_product_amount = int(stock_form["product_amount"])
    sql_connection.execute(Stock.edit_stock_by_id(new_product_amount, stocking_id))
    sql_connection.commit()
    return jsonify(success=True, message="Stock has been successfully edited.")


@stock_blueprint.route("/stock/delete-stock", methods=["POST"])
def delete_stock() -> JSON:
    """Delete a stock.

    Args:

    Returns:
     JSON of all the stocks
    """
    mysql = import_mysql()
    sql_connection = Connection(mysql)
    stock_form = request.form
    stocking_id = int(stock_form["stocking_id"])
    stock_exist = sql_connection.execute(Stock.get_stock_by_id(stocking_id))
    if stock_exist == 0:
        return jsonify(success=False, message=STOCK_ERROR)
    else:  # pragma: no cover
        sql_connection.execute(Stock.delete_stock_by_id(stocking_id))
        sql_connection.commit()
        return jsonify(success=True, message="Stock has been successfully deleted.")
