# This file holds all the databse logic for the app, any UI stuff should go in ui.py, all databse logic goes here
import sqlite3


def new_case(title, debate_type):
    conn = sqlite3.connect("cases.db")
    c = conn.cursor()
    c.execute("INSERT INTO cases(title, type) VALUES (?, ?)", (title, debate_type))
    conn.commit()
    conn.close()
