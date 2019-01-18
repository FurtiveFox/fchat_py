import os
import sqlite3
from sqlite3 import Error
import pickle

class Fchat_DB():

    def __init__(self):
        self.db_file = (os.getcwd() + "\\fchat_py.db")
        self.conn = None

        self.sql_create_accounts_table = """ CREATE TABLE IF NOT EXISTS accounts (
                                                id integer PRIMARY KEY,
                                                username text NOT NULL,
                                                password blob
                                                ); """

    def open_database(self):

        try:
            self.conn = sqlite3.connect(self.db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)


    def close_database(self):

        if self.conn is not None:
            try:
                self.conn.close()
            except Error as e:
                print(e)



    def initialize_database(self):
        try:
            c = self.conn.cursor()
            c.execute(self.sql_create_accounts_table)
        except Error as e:
            print(e)
