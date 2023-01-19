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

# Create new vending machine
@app.route('/vending/create/', methods=['POST'])
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

# Delete vending machine
@app.route('/vending/delete-vending/<int:id>/')
def delete_product(id):
    cur = mysql.connection.cursor()
    query_statement = f"DELETE FROM vending_machine WHERE vending_id = {id}"
    cur.execute(query_statement)
    mysql.connection.commit()
    return redirect('/vending')

# @app.route('/product')
# def all_product():
#     cur = mysql.connection.cursor()
#     number_of_rows = cur.execute("SELECT * FROM product ORDER BY product_price DESC")
#     if(number_of_rows>0):
#         prods = cur.fetchall()
#         cur.close()
#         return jsonify(prods)
#     else:
#         return None

# @app.route('/product/single/<int:id>', methods=['GET'])
# def one_product(id):
#     cur = mysql.connection.cursor()
#     number_of_rows = cur.execute("SELECT * FROM product WHERE product_id = {id}")
#     if(number_of_rows>0):
#         prods = cur.fetchone()
#         cur.close()
#         return jsonify(prods)
#     else:
#         return None

# @app.route('/delete-product/<int:id>/')
# def delete_product(id):
#     cur = mysql.connection.cursor()
#     query_statement = f"DELETE FROM product WHERE product_id = {id}"
#     cur.execute(query_statement)
#     mysql.connection.commit()
#     return redirect('/product')

if __name__ == '__main__':
    app.run(debug=True)