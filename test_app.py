#!/bin/python
# This file contains a function that lists all the cases in the table cases in cases.db.
# In the future, it will have other functions to test other aspects of the app, this file should be deleted before the app is deployed.

import sqlite3


def list_elements_of_table_cases():
    conn = sqlite3.connect("cases.db")
    c = conn.cursor()
    c.execute("SELECT title FROM cases")
    results = c.fetchall()
    conn.close()
    print(results)


def main():
    list_elements_of_table_cases()


if __name__ == "__main__":
    main()
