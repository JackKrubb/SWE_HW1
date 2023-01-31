class Product:
    """
    A class for products in the vending machine.

    Methods
    -------
    get_all_products():
        retrieves all products from the product table.
    get_product_by_id(id: int):
        retrieves a certain product by id from the Product table
    add_product(product_name: str, product_price: float):
        add a product to the database
    edit_product_by_id(product_id: int, product_name: str, product_price: float):
        edit a product from the database
    delete_product_by_id(product_id: int):
        delete a product from the database
    """

    @staticmethod
    def get_all_products() -> str:
        """Retrieve all products from the product table.

        Args:

        Returns:
          query statement to get all products
        """
        return f'{"SELECT * FROM product ORDER BY product_price DESC"}'

    @staticmethod
    def get_product_by_id(product_id: int) -> str:
        """Retrieve a certain product by id from the database.

        Args:
            product_id (int): product's id

        Returns:
          query statement to get the product with product_id = id
        """
        return f"SELECT * FROM product WHERE product_id = {product_id}"

    @staticmethod
    def add_product(product_name: str, product_price: float) -> str:
        """Add a product to the database.

        Args:
            product_name (str): name for product
            product_price (float): price for product

        Returns:
          query statement inserting new product into the database
        """
        return f"INSERT INTO product(product_name, product_price) VALUES ('{product_name}','{product_price}')"

    @staticmethod
    def edit_product_by_id(product_id: int, new_product_name: str, new_product_price: float) -> str:
        """Edit a product from the database.

        Args:
            product_id (int): product's id
            new_product_name (str): name for product
            new_product_price (float): price for product

        Returns:
          query statement editing a product from the database
        """
        return (
            f"UPDATE product SET product_name={new_product_name}, product_price={new_product_price} "
            f"WHERE product_id = {product_id}"
        )

    @staticmethod
    def delete_product_by_id(product_id: int) -> str:
        """Delete a product from the database.

        Args:
            product_id (int): product's id

        Returns:
          query statement deleting a product from the database
        """
        return f"DELETE FROM product WHERE product_id = {product_id}"
