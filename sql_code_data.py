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

    c.execute('''create table customer_orders (
    order_id integer,
    customer_id integer,
    order_date date,
    order_amount integer
    )''')

    cus_ord_data = [
        (1, 100, '2022-01-01', 2000),
        (2, 200, '2022-01-01', 2500),
        (3, 300, '2022-01-01', 2100),
        (4, 100, '2022-01-02', 2000),
        (5, 400, '2022-01-02', 2200),
        (6, 500, '2022-01-02', 2700),
        (7, 100, '2022-01-03', 3000),
        (8, 400, '2022-01-03', 1000),
        (9, 600, '2022-01-03', 3000)
    ]

    c.executemany('INSERT INTO customer_orders VALUES (?, ?, ?, ?)', cus_ord_data)
    conn.commit()    

    c.execute('''
    CREATE TABLE entries (
        name VARCHAR(20),
        address VARCHAR(20),
        email VARCHAR(20),
        floor INTEGER,
        resources VARCHAR(10)
    )
    ''')

    entries_data = [
        ('A', 'Bangalore', 'A@gmail.com', 1, 'CPU'),
        ('A', 'Bangalore', 'A1@gmail.com', 1, 'CPU'),
        ('A', 'Bangalore', 'A2@gmail.com', 2, 'DESKTOP'),
        ('B', 'Bangalore', 'B@gmail.com', 2, 'DESKTOP'),
        ('B', 'Bangalore', 'B1@gmail.com', 2, 'DESKTOP'),
        ('B', 'Bangalore', 'B2@gmail.com', 1, 'MONITOR')
    ]

    c.executemany('INSERT INTO entries VALUES (?, ?, ?, ?, ?)', entries_data)
    conn.commit()

    c.execute('''CREATE TABLE IF NOT EXISTS Person (
             PersonID INTEGER PRIMARY KEY,
             Name TEXT,
             Email TEXT,
             Score INTEGER
             )''')

    # Insert data into table
    person_data = [
        (1, 'Alice', 'alice2018@hotmail.com', 88),
        (2, 'Bob', 'bob2018@hotmail.com', 11),
        (3, 'Davis', 'davis2018@hotmail.com', 27),
        (4, 'Tara', 'tara2018@hotmail.com', 45),
        (5, 'John', 'john2018@hotmail.com', 63)
    ]

    c.executemany('INSERT INTO Person VALUES (?, ?, ?, ?)', person_data)

    c.execute('''CREATE TABLE IF NOT EXISTS Friend (
                PersonID INTEGER,
                FriendID INTEGER,
                FOREIGN KEY(PersonID) REFERENCES Person(PersonID),
                FOREIGN KEY(FriendID) REFERENCES Person(PersonID)
                )''')

    friend_data = [
        (1, 2),
        (1, 3),
        (2, 1),
        (2, 3),
        (3, 5),
        (4, 2),
        (4, 3),
        (4, 5)
    ]

    c.executemany('INSERT INTO Friend VALUES (?, ?)', friend_data)
    conn.commit()

    questions = [
        ("Welcome to the ICC World Cup database, where the excitement of cricket unfolds! Within the 'icc_world_cup' table, we've neatly organized columns for Team_1, Team_2, and Winner. Your mission: unearth the total matches played, victories secured, and defeats encountered by each team. Your goal is to present this data sorted by the number of wins, revealing the true champions of the cricketing world!", [("India", 2, 2, 0), ("NZ", 1, 1, 0), ("Eng", 2, 1, 1), ("Aus", 2, 1, 1), ("SL", 2, 0, 2), ("SA", 1, 0, 1)]),
        ("Can you devise a query to calculate both the count of new customers and repeated customers for each order date from the provided Customer_orders table? Provide the result sorted in ascending order by order date, with the format: order_date, new_customer_count, repeat_customer_count.", [('2022-01-01', 3, 0), ('2022-01-02', 2, 1), ('2022-01-03', 1, 2)]),
        ("Given is a table 'Entries', which contains the details of employees' entries in a company, specifying the resources they use. However, each employee can only enter a floor once per day. There's a loophole where if the same person has different email IDs, they can enter multiple times. Your task is to find, for each employee name, the total number of entries, the most visited floor, and the resources they used. Present the results in the format: name, total_visits, most_visited_floor, resources_used.", [('A', 3, 1, 'CPU,DESKTOP'), ('B', 3, 2, 'DESKTOP,MONITOR')]),
        ("Consider two tables: 'Person' and 'Friend'. Write a query to retrieve the PersonID, Name, number of friends, and total score of individuals who have friends with a combined score exceeding 100. This query will help identify individuals with significant social connections and academic achievements. Give your result in the formate : personid, total_friend_score, no_of_friends,	person_name", [(2, 115, 2, 'Bob'), (4, 101, 3, 'Tara')])#,
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
            "Column Name": ["order_id", "customer_id", "order_date", "order_amount"],
            "Data Type": ["INTEGER", "INTEGER", "DATE", "INTEGER"],
            "Description": ["Unique identifier for each order", "Unique identifier for each customer", "Date of the order", "Amount of the order"]
        },
        {
            "Column Name": ["name", "address", "email", "floor", "resources"],
            "Data Type": ["VARCHAR(20)", "VARCHAR(20)", "VARCHAR(20)", "INTEGER", "VARCHAR(10)"],
            "Description": ["Name of the employee","Address of the employee","Email address of the employee","Visited Floor number","Resources used by the employee"]
        },
        [
            {
                "Column Name": ["PersonID", "Name", "Email", "Score"],
                "Data Type": ["INTEGER", "TEXT", "TEXT", "INTEGER"],
                "Description": ["Unique identifier for each person", "Name of the person", "Email address of the person", "Score of the person"]
            },
            {
                "Column Name": ["PersonID", "FriendID"],
                "Data Type": ["INTEGER", "INTEGER"],
                "Description": ["References the ID of the person", "References the ID of the friend"]
            }
        ]
    ]

    schema_title = [["Table : ICC_World_Cup"],["Table : Customer_orders"],["Table : Entries"],["Table : Person","Table : Friend"]]
    expected_out_col = [["Team","Total_Matches_Played","Victories_Secured","Defeats_Encountered"],["order_date","new_customer_count","repeat_customer_count"],['name', 'total_visits', 'most_visited_floor', 'resources_used'], ['personid','total_friend_score','no_of_friends','person_name']]
    
    return conn, c, questions, schema_set, schema_title, expected_out_col
