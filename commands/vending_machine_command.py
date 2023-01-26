class Vending_Machine:

    SELECT_ALL = "SELECT * FROM vending_machine"
    def get_vending_machine_by_id(id: int):
        return f"SELECT * FROM vending_machine WHERE vending_id = {id}"

    def create_vending_machine(vending_location):
        return f"INSERT INTO vending_machine(vending_location) VALUES ({vending_location})"

    def edit_vending_machine_by_id(new_vending_location, id: int):
        return f"UPDATE vending_machine SET vending_location={new_vending_location} WHERE vending_id = {id}"

    def delete_vending_machine_by_id(id: int):
        return f"DELETE FROM vending_machine WHERE vending_id = {id}"