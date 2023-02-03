from typing import List, Tuple

from flask_mysqldb import MySQL


class Connection:
    """
    A class for mySQL connection.

    Methods
    -------
    execute(query_statement: str):
        execute the given query_statement from the parameter
    commit():
        commit the connection
    fetch_all_data_without_close():
        fetch all data without closing cursor
    fetch_all_data():
        fetch all data and close cursor
    fetch_one_data_without_close():
        fetch one data without closing cursor
    fetch_one_data():
        fetch one data and close cursor

    """

    def __init__(self, mysql: MySQL):
        """Initialize connection class with mysql connection."""
        self.cursor = mysql.connection.cursor()
        self.mysql = mysql

    def execute(self, query_statement: str) -> int:
        """Execute the given query_statement from the parameter.

        Args:
            query_statement (str): query statement

        Returns:
          number of rows from cursor execution
        """
        return self.cursor.execute(query_statement)

    def commit(self):
        """Commit the connection.

        Args:

        Returns:
          commits the connection and closes cursor
        """
        self.mysql.connection.commit()
        self.cursor.close()

    def fetch_all_data_without_close(self) -> List[Tuple]:
        """Fetch all data without closing cursor.

        Args:

        Returns:
          list of tuples of data
        """
        result = self.cursor.fetchall()  # pragma: no cover
        return result  # pragma: no cover

    def fetch_all_data(self) -> List[Tuple]:
        """Fetch all data and close cursor.

        Args:

        Returns:
          list of tuples of data and closes cursor
        """
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def fetch_one_data_without_close(self) -> dict:
        """Fetch one data without closing cursor.

        Args:

        Returns:
          dictionary of data
        """
        result = self.cursor.fetchone()  # pragma: no cover
        return result  # pragma: no cover

    def fetch_one_data(self) -> dict:
        """Fetch one data and close cursor.

        Args:

        Returns:
          dictionary of data and closes cursor
        """
        result = self.cursor.fetchone()
        self.cursor.close()
        return result
