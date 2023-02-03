class VendingMachine:
    """
    A class for vending machines.

    Methods
    -------
    get_all_vending_machines():
        retrieves all vending machines from the vending_machine table
    get_vending_machine_by_id(id: int):
        retrieves a certain vending machine by id from the vending_machine table
    create_vending_machine(vending_location: str):
        add a vending machine to the database
    edit_vending_machine_by_id(new_vending_location: str, vending_id: int):
        edit a vending machine from the database
    delete_vending_machine_by_id(vending_id: int):
        delete a vending machine from the database
    """

    @staticmethod
    def get_all_vending_machines() -> str:
        """Retrieve all vending machine from the vending machine table.

        Args:

        Returns:
          query statement to get all vending machines
        """
        return f'{"SELECT * FROM vending_machine"}'

    @staticmethod
    def get_vending_machine_by_id(vending_id: int) -> str:
        """Retrieve a certain vending machine by id from the database.

        Args:
            vending_id (int): vending machine's id

        Returns:
          query statement to get the vending machine with vending_id = id
        """
        return f"SELECT * FROM vending_machine WHERE vending_id = {vending_id}"

    @staticmethod
    def create_vending_machine(vending_location: str) -> str:
        """Add a product to the database.

        Args:
            vending_location (str): location for vending machine

        Returns:
          query statement inserting new vending machine into the database
        """
        return f"INSERT INTO vending_machine(vending_location) VALUES ({vending_location})"

    @staticmethod
    def edit_vending_machine_by_id(new_vending_location: str, vending_id: int) -> str:
        """Edit a product from the database.

        Args:
            new_vending_location (str): new location for vending machine
            vending_id (int): vending machine's id

        Returns:
          query statement editing a vending machine from the database
        """
        return (  # pragma: no cover
            f"UPDATE vending_machine SET vending_location={new_vending_location} WHERE vending_id = {vending_id}"
        )

    @staticmethod
    def delete_vending_machine_by_id(vending_id: int) -> str:
        """Delete a product from the database.

        Args:
            vending_id (int): vending machine's id

        Returns:
          query statement deleting a vending machine from the database
        """
        return f"DELETE FROM vending_machine WHERE vending_id = {vending_id}"  # pragma: no cover
