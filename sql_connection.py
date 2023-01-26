class Connection:

    def __init__(self, mysql):    
        self.cursor = mysql.connection.cursor()
        self.mysql = mysql

    def execute(self, query_statement):
        return self.cursor.execute(query_statement)

    def commit(self):
        self.mysql.connection.commit()
        self.cursor.close()

    def fetch_all_data_without_close(self):
        result = self.cursor.fetchall()
        return result

    def fetch_all_data(self):
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def fetch_one_data_without_close(self):
        result = self.cursor.fetchone()
        return result
        
    def fetch_one_data(self):
        result = self.cursor.fetchone()
        self.cursor.close()
        return result