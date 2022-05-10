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
        create_transactions_table = "CREATE TABLE IF NOT EXISTS transactions " \
                       "(id int PRIMARY KEY,type int, date text, status int, lentBy int, borrowedBy int, Reason text, amount int)"
        self.cursor.execute(create_transactions_table)
        insert_user ='''INSERT OR IGNORE INTO users VALUES(1,'LBUser1','lbuser1@gmail.com','Password1!',30)'''
        self.cursor.execute(insert_user)
        insert_user ='''INSERT OR IGNORE INTO users VALUES(2,'LBUser2','lbuser2@gmail.com','Password1!',50)'''
        self.cursor.execute(insert_user)
        insert_user ='''INSERT OR IGNORE INTO users VALUES(3,'LBUser3','lbuser3@gmail.com','Password1!',-20)'''
        self.cursor.execute(insert_user)
        insert_user ='''INSERT OR IGNORE INTO users VALUES(4,'LBUser4','lb','lb',200)'''
        self.cursor.execute(insert_user)

        insert_transaction = '''INSERT OR IGNORE INTO transactions VALUES(1,0,'2022-04-13',0, 1,2,'School Fee', 100)'''
        self.cursor.execute(insert_transaction)

        insert_transaction = '''INSERT OR IGNORE INTO transactions VALUES(2,0,'2022-04-12',0, 2,3,'EMI', 150)'''
        self.cursor.execute(insert_transaction)

        insert_transaction = '''INSERT OR IGNORE INTO transactions VALUES(3,0,'2022-04-11',0, 3,1,'Medical', 70)'''
        self.cursor.execute(insert_transaction)
