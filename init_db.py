import sqlite3


# Create a database
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
    conn.commit()
    conn.close()

    def case_table():
        conn = sqlite3.connect("cases.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS cases(
        case_number INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        type INTEGER,
        FOREIGN KEY (type) REFERENCES type(id)
        )""")

    def citations():
        conn = sqlite3.connect("cases.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS citations")

    def paragraphs():
        pass

    case_table()


# Make sure no duplicates are in the database
def check_database():
    conn = sqlite3.connect("cases.db")
    c = conn.cursor()
    c.execute("SELECT * FROM type")
    data = c.fetchall()
    print(data)


def main():
    create_database()
    # check_database()


if __name__ == "__main__":
    main()
