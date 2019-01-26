import os
import sqlite3
from sqlite3 import Error
import pickle


class Fchat_DB:

    def __init__(self):
        self.db_file = os.path.join(os.getcwd(), "fchat_py.db")

        try:
            self.conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)

        try:
            self.cur = self.conn.cursor()
        except Error as e:
            print(e)


        self.sql_create_accounts_table = """ CREATE TABLE IF NOT EXISTS accounts (
                                                id integer PRIMARY KEY,
                                                accountname text NOT NULL,
                                                password blob
                                                ); """

        self.sql_retrive_accounts = """ SELECT accountname, password FROM accounts"""



    def get_accounts(self):
        with self.conn:
            self.cur.execute(self.sql_retrive_accounts)
            data = self.cur.fetchall()
            if not data:
                print("No accounts found")
                return None
            accounts = []
            for row in data:
                if row[1]:
                    account = Fchat_Account(row[0],pickle.loads(row[1]))

                else:
                    account = Fchat_Account(row[0], None)
                accounts.append(account)
            return accounts

    def initialize_database(self):
        with self.conn:
            self.cur.execute(self.sql_create_accounts_table)

    def insert_account(self, account):
        with self.conn:
            self.cur.execute("INSERT INTO accounts VALUES(?,?,?)", (None, account.account_name, pickle.dumps(account.password)))


class Fchat_Account:

    def __init__(self, account_name, password):
        self.account_name = account_name
        self.password = password




