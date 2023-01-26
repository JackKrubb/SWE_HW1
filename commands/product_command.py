class Product:
    SELECT_ALL =  "SELECT * FROM product ORDER BY product_price DESC"

    def get_product_by_id(id: int):
        return f"SELECT * FROM product WHERE product_id = {id}"

    def add_product(product_name, product_price):
        return f"INSERT INTO product(product_name, product_price) VALUES ('{product_name}','{product_price}')"

    def edit_product_by_id(id: int, new_product_name, new_product_price):
        return f"UPDATE product SET product_name={new_product_name}, product_price={new_product_price} WHERE product_id = {id}"

    def delete_product_by_id(id: int):
        return f"DELETE FROM product WHERE product_id = {id}"