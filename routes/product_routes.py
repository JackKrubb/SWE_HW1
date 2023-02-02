from flask import Blueprint, jsonify, request
from flask_mysqldb import MySQL
from MySQLdb.constants.FIELD_TYPE import JSON

from command_template.product_command import Product
from sql.sql_connection import Connection

product_blueprint = Blueprint("product", __name__, url_prefix="/")
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


def text_is_invalid(text: str) -> bool:
    """Check if the text is invalid.

    Args:
        text (str): input text

    Returns:
      true if the text is a number, false otherwise
    """
    if text.isnumeric():
        return True
    else:
        return False


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


@product_blueprint.route("/product", methods=["GET"])
def all_product() -> JSON:
    """Return all products.

    Args:

    Returns:
      json of all products, otherwise, None
    """
    mysql = import_mysql()
    sql_connection = Connection(mysql)
    sql_connection.execute(Product.get_all_products())
    prods = sql_connection.fetch_all_data()
    return jsonify(prods)


@product_blueprint.route("/product/single", methods=["GET"])
def one_product() -> JSON:
    """Return one product.

    Args:

    Returns:
      json of that product, otherwise, None
    """
    mysql = import_mysql()
    product_form = request.form
    product_id = int(product_form["product_id"])
    sql_connection = Connection(mysql)
    sql_connection.execute(Product.get_product_by_id(product_id))
    prods = sql_connection.fetch_one_data()
    return jsonify(prods)


@product_blueprint.route("/product/add-product", methods=["POST"])
def add_product() -> JSON:
    """Add a product.

    Args:

    Returns:
      json message if the text or number is invalid, otherwise, JSON of all products
    """
    mysql = import_mysql()
    product_form = request.form
    product_name = product_form["product_name"]
    if text_is_invalid(product_name):
        return jsonify(success=False, message="Product name cannot be a number")
    elif num_is_invalid(product_form["product_price"]):
        return jsonify(success=False, message=INVALID_NUMBER_MSG)
    product_price = int(product_form["product_price"])
    sql_connection = Connection(mysql)
    sql_connection.execute(Product.add_product(product_name, product_price))
    sql_connection.commit()
    return jsonify(success=True, message="Product has been successfully added.")


@product_blueprint.route("/product/edit-product", methods=["POST"])
def edit_product() -> JSON:
    """Edit a product.

    Args:

    Returns:
      json message if the text or number is invalid, otherwise, JSON of all products
    """
    mysql = import_mysql()
    sql_connection = Connection(mysql)
    product_form = request.form
    new_product_name = product_form["product_name"]
    product_id = int(product_form["product_id"])
    one_product_by_id = sql_connection.execute(Product.get_product_by_id(product_id))
    if one_product_by_id == 0:
        return jsonify(success=False, message="Product does not exist.")
    if text_is_invalid(new_product_name):  # pragma: no cover
        return jsonify(success=False, message="Product name cannot be a number")
    elif num_is_invalid(product_form["product_price"]):  # pragma: no cover
        return jsonify(success=False, message=INVALID_NUMBER_MSG)
    new_product_price = int(product_form["product_price"])
    sql_connection.execute(Product.edit_product_by_id(product_id, new_product_name, new_product_price))
    sql_connection.commit()
    return jsonify(success=True, message="Product has been successfully edited.")


@product_blueprint.route("/product/delete-product", methods=["POST"])
def delete_product() -> JSON:
    """Delete a product.

    Args:

    Returns:
      JSON of all products
    """
    mysql = import_mysql()
    product_form = request.form
    product_id = int(product_form["product_id"])
    sql_connection = Connection(mysql)
    one_product_by_id = sql_connection.execute(Product.get_product_by_id(product_id))
    if one_product_by_id == 0:
        return jsonify(success=False, message="Product does not exist.")
    else:  # pragma: no cover
        sql_connection.execute(Product.delete_product_by_id(product_id))
        sql_connection.commit()
        return jsonify(success=True, message="Product has been successfully deleted.")
