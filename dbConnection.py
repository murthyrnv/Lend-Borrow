import sqlite3

class db:
    def __init__(self):
        self.dbconn = sqlite3.connect('appData.db')
        self.dbconn.row_factory = sqlite3.Row
        self.cursor = self.dbconn.cursor()

    def getcursor(self):
        return self.cursor

    def closeconn(self):
        self.cursor.close()
        self.dbconn.close()

    def initializeDB(self):
        create_users_table = "CREATE TABLE IF NOT EXISTS users " \
                       "(id int PRIMARY KEY,name text, email text, password text, balance int)"
        self.cursor.execute(create_users_table)
        insert_user ='''INSERT OR IGNORE INTO users VALUES(1,'LBUser1','lbuser1@gmail.com','Password1!',100)'''
        self.cursor.execute(insert_user)
        insert_user ='''INSERT OR IGNORE INTO users VALUES(2,'LBUser2','lbuser2@gmail.com','Password1!',150)'''
        self.cursor.execute(insert_user)
        insert_user ='''INSERT OR IGNORE INTO users VALUES(3,'LBUser3','lbuser3@gmail.com','Password1!',200)'''
        self.cursor.execute(insert_user)
        insert_user ='''INSERT OR IGNORE INTO users VALUES(4,'LBUser4','lb','lb',200)'''
        self.cursor.execute(insert_user)