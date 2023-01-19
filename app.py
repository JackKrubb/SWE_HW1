from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_mysqldb import MySQL
import yaml
from flask_bootstrap import Bootstrap

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
@app.route('/vending')
def all_vending():
    cur = mysql.connection.cursor()
    number_of_rows = cur.execute("SELECT * FROM vending_machine")
    if(number_of_rows>0):
        vend = cur.fetchall()
        cur.close()
        return jsonify(vend)
    else:
        return None

# Return one vending
@app.route('/vending/single/<int:id>', methods=['GET'])
def one_vending(id):
    cur = mysql.connection.cursor()
    number_of_rows = cur.execute("SELECT * FROM vending_machine WHERE vending_id = {id}")
    if(number_of_rows>0):
        vend = cur.fetchone()
        cur.close()
        return jsonify(vend)
    else:
        return None

# Create new vending machine
@app.route('/vending/create-vending', methods=['POST'])
def create_vending():
    vending_form = request.form
    vending_location = vending_form['vending_location']
    cur = mysql.connection.cursor()
    query_statement = f"INSERT INTO vending_machine(vending_location) VALUES ({vending_location})"
    cur.execute(query_statement)
    mysql.connection.commit()
    cur.close()
    return redirect('/vending')


# Edit vending machine
@app.route('/vending/edit-vending/<int:id>', methods=['POST'])
def edit_vending(id):
    cur = mysql.connection.cursor()
    vending_form = request.form
    new_vending_location = vending_form['vending_location']
    query_statement = f"UPDATE vending_machine SET vending_location={new_vending_location} WHERE vending_id = {id}"
    cur.execute(query_statement)
    mysql.connection.commit()
    cur.close()
    return redirect('/vending')

# Delete one vending machine
@app.route('/vending/delete-vending/<int:id>')
def delete_vending(id):
    cur = mysql.connection.cursor()
    query_statement = f"DELETE FROM vending_machine WHERE vending_id = {id}"
    cur.execute(query_statement)
    mysql.connection.commit()
    return redirect('/vending')

# Return all products ordered by price
@app.route('/product')
def all_product():
    cur = mysql.connection.cursor()
    number_of_rows = cur.execute("SELECT * FROM product ORDER BY product_price DESC")
    if(number_of_rows>0):
        prods = cur.fetchall()
        cur.close()
        return jsonify(prods)
    else:
        return None

# Return one product 
@app.route('/product/single/<int:id>', methods=['GET'])
def one_product(id):
    cur = mysql.connection.cursor()
    number_of_rows = cur.execute("SELECT * FROM product WHERE product_id = {id}")
    if(number_of_rows>0):
        prods = cur.fetchone()
        cur.close()
        return jsonify(prods)
    else:
        return None

# Add new product
@app.route('/product/add-product', methods=['POST'])
def add_product():
    product_form = request.form
    product_name = product_form['product_name']
    product_price = product_form['product_price']
    cur = mysql.connection.cursor()
    query_statement = f"INSERT INTO product(product_name, product_price) VALUES ('{product_name}','{product_price}')"
    cur.execute(query_statement)
    mysql.connection.commit()
    cur.close()
    return redirect('/product')

# Edit product
@app.route('/product/edit-product/<int:id>', methods=['POST'])
def edit_product(id):
    cur = mysql.connection.cursor()
    product_form = request.form
    new_product_name = product_form['product_name']
    new_product_price = product_form['product_price']
    query_statement = f"UPDATE product SET product_name={new_product_name}, product_price={new_product_price} WHERE product_id = {id}"
    cur.execute(query_statement)
    mysql.connection.commit()
    cur.close()
    return redirect('/product')

# Delete one product
@app.route('/product/delete-product/<int:id>')
def delete_product(id):
    cur = mysql.connection.cursor()
    query_statement = f"DELETE FROM product WHERE product_id = {id}"
    cur.execute(query_statement)
    mysql.connection.commit()
    return redirect('/product')

# Return all stocks in all vending machine
@app.route('/stock')
def all_stock():
    cur = mysql.connection.cursor()
    number_of_rows = cur.execute("SELECT * FROM stocking")
    if(number_of_rows>0):
        stock = cur.fetchall()
        cur.close()
        return jsonify(stock)
    else:
        return None

# Return one stock from one vending
@app.route('/stock/single-stock', methods=['GET'])
def one_stock_one_vend():
    stock_form = request.form
    vending_id = stock_form['vending_id']
    product_id = stock_form['product_id']

    cur = mysql.connection.cursor()
    query_statement = f"SELECT * FROM stocking WHERE product_id = {product_id} AND vending_id = {vending_id}"
    number_of_rows = cur.execute(query_statement)
    if(number_of_rows>0):
        stock = cur.fetchone()
        cur.close()
        return jsonify(stock)
    else:
        return None

# Return all stock from one vending
@app.route('/stock/single-vend', methods=['GET'])
def all_stock_one_vend():
    stock_form = request.form
    vending_id = stock_form['vending_id']

    cur = mysql.connection.cursor()
    query_statement = f"SELECT * FROM stocking WHERE vending_id = {vending_id}"
    number_of_rows = cur.execute(query_statement)
    if(number_of_rows>0):
        stock = cur.fetchall()
        cur.close()
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

    cur = mysql.connection.cursor()
    query_statement_check = f"SELECT * FROM stocking WHERE product_id={product_id} AND vending_id={vending_id}"
    duplicate = cur.execute(query_statement_check)
    if duplicate > 0:
        stock = cur.fetchone()
        stocking_id = stock['stocking_id']
        new_product_amount = int(stock['product_amount']) + int(product_amount)
        query_statement = f"UPDATE stocking SET product_amount={new_product_amount} WHERE stocking_id={stocking_id}"
        cur.execute(query_statement)
        mysql.connection.commit()
        cur.close()
        return redirect('/stock')
    else:
        query_statement = f"INSERT INTO stocking(vending_id, product_id, product_amount) VALUES ('{vending_id}','{product_id}','{product_amount}')"
        cur.execute(query_statement)
        mysql.connection.commit()
        cur.close()
        return redirect('/stock')

if __name__ == '__main__':
    app.run(debug=True)