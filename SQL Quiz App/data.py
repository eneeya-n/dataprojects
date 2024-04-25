import sqlite3

def exc():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()

    # Create customers table and insert sample data
    c.execute('''CREATE TABLE customers (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT,
                    country TEXT
                )''')

    sample_customers = [
        (1, 'John Doe', 'john@example.com', 'USA'),
        (2, 'Alice Smith', 'alice@example.com', 'Canada'),
        (3, 'Bob Johnson', 'bob@example.com', 'UK'),
        (4, 'Emily Brown', 'emily@example.com', 'USA'),
        (5, 'David Lee', 'david@example.com', 'Australia'),
        (6, 'Emma Wilson', 'emma@example.com', 'USA'),
        (7, 'Michael Clark', 'michael@example.com', 'Canada'),
        (8, 'Sophia Garcia', 'sophia@example.com', 'UK'),
        (9, 'James Martinez', 'james@example.com', 'USA'),
        (10, 'Olivia Taylor', 'olivia@example.com', 'Australia')
    ]

    c.executemany('INSERT INTO customers VALUES (?, ?, ?, ?)', sample_customers)
    conn.commit()

    c.execute('''create table icc_world_cup
    (
    Team_1 Varchar(20),
    Team_2 Varchar(20),
    Winner Varchar(20)
    )''')

    icc_data = [
        ('India','SL','India'),
        ('SL','Aus','Aus'),
        ('SA','Eng','Eng'),
        ('Eng','NZ','NZ'),
        ('Aus','India','India')
    ]

    c.executemany('INSERT INTO icc_world_cup VALUES (?, ?, ?)', icc_data)
    conn.commit()

    questions = [
        ("Welcome to the ICC World Cup database, where the excitement of cricket unfolds! Within the 'icc_world_cup' table, we've neatly organized columns for Team_1, Team_2, and Winner. Your mission: unearth the total matches played, victories secured, and defeats encountered by each team. Your goal is to present this data sorted by the number of wins, revealing the true champions of the cricketing world!", [("India", 2, 2, 0), ("NZ", 1, 1, 0), ("Eng", 2, 1, 1), ("Aus", 2, 1, 1), ("SL", 2, 0, 2), ("SA", 1, 0, 1)]),
        ("How many customers are from the USA?", [(4,)])#,
        # ("List the names and emails of customers from Canada.", [("Alice Smith", "alice@example.com"), ("Michael Clark", "michael@example.com")]),
        # ("Count the number of customers from the UK.", [(2,)]),
        # ("List the names of customers containing the letter 'a'.", [("Alice Smith",), ("David Lee",), ("Emma Wilson",), ("Michael Clark",), ("Sophia Garcia",), ("James Martinez",), ("Olivia Taylor",)]),
        # ("List the emails of customers from Australia whose name starts with 'E'.", [("emily@example.com",), ("emma@example.com",)])
    ]

    schema_set = [
        {
            "Column Name": ["Team_1", "Team_2", "Winner"],
            "Data Type": ["VARCHAR(20)", "VARCHAR(20)", "VARCHAR(20)"],
            "Description": ["Name of the first team", "Name of the second team", "Name of the winning team"]
        },
        {
            "Column Name": ["id", "name", "email", "country"],
            "Data Type": ["INTEGER", "TEXT", "TEXT", "TEXT"],
            "Description": ["Unique identifier for each customer", "Name of the customer", "Email address of the customer", "Country of the customer"]
        }
    ]
    return conn, c, questions, schema_set