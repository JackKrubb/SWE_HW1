from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_mysqldb import MySQL
import yaml
from flask_bootstrap import Bootstrap
from commands.vending_machine_command import Vending_Machine
from commands.product_command import Product
from commands.stock_command import Stock
from sql_connection import Connection

app = Flask(__name__)
Bootstrap(app)

cred = yaml.load(open('cred.yaml'), Loader=yaml.Loader)
app.config['MYSQL_HOST'] = cred['mysql_host']
app.config['MYSQL_USER'] = cred['mysql_user']
app.config['MYSQL_PASSWORD'] = cred['mysql_password']
app.config['MYSQL_DB'] = cred['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# Return all vending machines

def text_is_invalid(text):
    if text.isnumeric():
        return True
    else:
        return False

def num_is_invalid(num):
    if not isinstance(num, int):
        return True
    elif num < 0:
        return True
    else:
        return False

@app.route('/vending')
def all_vending():
    sql_connection = Connection(mysql)
    all_vending_machines = sql_connection.execute(Vending_Machine.SELECT_ALL)
    if (all_vending_machines > 0):
        vend = sql_connection.fetch_all_data()
        return jsonify(vend)
    else:
        return None

# Return one vending

@app.route('/vending/single/<int:id>', methods=['GET'])
def one_vending(id):
    sql_connection = Connection(mysql)
    all_vending_machines_by_id = sql_connection.execute(Vending_Machine.get_vending_machine_by_id(id))
    if (all_vending_machines_by_id > 0):
        vend = sql_connection.fetch_one_data()
        return jsonify(vend)
    else:
        return None

# Create new vending machine

@app.route('/vending/create-vending', methods=['POST'])
def create_vending():
    vending_form = request.form
    vending_location = vending_form['vending_location']
    if text_is_invalid(vending_location):
        return jsonify(success=False, message="Vending location cannot be a number")
    sql_connection = Connection(mysql)
    sql_connection.execute(Vending_Machine.create_vending_machine(vending_location))
    sql_connection.commit()
    return redirect('/vending')


# Edit vending machine
@app.route('/vending/edit-vending/<int:id>', methods=['POST'])
def edit_vending(id):
    vending_form = request.form
    new_vending_location = vending_form['vending_location']
    if text_is_invalid(new_vending_location):
        return jsonify(success=False, message="Vending location cannot be a number")
    sql_connection = Connection(mysql)
    sql_connection.execute(Vending_Machine.edit_vending_machine_by_id(new_vending_location, id))
    sql_connection.commit()
    return redirect('/vending')

# Delete one vending machine

@app.route('/vending/delete-vending/<int:id>')
def delete_vending(id):
    sql_connection = Connection(mysql)
    sql_connection.execute(Vending_Machine.delete_vending_machine_by_id(id))
    sql_connection.commit()
    return redirect('/vending')

# Return all products ordered by price

@app.route('/product')
def all_product():
    sql_connection = Connection(mysql)
    all_products = sql_connection.execute(Product.SELECT_ALL)
    if (all_products > 0):
        prods = sql_connection.fetch_all_data()
        return jsonify(prods)
    else:
        return None

# Return one product

@app.route('/product/single/<int:id>', methods=['GET'])
def one_product(id):
    sql_connection = Connection(mysql)
    product_by_id = sql_connection.execute(Product.get_product_by_id(id))
    if (product_by_id > 0):
        prods = sql_connection.fetch_one_data()
        return jsonify(prods)
    else:
        return None

# Add new product

@app.route('/product/add-product', methods=['POST'])
def add_product():
    product_form = request.form
    product_name = product_form['product_name']
    product_price = product_form['product_price']
    if text_is_invalid(product_name):
        return jsonify(success=False, message="Product name cannot be a number")
    elif num_is_invalid(product_price):
        return jsonify(success=False, message="Invalid number, please input the correct input")
    sql_connection = Connection(mysql)
    sql_connection.execute(Product.add_product(product_name, product_price))
    sql_connection.commit()
    return redirect('/product')

# Edit product

@app.route('/product/edit-product/<int:id>', methods=['POST'])
def edit_product(id):
    product_form = request.form
    new_product_name = product_form['product_name']
    new_product_price = product_form['product_price']
    if text_is_invalid(new_product_name):
        return jsonify(success=False, message="Product name cannot be a number")
    elif num_is_invalid(new_product_price):
        return jsonify(success=False, message="Invalid number, please input the correct input")
    sql_connection = Connection(mysql)
    sql_connection.execute(Product.edit_product_by_id(id, new_product_name, new_product_price))
    sql_connection.commit()
    return redirect('/product')

# Delete one product

@app.route('/product/delete-product/<int:id>')
def delete_product(id):
    sql_connection = Connection(mysql)
    sql_connection.execute(Product.delete_product_by_id(id))
    sql_connection.commit()
    return redirect('/product')

# Return all stocks in all vending machine

@app.route('/stock')
def all_stock():
    sql_connection = Connection(mysql)
    all_stocks = sql_connection.execute(Stock.SELECT_ALL)
    if (all_stocks > 0):
        stock = sql_connection.fetch_all_data()
        return jsonify(stock)
    else:
        return None

# Return one stock from one vending

@app.route('/stock/single-stock', methods=['GET'])
def one_stock_one_vend():
    stock_form = request.form
    vending_id = stock_form['vending_id']
    product_id = stock_form['product_id']

    sql_connection = Connection(mysql)
    one_stock_from_one_vend = sql_connection.execute(Stock.get_one_stock_from_one_vend(product_id, vending_id))
    if (one_stock_from_one_vend > 0):
        stock = sql_connection.fetch_one_data()
        return jsonify(stock)
    else:
        return None

# Return all stock from one vending

@app.route('/stock/single-vend', methods=['GET'])
def all_stock_one_vend():
    stock_form = request.form
    vending_id = stock_form['vending_id']

    sql_connection = Connection(mysql)
    all_stocks_one_vend = sql_connection.execute(Stock.get_all_stock_from_one_vend(vending_id))
    if (all_stocks_one_vend > 0):
        stock = sql_connection.fetch_all_data()
        return jsonify(stock)
    else:
        return None

# Add stocks

@app.route('/stock/add-stock', methods=['POST'])
def add_stock():
    stock_form = request.form
    vending_id = stock_form['vending_id']
    product_id = stock_form['product_id']
    product_amount = stock_form['product_amount']
    if num_is_invalid(product_amount):
        return jsonify(success=False, message="Invalid number, please input the correct input")
    sql_connection = Connection(mysql)
    duplicate = sql_connection.execute(Stock.get_one_stock_from_one_vend(product_id, vending_id))
    if duplicate > 0:
        stock = sql_connection.fetch_one_data_without_close()
        stocking_id = stock['stocking_id']
        new_product_amount = int(stock['product_amount']) + int(product_amount)
        sql_connection.execute(Stock.edit_stock_by_id(new_product_amount, stocking_id))
        sql_connection.commit()
        return redirect('/stock')
    else:
        sql_connection.execute(Stock.add_stock(vending_id, product_id, product_amount))
        sql_connection.commit()
        return redirect('/stock')

# Edit stock amount

@app.route('/stock/edit-stock', methods=['POST'])
def edit_stock():
    sql_connection = Connection(mysql)
    stock_form = request.form
    stocking_id = stock_form['stocking_id']
    new_product_amount = stock_form['product_amount']
    if num_is_invalid(new_product_amount):
        return jsonify(success=False, message="Invalid number, please input the correct input")
    sql_connection.execute(Stock.edit_stock_by_id(new_product_amount, stocking_id))
    sql_connection.commit()
    return redirect('/stock')

# Delete stock

@app.route('/stock/delete-stock')
def delete_stock():
    sql_connection = Connection(mysql)
    stock_form = request.form
    stocking_id = stock_form['stocking_id']
    sql_connection.execute(Stock.delete_stock_by_id(stocking_id))
    sql_connection.commit()
    return redirect('/stock')


if __name__ == '__main__':
    app.run(debug=True)
