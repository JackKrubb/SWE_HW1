import pymysql
from flask_wtf import CSRFProtect

pymysql.install_as_MySQLdb()
import yaml
from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()


def create_app() -> Flask:
    """Initialize and setup flask app.

    Args:

    Returns:
      flask application
    """
    application = Flask(__name__)
    csrf = CSRFProtect()
    csrf.init_app(application)  # Uncomment when running pytest
    cred = yaml.load(open("./cred.yaml"), Loader=yaml.Loader)
    application.config["MYSQL_HOST"] = cred["mysql_host"]
    application.config["MYSQL_USER"] = cred["mysql_user"]
    application.config["MYSQL_PASSWORD"] = cred["mysql_password"]
    application.config["MYSQL_DB"] = cred["mysql_db"]
    application.config["MYSQL_CURSORCLASS"] = "DictCursor"
    mysql.init_app(application)

    with application.app_context():
        from routes.product_routes import product_blueprint
        from routes.purchase_routes import purchase_blueprint
        from routes.stock_routes import stock_blueprint
        from routes.vending_machine_routes import vending_blueprint

        application.register_blueprint(vending_blueprint)
        application.register_blueprint(product_blueprint)
        application.register_blueprint(stock_blueprint)
        application.register_blueprint(purchase_blueprint)

    return application


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
