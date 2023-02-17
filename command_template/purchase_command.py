class Purchase:
    """
    A class for stocks in the vending machine.

    Methods
    -------
    get_one_stock_from_one_vend(product_id: int, vending_id: int):
        retrieves one stock from a specified vending machine
    get_all_stock_from_one_vend(vending_id: int):
        retrieves all stock from specified vending machine
    add_stock(vending_id: int, product_id: int, product_amount: int):
        add a stock to the database
    edit_stock_by_id(new_product_amount: int, stocking_id: int):
        edit a stock from the database
    delete_stock_by_id(stocking_id: int):
        delete a stock from the database
    """

    @staticmethod
    def get_purchase_from_vending_machine(vending_machine_id: int) -> str:
        """Get purchase records from vending machine."""
        return f"SELECT * FROM purchase WHERE vending_id = {vending_machine_id}"

    @staticmethod
    def get_purchase_from_product(product_id: int) -> str:
        """Get purchase records from product."""
        return f"SELECT * FROM purchase WHERE product_id = {product_id}"

    @staticmethod
    def create_purchase_record(product_id: int, vending_machine_id: int, quantity: int, json_state: str) -> str:
        """Create purchase records into the database."""
        return (  # pragma: no cover
            f"INSERT INTO purchase(product_id, vending_id, quantity_amount, time_stamp, stock_state)"
            f"VALUES ({product_id},{vending_machine_id},{quantity},now(), '{json_state}')"
        )
