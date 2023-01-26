class Stock:
    SELECT_ALL = "SELECT * FROM stocking"

    def get_one_stock_from_one_vend(product_id: int, vending_id: int):
        return f"SELECT * FROM stocking WHERE product_id = {product_id} AND vending_id = {vending_id}"

    def get_all_stock_from_one_vend(vending_id: int):
        return f"SELECT * FROM stocking WHERE vending_id = {vending_id}"

    def add_stock(vending_id: int, product_id: int, product_amount):
        return f"INSERT INTO stocking(vending_id, product_id, product_amount) VALUES ('{vending_id}','{product_id}','{product_amount}')"

    def edit_stock_by_id(new_product_amount: int, stocking_id: int):
        return f"UPDATE stocking SET product_amount={new_product_amount} WHERE stocking_id={stocking_id}"

    def delete_stock_by_id(stocking_id: int):
        return f"DELETE FROM stocking WHERE stocking_id = {stocking_id}"
