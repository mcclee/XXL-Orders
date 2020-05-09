import sqlite3


class DBController:
    def __init__(self, db_name):
        self.db = None
        self.db_name = db_name

    def get_db(self):
        if self.db is not None:
            return self.db
        self.db = sqlite3.connect(self.db_name)
        return self.db

    def close(self):
        if self.db:
            self.db.close()
        self.db = None


class UserController(DBController):
    def __init__(self, db_name, user_table):
        super().__init__(db_name)
        self.table = user_table
        self.db = super().get_db()

    def insert(self, ID, username, psw):
        try:
            self.db.cursor().execute(
                f'insert into {self.table} (id, name, password) values (?, ?, ?)',
                (ID, username, psw))
        except sqlite3.IntegrityError:
            print(f"{ID} has been used")
            return False
        self.db.commit()
        return True

    def update_address(self, ID, address):
        self.db = super().get_db()
        self.db.cursor().execute(f"update {self.table} SET address = ? where id = ?", (address, ID))
        self.db.commit()

    def exist(self, ID):
        self.db = super().get_db()
        result = self.db.cursor().execute(f"select ID from {self.table} where id = ?", (ID,)).fetchall()
        return True if result else False


if __name__ == '__main__':
    uc = UserController("XXL.db", "User")










