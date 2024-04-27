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

    # Create table Trips
    c.execute('''CREATE TABLE IF NOT EXISTS Trips (
                    id INTEGER,
                    client_id INTEGER,
                    driver_id INTEGER,
                    city_id INTEGER,
                    status TEXT,
                    request_at TEXT
                )''')
    
    # Insert data into Trips table
    trips_data = [
        (1, 1, 10, 1, 'completed', '2013-10-01'),
        (2, 2, 11, 1, 'cancelled_by_driver', '2013-10-01'),
        (3, 3, 12, 6, 'completed', '2013-10-01'),
        (4, 4, 13, 6, 'cancelled_by_client', '2013-10-01'),
        (5, 1, 10, 1, 'completed', '2013-10-02'),
        (6, 2, 11, 6, 'completed', '2013-10-02'),
        (7, 3, 12, 6, 'completed', '2013-10-02'),
        (8, 2, 12, 12, 'completed', '2013-10-03'),
        (9, 3, 10, 12, 'completed', '2013-10-03'),
        (10, 4, 13, 12, 'cancelled_by_driver', '2013-10-03')
    ]

    c.executemany('INSERT INTO Trips VALUES (?, ?, ?, ?, ?, ?)', trips_data)

    # Create table Users
    c.execute('''CREATE TABLE IF NOT EXISTS Users_Details (
                    users_id INTEGER,
                    banned TEXT,
                    role TEXT
                )''')

    users_data = [
        (1, 'No', 'client'),
        (2, 'Yes', 'client'),
        (3, 'No', 'client'),
        (4, 'No', 'client'),
        (10, 'No', 'driver'),
        (11, 'No', 'driver'),
        (12, 'No', 'driver'),
        (13, 'No', 'driver')
    ]

    c.executemany('INSERT INTO Users_Details VALUES (?, ?, ?)', users_data)
    conn.commit()

    questions = [
        ("Welcome to the ICC World Cup database, where the excitement of cricket unfolds! Within the 'icc_world_cup' table, we've neatly organized columns for Team_1, Team_2, and Winner. Your mission: unearth the total matches played, victories secured, and defeats encountered by each team. Your goal is to present this data sorted by the number of wins, revealing the true champions of the cricketing world!", [("India", 2, 2, 0), ("NZ", 1, 1, 0), ("Eng", 2, 1, 1), ("Aus", 2, 1, 1), ("SL", 2, 0, 2), ("SA", 1, 0, 1)]),
        ("Can you devise a query to calculate both the count of new customers and repeated customers for each order date from the provided Customer_orders table? Provide the result sorted in ascending order by order date, with the format: order_date, new_customer_count, repeat_customer_count.", [('2022-01-01', 3, 0), ('2022-01-02', 2, 1), ('2022-01-03', 1, 2)]),
        ("Given is a table 'Entries', which contains the details of employees' entries in a company, specifying the resources they use. However, each employee can only enter a floor once per day. There's a loophole where if the same person has different email IDs, they can enter multiple times. Your task is to find, for each employee name, the total number of entries, the most visited floor, and the resources they used. Present the results in the format: name, total_visits, most_visited_floor, resources_used.", [('A', 3, 1, 'CPU,DESKTOP'), ('B', 3, 2, 'DESKTOP,MONITOR')]),
        ("Consider two tables: 'Person' and 'Friend'. Write a query to retrieve the PersonID, Name, number of friends, and total score of individuals who have friends with a combined score exceeding 100. This query will help identify individuals with significant social connections and academic achievements. Give your result in the formate : personid, total_friend_score, no_of_friends,	person_name", [(2, 115, 2, 'Bob'), (4, 101, 3, 'Tara')]),
        ('''Consider two tables: 'Tripes' and 'Users_Details', Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03" Round Cancellation Rate to two decimal points. The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day. Give your result in the formate : request_at, cancelled_trip_count, total_trips, cancelled_percent''', [('2013-10-01', 1, 3, 33.33), ('2013-10-02', 0, 2, 0.0), ('2013-10-03', 1, 2, 50.0)])#,
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
        ],
        [
            {
                "Column Name": ["id", "client_id", "driver_id", "city_id", "status", "request_at"],
                "Data Type": ["INTEGER", "INTEGER", "INTEGER", "INTEGER", "TEXT", "TEXT"],
                "Description": ["Unique identifier for each trip","ID of the client who requested the trip","ID of the driver assigned to the trip","ID of the city where the trip took place","Status of the trip","Timestamp of when the trip was requested"]
            },
            {
                "Column Name": ["users_id", "banned", "role"],
                "Data Type": ["INTEGER", "TEXT", "TEXT"],
                "Description": ["Unique identifier for each user","Indicator if the user is banned (Yes/No)","Role of the user (e.g., client, driver)"]
            }
        ]
    ]

    schema_title = [["Table : ICC_World_Cup"],["Table : Customer_orders"],["Table : Entries"],["Table : Person","Table : Friend"],["Table: Trips", "Table: Users_Details"]]
    expected_out_col = [["Team","Total_Matches_Played","Victories_Secured","Defeats_Encountered"],["order_date","new_customer_count","repeat_customer_count"],['name', 'total_visits', 'most_visited_floor', 'resources_used'], ['personid','total_friend_score','no_of_friends','person_name'],['request_at', 'cancelled_trip_count', 'total_trips', 'cancelled_percent']]
    print("Hello")
    return conn, c, questions, schema_set, schema_title, expected_out_col
