from flask import Blueprint, jsonify, request
from flask_mysqldb import MySQL
from MySQLdb.constants.FIELD_TYPE import JSON

from command_template.vending_machine_command import VendingMachine
from sql.sql_connection import Connection

vending_blueprint = Blueprint("vending_machine", __name__, url_prefix="/")


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


@vending_blueprint.route("/vending", methods=["GET"])
def all_vending() -> JSON:
    """Return all vending machines.

    Args:

    Returns:
      json of all vending machines if exist, none otherwise
    """
    mysql = import_mysql()

    sql_connection = Connection(mysql)
    sql_connection.execute(VendingMachine.get_all_vending_machines())
    vend = sql_connection.fetch_all_data()
    return jsonify(vend)


@vending_blueprint.route("/vending/single", methods=["GET"])
def one_vending() -> JSON:
    """Return one vending machine.

    Args:

    Returns:
      json of the vending machine if it exists, none otherwise
    """
    mysql = import_mysql()
    vending_form = request.form
    vending_id = int(vending_form["vending_id"])
    sql_connection = Connection(mysql)
    sql_connection.execute(VendingMachine.get_vending_machine_by_id(vending_id))
    vend = sql_connection.fetch_one_data()
    return jsonify(vend)


@vending_blueprint.route("/vending/create-vending", methods=["POST"])
def create_vending() -> JSON:
    """Add a vending machine to the database.

    Args:

    Returns:
      json of message if you cannot create the vending machine, otherwise, return all vending machines
    """
    mysql = import_mysql()
    vending_form = request.form
    vending_location = vending_form["vending_location"]
    if text_is_invalid(vending_location):
        return jsonify(success=False, message="Vending location cannot be a number")
    sql_connection = Connection(mysql)
    sql_connection.execute(VendingMachine.create_vending_machine(vending_location))
    sql_connection.commit()
    return jsonify(success=True, message="Vending machine has been successfully created.")


@vending_blueprint.route("/vending/edit-vending", methods=["POST"])
def edit_vending() -> JSON:
    """Edit a vending machine.

    Args:

    Returns:
      json of message if you cannot edit the vending machine, otherwise, return all vending machines
    """
    mysql = import_mysql()
    vending_form = request.form
    new_vending_location = vending_form["vending_location"]
    vending_id = int(vending_form["vending_id"])
    sql_connection = Connection(mysql)
    one_vending_machine_by_id = sql_connection.execute(VendingMachine.get_vending_machine_by_id(vending_id))
    if one_vending_machine_by_id == 0:
        return jsonify(success=False, message="Vending machine does not exist.")
    if text_is_invalid(new_vending_location):  # pragma: no cover
        return jsonify(success=False, message="Vending location cannot be a number")
    sql_connection.execute(VendingMachine.edit_vending_machine_by_id(new_vending_location, vending_id))
    sql_connection.commit()
    return jsonify(success=True, message="Vending machine has been successfully edited.")


@vending_blueprint.route("/vending/delete-vending", methods=["POST"])
def delete_vending() -> JSON:
    """Delete a vending machine.

    Args:

    Returns:
      return all vending machines
    """
    mysql = import_mysql()
    vending_form = request.form
    vending_id = int(vending_form["vending_id"])
    sql_connection = Connection(mysql)
    one_vending_machine_by_id = sql_connection.execute(VendingMachine.get_vending_machine_by_id(vending_id))
    if one_vending_machine_by_id == 0:
        return jsonify(success=False, message="Vending machine does not exist.")
    else:  # pragma: no cover
        sql_connection.execute(VendingMachine.delete_vending_machine_by_id(vending_id))
        sql_connection.commit()
        return jsonify(success=True, message="Vending machine has been successfully deleted.")
