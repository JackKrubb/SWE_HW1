import yaml
from flask import Flask, jsonify, redirect, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from MySQLdb.constants.FIELD_TYPE import JSON

from commands.product_command import Product
from commands.stock_command import Stock
from commands.vending_machine_command import VendingMachine
from sql_connection import Connection

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)  # Compliant
Bootstrap(app)

cred = yaml.load(open("../cred.yaml"), Loader=yaml.Loader)
app.config["MYSQL_HOST"] = cred["mysql_host"]
app.config["MYSQL_USER"] = cred["mysql_user"]
app.config["MYSQL_PASSWORD"] = cred["mysql_password"]
app.config["MYSQL_DB"] = cred["mysql_db"]
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

ALL_VENDING_ROUTE = "/vending"
ALL_PRODUCT_ROUTE = "/product"
ALL_STOCK_ROUTE = "/stock"
INVALID_NUMBER_MSG = "Invalid number, please input the correct input"


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


def num_is_invalid(num: float) -> bool:
    """Check if number is invalid.

    Args:
        num (int): input number

    Returns:
      true if number is negative, or it is not a number, false otherwise
    """
    if not isinstance(num, float):
        return True
    elif num < 0:
        return True
    else:
        return False


@app.route("/vending")
def all_vending() -> JSON:
    """Return all vending machines.

    Args:

    Returns:
      json of all vending machines if exist, none otherwise
    """
    sql_connection = Connection(mysql)
    all_vending_machines = sql_connection.execute(VendingMachine.get_all_vending_machines())
    if all_vending_machines > 0:
        vend = sql_connection.fetch_all_data()
        return jsonify(vend)
    else:
        return None


@app.route("/vending/single/<int:vending_id>", methods=["GET"])
def one_vending(vending_id: int) -> JSON:
    """Return one vending machine.

    Args:
        vending_id (int): vending machine's id

    Returns:
      json of the vending machine if it exists, none otherwise
    """
    sql_connection = Connection(mysql)
    all_vending_machines_by_id = sql_connection.execute(VendingMachine.get_vending_machine_by_id(vending_id))
    if all_vending_machines_by_id > 0:
        vend = sql_connection.fetch_one_data()
        return jsonify(vend)
    else:
        return None


@app.route("/vending/create-vending", methods=["POST"])
def create_vending() -> JSON:
    """Add a vending machine to the database.

    Args:

    Returns:
      json of message if cannot create the vending machine, otherwise, return all vending machines
    """
    vending_form = request.form
    vending_location = vending_form["vending_location"]
    if text_is_invalid(vending_location):
        return jsonify(success=False, message="Vending location cannot be a number")
    sql_connection = Connection(mysql)
    sql_connection.execute(VendingMachine.create_vending_machine(vending_location))
    sql_connection.commit()
    return redirect(ALL_VENDING_ROUTE)


@app.route("/vending/edit-vending", methods=["POST"])
def edit_vending() -> JSON:
    """Edit a vending machine.

    Args:

    Returns:
      json of message if cannot edit the vending machine, otherwise, return all vending machines
    """
    vending_form = request.form
    new_vending_location = vending_form["vending_location"]
    vending_id = int(vending_form["vending_id"])
    if text_is_invalid(new_vending_location):
        return jsonify(success=False, message="Vending location cannot be a number")
    sql_connection = Connection(mysql)
    sql_connection.execute(VendingMachine.edit_vending_machine_by_id(new_vending_location, vending_id))
    sql_connection.commit()
    return redirect(ALL_VENDING_ROUTE)


@app.route("/vending/delete-vending")
def delete_vending() -> JSON:
    """Delete a vending machine.

    Args:

    Returns:
      return all vending machines
    """
    vending_form = request.form
    vending_id = int(vending_form["vending_id"])
    sql_connection = Connection(mysql)
    sql_connection.execute(VendingMachine.delete_vending_machine_by_id(vending_id))
    sql_connection.commit()
    return redirect(ALL_VENDING_ROUTE)


@app.route("/product")
def all_product() -> JSON:
    """Return all products.

    Args:

    Returns:
      json of all products, otherwise, None
    """
    sql_connection = Connection(mysql)
    all_products = sql_connection.execute(Product.get_all_products())
    if all_products > 0:
        prods = sql_connection.fetch_all_data()
        return jsonify(prods)
    else:
        return None


@app.route("/product/single/<int:product_id>", methods=["GET"])
def one_product(product_id: int) -> JSON:
    """Return one product.

    Args:

    Returns:
      json of that product, otherwise, None
    """
    sql_connection = Connection(mysql)
    product_by_id = sql_connection.execute(Product.get_product_by_id(product_id))
    if product_by_id > 0:
        prods = sql_connection.fetch_one_data()
        return jsonify(prods)
    else:
        return None


# Add new product


@app.route("/product/add-product", methods=["POST"])
def add_product() -> JSON:
    """Add a product.

    Args:

    Returns:
      json message if the text or number is invalid, otherwise, JSON of all products
    """
    product_form = request.form
    product_name = product_form["product_name"]
    product_price = float(product_form["product_price"])
    if text_is_invalid(product_name):
        return jsonify(success=False, message="Product name cannot be a number")
    elif num_is_invalid(product_price):
        return jsonify(success=False, message=INVALID_NUMBER_MSG)
    sql_connection = Connection(mysql)
    sql_connection.execute(Product.add_product(product_name, product_price))
    sql_connection.commit()
    return redirect(ALL_PRODUCT_ROUTE)


@app.route("/product/edit-product", methods=["POST"])
def edit_product() -> JSON:
    """Edit a product.

    Args:

    Returns:
      json message if the text or number is invalid, otherwise, JSON of all products
    """
    product_form = request.form
    new_product_name = product_form["product_name"]
    new_product_price = float(product_form["product_price"])
    product_id = int(product_form["product_id"])
    if text_is_invalid(new_product_name):
        return jsonify(success=False, message="Product name cannot be a number")
    elif num_is_invalid(new_product_price):
        return jsonify(success=False, message=INVALID_NUMBER_MSG)
    sql_connection = Connection(mysql)
    sql_connection.execute(Product.edit_product_by_id(product_id, new_product_name, new_product_price))
    sql_connection.commit()
    return redirect(ALL_PRODUCT_ROUTE)


@app.route("/product/delete-product")
def delete_product() -> JSON:
    """Delete a product.

    Args:

    Returns:
      JSON of all products
    """
    product_form = request.form
    product_id = int(product_form["product_id"])
    sql_connection = Connection(mysql)
    sql_connection.execute(Product.delete_product_by_id(product_id))
    sql_connection.commit()
    return redirect(ALL_PRODUCT_ROUTE)


@app.route("/stock")
def all_stock() -> JSON:
    """Return all stocks in all vending machines.

    Args:

    Returns:
     JSON of all stocks
    """
    sql_connection = Connection(mysql)
    all_stocks = sql_connection.execute(Stock.get_all_stocks())
    if all_stocks > 0:
        stock = sql_connection.fetch_all_data()
        return jsonify(stock)
    else:
        return None


@app.route("/stock/single-stock", methods=["GET"])
def one_stock_one_vend() -> JSON:
    """Return one stock from one vending machine.

    Args:

    Returns:
     JSON of the stock of that vending machine, otherwise, None
    """
    stock_form = request.form
    vending_id = int(stock_form["vending_id"])
    product_id = int(stock_form["product_id"])

    sql_connection = Connection(mysql)
    one_stock_from_one_vend = sql_connection.execute(Stock.get_one_stock_from_one_vend(product_id, vending_id))
    if one_stock_from_one_vend > 0:
        stock = sql_connection.fetch_one_data()
        return jsonify(stock)
    else:
        return None


@app.route("/stock/single-vend", methods=["GET"])
def all_stock_one_vend() -> JSON:
    """Return all stocks from one vending machine.

    Args:

    Returns:
     JSON of all the stocks of that vending machine, otherwise, None
    """
    stock_form = request.form
    vending_id = int(stock_form["vending_id"])

    sql_connection = Connection(mysql)
    all_stocks_one_vend = sql_connection.execute(Stock.get_all_stock_from_one_vend(vending_id))
    if all_stocks_one_vend > 0:
        stock = sql_connection.fetch_all_data()
        return jsonify(stock)
    else:
        return None


@app.route("/stock/add-stock", methods=["POST"])
def add_stock() -> JSON:
    """Add stock into the database.

    Args:

    Returns:
     JSON message if invalid number, otherwise, return JSON of all stocks
    """
    stock_form = request.form
    vending_id = int(stock_form["vending_id"])
    product_id = int(stock_form["product_id"])
    product_amount = int(stock_form["product_amount"])
    if num_is_invalid(product_amount):
        return jsonify(success=False, message=INVALID_NUMBER_MSG)
    sql_connection = Connection(mysql)
    duplicate = sql_connection.execute(Stock.get_one_stock_from_one_vend(product_id, vending_id))
    if duplicate > 0:
        stock = sql_connection.fetch_one_data_without_close()
        stocking_id = int(stock["stocking_id"])
        new_product_amount = int(stock["product_amount"]) + int(product_amount)
        sql_connection.execute(Stock.edit_stock_by_id(new_product_amount, stocking_id))
        sql_connection.commit()
        return redirect(ALL_STOCK_ROUTE)
    else:
        sql_connection.execute(Stock.add_stock(vending_id, product_id, product_amount))
        sql_connection.commit()
        return redirect(ALL_STOCK_ROUTE)


# Edit stock amount


@app.route("/stock/edit-stock", methods=["POST"])
def edit_stock() -> JSON:
    """Edit a stock.

    Args:

    Returns:
     JSON of message if invalid number, otherwise, return JSON of all sstocks.
    """
    sql_connection = Connection(mysql)
    stock_form = request.form
    stocking_id = int(stock_form["stocking_id"])
    new_product_amount = int(stock_form["product_amount"])
    if num_is_invalid(new_product_amount):
        return jsonify(success=False, message=INVALID_NUMBER_MSG)
    sql_connection.execute(Stock.edit_stock_by_id(new_product_amount, stocking_id))
    sql_connection.commit()
    return redirect(ALL_STOCK_ROUTE)


# Delete stock


@app.route("/stock/delete-stock")
def delete_stock() -> JSON:
    """Delete a stock.

    Args:

    Returns:
     JSON of all the stocks
    """
    sql_connection = Connection(mysql)
    stock_form = request.form
    stocking_id = int(stock_form["stocking_id"])
    sql_connection.execute(Stock.delete_stock_by_id(stocking_id))
    sql_connection.commit()
    return redirect(ALL_STOCK_ROUTE)


if __name__ == "__main__":
    app.run(debug=True)
