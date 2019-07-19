import sqlite3
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.conn.commit()


    def selectLast(self):
        self.cursor.execute("SELECT * FROM carinfo ORDER BY id DESC LIMIT 1")
        result = self.cursor.fetchone()
        return result[1], result[2]

    def selectByHash(self, key):

        self.cursor.execute("SELECT * FROM carinfo WHERE hash = '{}'".format(key))
        result = self.cursor.fetchone()
        print(result)
        if result == None:
            return None, None
        return result[1], result[2]

    def __del__(self):
        self.conn.close()



    