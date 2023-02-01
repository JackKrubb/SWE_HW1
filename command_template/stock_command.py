class Stock:
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
    def get_all_stocks() -> str:
        """Retrieve all stocks from the stocking table.

        Args:

        Returns:
          query statement to get all stocks
        """
        return f'{"SELECT * FROM stocking"}'

    @staticmethod
    def get_one_stock_from_one_vend(product_id: int, vending_id: int) -> str:
        """Retrieve all products from the product table.

        Args:
            product_id (int): product's id
            vending_id (int): vending machine's id

        Returns:
          query statement to return one stock from one vending machine
        """
        return f"SELECT * FROM stocking WHERE product_id = {product_id} AND vending_id = {vending_id}"

    @staticmethod
    def get_all_stock_from_one_vend(vending_id: int) -> str:
        """Retrieve all products from the product table.

        Args:
            vending_id (int): vending machine's id

        Returns:
          query statement to get all stocks from one vending machine
        """
        return f"SELECT * FROM stocking WHERE vending_id = {vending_id}"

    @staticmethod
    def add_stock(vending_id: int, product_id: int, product_amount: int) -> str:
        """Add a stock to the database.

        Args:
            vending_id (int): vending machine's id
            product_id (int): product's id
            product_amount (int): product's amount

        Returns:
          query statement inserting new stocks into the database
        """
        return (
            f"INSERT INTO stocking(vending_id, product_id, product_amount) "
            f"VALUES ('{vending_id}','{product_id}','{product_amount}')"
        )

    @staticmethod
    def edit_stock_by_id(new_product_amount: int, stocking_id: int) -> str:
        """Edit a stock from the database.

        Args:
            new_product_amount (int): new product's amount
            stocking_id (int): stocking's id

        Returns:
          query statement editing a stock from the database
        """
        return f"UPDATE stocking SET product_amount={new_product_amount} WHERE stocking_id={stocking_id}"

    @staticmethod
    def delete_stock_by_id(stocking_id: int) -> str:
        """Delete a stock from the database.

        Args:
            stocking_id (int): product's id

        Returns:
          query statement deleting a stock from the database
        """
        return f"DELETE FROM stocking WHERE stocking_id = {stocking_id}"
