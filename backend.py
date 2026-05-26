#!/bin/python3
# This file holds all the database logic for the app, any UI stuff should go in ui.py, all databse logic goes here
import sqlite3


def create_database():
    conn = sqlite3.connect("cases.db")
    c = conn.cursor()
    values = [(1, "Public Forum"), (2, "Lincoln-Douglas"), (3, "Congress")]
    c.execute(
        """CREATE TABLE IF NOT EXISTS type(
        id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL
    )"""
    )
    conn.commit()
    # Insert the types of debate into rows, "OR IGNORE" prevents duplicates
    c.executemany(
        """INSERT OR IGNORE INTO type (id, name) VALUES (?, ?)""",
        values,
    )

    c.execute("""CREATE TABLE IF NOT EXISTS cases(
        case_number INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        type INTEGER,
        side INTEGER,
        FOREIGN KEY (type) REFERENCES type(id)
        )""")
    conn.commit()
    conn.close()


def new_case(title, debate_type):
    conn = sqlite3.connect("cases.db")
    c = conn.cursor()
    c.execute("INSERT INTO cases(title, type) VALUES (?, ?)", (title, debate_type))
    conn.commit()
    conn.close()
