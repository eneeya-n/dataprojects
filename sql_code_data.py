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

    # Create ticket_records table
    c.execute('''
    CREATE TABLE IF NOT EXISTS ticket_records (
        ticket_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        paid_time DATETIME,
        reason VARCHAR(255)
    )
    ''')

    # Create order_records table
    c.execute('''
    CREATE TABLE IF NOT EXISTS order_records (
        order_id INTEGER PRIMARY KEY,
        order_status VARCHAR(50),
        mid INT,
        FOREIGN KEY (mid) REFERENCES mid_records(mid)
    )
    ''')

    # Create mid_records table
    c.execute('''
    CREATE TABLE IF NOT EXISTS mid_records (
        mid INTEGER PRIMARY KEY,
        brand VARCHAR(50),
        locality VARCHAR(50),
        city VARCHAR(50)
    )
    ''')

    ticket_records_data = [
        (1, 101, '2023-09-20 12:05:00', 'Successful Payment'),
        (2, 101, '2023-09-20 12:10:00', 'Refund Issued'),
        (3, 102, '2023-09-20 12:15:00', 'Successful Payment'),
        (4, 102, '2023-09-20 12:25:00', 'Failed Payment'),
        (5, 103, '2023-09-20 12:30:00', 'Successful Payment'),
        (6, 104, '2023-09-20 12:35:00', 'Successful Payment'),
        (7, 104, '2023-09-20 12:40:00', 'Refund Issued'),
        (8, 105, '2023-09-20 12:45:00', 'Successful Payment'),
        (9, 106, '2023-09-20 12:50:00', 'Successful Payment'),
        (10, 106, '2023-09-20 12:55:00', 'Successful Payment'),
        (11, 107, '2023-09-20 13:00:00', 'Successful Payment'),
        (12, 108, '2023-09-20 13:05:00', 'Successful Payment'),
        (13, 109, '2023-09-20 13:10:00', 'Successful Payment'),
        (14, 109, '2023-09-20 13:15:00', 'Refund Issued'),
        (15, 110, '2023-09-20 13:20:00', 'Successful Payment')
    ]

    c.executemany('INSERT INTO ticket_records VALUES (?, ?, ?, ?)', ticket_records_data)  

    order_records_data = [
        (101, 'Completed', 201),
        (102, 'Failed', 202),
        (103, 'Completed', 203),
        (104, 'Completed', 204),
        (105, 'Completed', 205),
        (106, 'Completed', 206),
        (107, 'Completed', 207),
        (108, 'Completed', 208),
        (109, 'Completed', 209),
        (110, 'Completed', 210)
    ]

    c.executemany('INSERT INTO order_records VALUES (?, ?, ?)', order_records_data)  

    mid_records_data = [
        (201, 'Brand A', 'Locality X', 'City 1'),
        (202, 'Brand B', 'Locality Y', 'City 2'),
        (203, 'Brand C', 'Locality Z', 'City 3'),
        (204, 'Brand D', 'Locality X', 'City 1'),
        (205, 'Brand E', 'Locality Y', 'City 2'),
        (206, 'Brand F', 'Locality Z', 'City 3'),
        (207, 'Brand G', 'Locality X', 'City 1'),
        (208, 'Brand H', 'Locality Y', 'City 2'),
        (209, 'Brand I', 'Locality Z', 'City 3'),
        (210, 'Brand J', 'Locality X', 'City 1')
    ]

    c.executemany('INSERT INTO mid_records VALUES (?, ?, ?, ?)', mid_records_data)  
    conn.commit()

    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY,
            account_id INTEGER,
            transaction_date DATE,
            amount DECIMAL(10, 2)
        )
    ''')

    # Define the transaction data
    transactions_data = [
        (1, 101, '2023-01-01', 1000.00),
        (2, 102, '2023-01-02', -500.00),
        (3, 101, '2023-01-03', 300.00),
        (4, 103, '2023-01-05', 800.00),
        (5, 102, '2023-01-08', -200.00),
        (6, 101, '2023-01-10', 1500.00),
        (7, 103, '2023-01-15', -300.00),
        (8, 104, '2023-01-20', 600.00),
        (9, 102, '2023-01-25', -1000.00),
        (10, 101, '2023-01-30', 200.00)
    ]

    # Insert the transaction data into the table
    c.executemany('INSERT INTO transactions VALUES (?, ?, ?, ?)', transactions_data)
    conn.commit()

    # Create CricketPlayer table if not exists
    c.execute('''
        CREATE TABLE IF NOT EXISTS CricketPlayer_Table (
            player_id INTEGER PRIMARY KEY,
            player_name TEXT,
            country TEXT,
            batting_style TEXT,
            bowling_style TEXT,
            matches_played INTEGER,
            runs_scored INTEGER,
            wickets_taken INTEGER,
            batting_average DECIMAL(5,2),
            bowling_average DECIMAL(5,2)
        )
    ''')

    # Create Team table if not exists
    c.execute('''
        CREATE TABLE IF NOT EXISTS Team_Table (
            team_id INTEGER PRIMARY KEY,
            team_name TEXT,
            country TEXT,
            coach TEXT,
            captain TEXT,
            player_id INTEGER,
            FOREIGN KEY (player_id) REFERENCES CricketPlayer(player_id)
        )
    ''')

    CricketPlayer_Table_Data = [(1, 'Virat Kohli', 'India', 'Right-hand', 'Right-arm', 250, 12000, 10, 50, 50),
        (2, 'Steve Smith', 'Australia', 'Right-hand', 'Right-arm', 200, 8000, 20, 40, 30),
        (3, 'Kane Williamson', 'New Zealand', 'Right-hand', 'Right-arm', 180, 6500, 15, 45, 35),
        (4, 'Joe Root', 'England', 'Right-hand', 'Right-arm', 220, 9000, 12, 55, 40),
        (5, 'Babar Azam', 'Pakistan', 'Right-hand', 'Right-arm', 150, 6000, 5, 55, 60),
        (6, 'David Warner', 'Australia', 'Left-hand', 'Right-arm', 190, 7000, 5, 45, 80),
        (7, 'Rohit Sharma', 'India', 'Right-hand', 'Right-arm', 180, 8000, 5, 50, 90),
        (8, 'Quinton de Kock', 'South Africa', 'Left-hand', 'Right-arm', 140, 4500, 0, 35, None),
        (9, 'Aaron Finch', 'Australia', 'Right-hand', 'Left-arm', 160, 5000, None, 30, None),
        (10, 'Faf du Plessis', 'South Africa', 'Right-hand', 'Right-arm', 160, 5500, None, 40, None),
        (11, 'Ross Taylor', 'New Zealand', 'Right-hand', 'Right-arm', 190, 7000, 0, 42, None),
        (12, 'Mushfiqur Rahim', 'Bangladesh', 'Right-hand', 'Right-arm', 130, 3500, 0, 30, None),
        (13, 'Shikhar Dhawan', 'India', 'Left-hand', 'Right-arm', 170, 6500, 0, 45, None),
        (14, 'Jason Holder', 'West Indies', 'Right-hand', 'Right-arm', 120, 2000, 150, 20, 25),
        (15, 'Kagiso Rabada', 'South Africa', 'Right-hand', 'Right-arm', 100, 500, 120, 5, 22),
        (16, 'Jasprit Bumrah', 'India', 'Right-hand', 'Right-arm', 90, 50, 150, 2, 20),
        (17, 'Trent Boult', 'New Zealand', 'Right-hand', 'Left-arm', 110, 500, 110, 10, 25),
        (18, 'Pat Cummins', 'Australia', 'Right-hand', 'Right-arm', 80, 300, 90, 7, 30),
        (19, 'Rashid Khan', 'Afghanistan', 'Right-hand', 'Right-arm', 70, 100, 120, 5, 18),
        (20, 'Mohammad Amir', 'Pakistan', 'Left-hand', 'Left-arm', 60, 50, 80, 1, 20),
        (21, 'Andre Russell', 'West Indies', 'Right-hand', 'Right-arm', 50, 1000, 70, 20, 15),
        (22, 'Mitchell Starc', 'Australia', 'Left-hand', 'Left-arm', 80, 200, 120, 5, 22),
        (23, 'Jos Buttler', 'England', 'Right-hand', 'Right-arm', 110, 3500, None, 35, None),
        (24, 'Rashid Khan', 'Afghanistan', 'Right-hand', 'Right-arm', 70, 0, 120, 5, 18),
        (25, 'David Miller', 'South Africa', 'Left-hand', 'Right-arm', 100, 2500, None, 25, None),
        (26, 'Martin Guptill', 'New Zealand', 'Right-hand', 'Right-arm', 130, 4500, None, 35, None),
        (27, 'Chris Gayle', 'West Indies', 'Left-hand', 'Right-arm', 120, 3500, 5, 30, 60),
        (28, 'Moeen Ali', 'England', 'Left-hand', 'Right-arm', 90, 2500, 70, 25, 30),
        (29, 'Rashid Khan', 'Afghanistan', 'Right-hand', 'Right-arm', 70, 100, 0, 5, 18),
        (30, 'Lasith Malinga', 'Sri Lanka', 'Right-hand', 'Right-arm', 120, 200, 130, 5, 20),
        (31, 'Chris Woakes', 'England', 'Right-hand', 'Right-arm', 80, 1000, 90, 15, 25),
        (32, 'Shakib Al Hasan', 'Bangladesh', 'Left-hand', 'Left-arm', 110, 4000, 120, 35, 22),
        (33, 'AB de Villiers', 'South Africa', 'Right-hand', 'Right-arm', 200, 8000, 10, 50, 30),
        (34, 'Kieron Pollard', 'West Indies', 'Right-hand', 'Right-arm', 150, 3500, 20, 40, 20),
        (35, 'David Miller', 'South Africa', 'Left-hand', 'Right-arm', 170, 5000, 5, 45, 25),
        (36, 'Moeen Ali', 'England', 'Left-hand', 'Right-arm', 140, 3500, 15, 55, 30)
    ]

    c.executemany('INSERT INTO CricketPlayer_Table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', CricketPlayer_Table_Data)

    Team_Table_Data = [
        (1, 'India', 'India', 'Ravi Shastri', 'Virat Kohli', 1),
        (2, 'Australia', 'Australia', 'Justin Langer', 'Steve Smith', 2),
        (3, 'New Zealand', 'New Zealand', 'Gary Stead', 'Kane Williamson', 3),
        (4, 'England', 'England', 'Chris Silverwood', 'Joe Root', 4),
        (5, 'Pakistan', 'Pakistan', 'Misbah-ul-Haq', 'Babar Azam', 5),
        (6, 'South Africa', 'South Africa', 'Mark Boucher', 'Faf du Plessis', 10),
        (7, 'West Indies', 'West Indies', 'Phil Simmons', 'Jason Holder', 14),
        (8, 'Bangladesh', 'Bangladesh', 'Russell Domingo', 'Mushfiqur Rahim', 12),
        (9, 'Sri Lanka', 'Sri Lanka', 'Mickey Arthur', 'Lasith Malinga', 30),
        (10, 'Afghanistan', 'Afghanistan', 'Lance Klusener', 'Rashid Khan', 19),
        (11, 'Ireland', 'Ireland', 'Graham Ford', 'Andrew Balbirnie', None),
        (12, 'Zimbabwe', 'Zimbabwe', 'Lalchand Rajput', 'Sean Williams', None),
        (13, 'Netherlands', 'Netherlands', 'Ryan Campbell', 'Pieter Seelaar', None),
        (14, 'Scotland', 'Scotland', 'Shane Burger', 'Kyle Coetzer', None),
        (15, 'UAE', 'UAE', 'Dougie Brown', 'Ahmed Raza', None),
        (16, 'South Africa A', 'South Africa', 'Mark Boucher', 'AB de Villiers', 33),
        (17, 'West Indies A', 'West Indies', 'Phil Simmons', 'Kieron Pollard', 34),
        (18, 'South Africa B', 'South Africa', 'Mark Boucher', 'David Miller', 35),
        (19, 'England A', 'England', 'Chris Silverwood', 'Moeen Ali', 36),
        (20, 'India A', 'India', 'Ravi Shastri', 'Virat Kohli', 1),
        (21, 'Australia A', 'Australia', 'Justin Langer', 'Steve Smith', 2)
    ]

    c.executemany('INSERT INTO Team_Table VALUES (?, ?, ?, ?, ?, ?)', Team_Table_Data)
    conn.commit()

    c.execute('''
        CREATE TABLE IF NOT EXISTS product_sales (
            product_id INTEGER,
            promotion_id INTEGER,
            cost_in_dollars INTEGER,
            customer_id INTEGER,
            date DATE,
            units_sold INTEGER
        )
    ''')

    product_sales_data = [
        (1, 1, 2, 1, '2022-04-01', 4),
        (3, 3, 6, 3, '2022-05-24', 6),
        (1, 2, 2, 10, '2022-05-01', 3),
        (1, 2, 3, 2, '2022-05-01', 9),
        (2, 2, 10, 2, '2022-05-01', 1),
        (9, 3, 1, 2, '2022-05-31', 5),
        (6, 1, 4, 1, '2022-04-07', 8),
        (6, 2, 2, 1, '2022-05-01', 12),
        (3, 3, 5, 1, '2022-05-25', 4),
        (3, 3, 6, 2, '2022-05-25', 6),
        (3, 3, 7, 3, '2022-05-25', 7),
        (2, 2, 12, 3, '2022-05-01', 1),
        (8, 2, 4, 3, '2022-05-01', 4),
        (9, 1, 1, 10, '2022-04-07', 2),
        (9, 5, 2, 3, '2022-04-06', 20),
        (10, 1, 3, 2, '2022-04-07', 4),
        (10, 1, 3, 1, '2022-04-01', 5),
        (3, 1, 6, 1, '2022-04-02', 10),
        (2, 1, 10, 10, '2022-04-04', 8),
        (2, 1, 11, 3, '2022-04-05', 6),
        (4, 2, 2, 2, '2022-05-02', 7),
        (5, 2, 8, 1, '2022-05-02', 7),
        (2, 3, 13, 1, '2022-05-30', 3),
        (1, 1, 2, 2, '2022-04-07', 3),
        (10, 2, 2, 3, '2022-05-02', 9),
        (11, 1, 5, 1, '2022-04-03', 9),
        (5, 1, 7, 10, '2022-04-02', 9),
        (5, 4, 8, 1, '2022-06-06', 8),
        (1, 1, 2, 2, '2022-04-02', 9),
        (5, 2, 8, 15, '2022-05-01', 2),
        (8, 2, 4, 3, '2022-05-11', 1),
        (8, 2, 4, 3, '2022-06-11', 1)
    ]

    c.executemany('''INSERT INTO product_sales VALUES (?, ?, ?, ?, ?, ?) ''', product_sales_data)
    conn.commit()

    # Create hulk_business table
    c.execute('''
        CREATE TABLE IF NOT EXISTS hulk_business (
            business_id VARCHAR(50),
            name VARCHAR(255),
            neighborhood VARCHAR(255),
            address VARCHAR(255),
            city VARCHAR(255),
            state VARCHAR(255),
            postal_code VARCHAR(10),
            latitude DECIMAL(10, 6),
            longitude DECIMAL(10, 6),
            stars DECIMAL(3, 1),
            review_count INT,
            is_open INT,
            categories VARCHAR(255)
        )
    ''')

    hulk_business_data = [
        ('0EF5UGrbnn1ToEfqbT09sQ', 'Alpine Autoworks', None, '1522 Broadway St', 'Port Coquitlam', 'BC', 'V3C 6M2', 49.26, -122.781, 4.5, 21, 1, 'Auto Repair;Automotive'),
        ('0jDvRJS-z9zdMgOUXgr6rA', 'Sunfare', None, '811 W Deer Valley Rd', 'Phoenix', 'AZ', '85027', 33.683, -112.085, 5.0, 27, 1, 'Personal Chefs;Food;Gluten-Free;Food Delivery Services;Event Planning & Services;Restaurants'),
        ('2BOgZrF1zKuhaZiOLn_7jQ', 'Zookz Sandwiches', None, '100 E Camelback Rd, Ste 164', 'Phoenix', 'AZ', '85012', 33.509, -112.071, 4.5, 186, 1, 'Sandwiches;Breakfast & Brunch;Restaurants'),
        ('2FayPIK4GgyK7W7iVJyRLw', 'Five Guys', None, '5000 S Arizona Mills Cir, Ste 365', 'Tempe', 'AZ', '85282', 33.382, -111.964, 3.0, 140, 1, 'Burgers;Restaurants;Fast Food'),
        ('2v2M2e5sHCBGfX5V7VsCfg', 'Panda Express', None, '206 S Decatur Blvd', 'Las Vegas', 'NV', '89107', 36.171, -115.209, 2.5, 105, 1, 'Chinese;Fast Food;Restaurants;American (Traditional)'),
        ('3QPfMJAc_pqj_7l4-91VLg', 'North York Optometric Clinic', 'North York', '4983A Yonge Street', 'Toronto', 'ON', 'M2N 5N5', 43.762, -79.411, 4.5, 25, 1, 'Eyewear & Opticians;Health & Medical'),
        ('57PSHmEDjQvdCfUuQoh3dQ', 'Phoenix Water Damage Restoration', 'North Mountain', '2155 W Pinnacle Peak Rd, Ste 201', 'Phoenix', 'AZ', '85027', 33.711, -112.117, 5.0, 7, 1, 'Home Services;Damage Restoration'),
        ('59uVbCUhF3z2O9n6zVXugA', 'Big O Tires', 'Spring Valley', '3775 S Durango Dr', 'Las Vegas', 'NV', '89147', 36.111, -115.282, 3.5, 27, 1, 'Tires;Auto Repair;Automotive'),
        ('5KDLz0IoQeZNLiUvn9O6Lw', "Dan's Auto Service", 'East York', '407 Donlands Avenue', 'Toronto', 'ON', 'M4J 3S2', 43.695, -79.337, 2.5, 8, 1, 'Auto Repair;Automotive'),
        ('6FmJM2SYWoUv_DC8FA7hpg', '1st Choice Storage Solutions', 'Southeast', '6360 S Pecos Rd', 'Las Vegas', 'NV', '89120', 36.071, -115.107, 3.5, 11, 1, 'Local Services;Self Storage;Movers;Professional Services'),
        ('6HmDqeNNZtHMK0t2glF_gg', 'Dry Clean Vegas', 'Southeast', '2550 Windmill Ln, Ste 100', 'Las Vegas', 'NV', '89123', 36.042, -115.118, 1.0, 4, 1, 'Dry Cleaning & Laundry;Laundry Services;Local Services;Dry Cleaning'),
        ('7fIOpL6qAt7yf9ziXz3i1A', 'Any Lab Test Now', None, '7801 N Lamar Blvd, Ste D112', 'Austin', 'TX', '78752', 30.346, -97.719, 4.5, 33, 1, 'Laboratory Testing;Diagnostic Services;Health & Medical;Medical Centers'),
        ('7HFBt7Z-bCmCZ-gIUV5z9w', 'Bloomington Eye Care', 'Bloomington', '10430 S Cicero Ave', 'Oak Lawn', 'IL', '60453', 41.708, -87.741, 5.0, 6, 1, 'Optometrists;Eyewear & Opticians;Health & Medical'),
        ('8GHOIYD-XPjyX_aIlBGYxA', 'Cheerfully Made Goods + Markets', None, '72 Mill St', 'Almonte', 'ON', 'K0A 1A0', 45.225, -76.19, 5.0, 5, 1, 'Shopping;Arts & Crafts;Fashion;Markets;Local Services;Food;Event Planning & Services;Gift Shops'),
        ('95JMmaa1mgpT8XeLI-bUHQ', 'Princess Seafood Market & Deli', 'Downtown', '114 N School St', 'Boonville', 'CA', '95415', 39.152, -123.368, 4.5, 86, 1, 'Seafood;Delis;Restaurants'),
        ('9jcdBZ5KnVvOaK_RjdCB7g', 'Candlewood Suites Ft. Lauderdale Airport/Cruise', None, '1120 W State Road 84', 'Fort Lauderdale', 'FL', '33315', 26.1, -80.157, 4.0, 61, 1, 'Hotels & Travel;Hotels'),
        ('ab0qE1mwACrlH-7eC5TZSQ', 'Carbone', None, '1900 Silverado Ranch Blvd', 'Las Vegas', 'NV', '89123', 36.015, -115.147, 4.0, 1252, 1, 'Italian;Pizza;Restaurants;Bars;Nightlife'),
        ('abkE8fJ1l3BQLH4jYc7Nnw', 'The Tobacco Company', 'Shockoe Slip', '1201 E Cary St', 'Richmond', 'VA', '23219', 37.53, -77.433, 4.0, 1232, 1, 'Tobacco Shops;Shopping;Bars;Nightlife'),
        ('ak1V2DuPEK5u__zBmXkAqA', 'Michelin Repair Center', 'Southeast', '6944 E Hampton Ave', 'Mesa', 'AZ', '85209', 33.393, -111.688, 4.0, 9, 1, 'Tires;Auto Repair;Automotive'),
        ('AlNMRr-ATm3_cjsHbMQF5g', 'Barrie Carpet and Upholstery Cleaning', None, '367 Mill St', 'Barrie', 'ON', 'L4N 6J9', 44.394, -79.686, 5.0, 9, 1, 'Carpet Cleaning;Local Services;Home Services'),
        ('bDjsaa1fD3QfBnbWjEA9Zw', 'Republic Ramen + Noodles', 'Downtown', '213 N Orange St', 'Glendale', 'CA', '91203', 34.148, -118.255, 4.0, 1043, 1, 'Japanese;Noodles;Ramen;Restaurants'),
        ('CX8pfLn7Bk9o2-8yDMp_2w', 'The UPS Store', None, '4815 E Carefree Hwy, Ste 108', 'Cave Creek', 'AZ', '85331', 33.798, -111.977, 1.5, 5, 1, 'Notaries;Printing Services;Local Services;Shipping Centers'),
        ('eGBrr03fjCFEEzTq-z1fBw', 'Chandler AZ Handyman', 'Chandler', '4116 W Kitty Hawk', 'Chandler', 'AZ', '85226', 33.307, -112.006, 5.0, 7, 1, 'Handyman;Home Services'),
        ('eJrN1vW-s4eNJ1FgbBwABw', 'Nys Best Electric', 'Paradise Valley', '7000 N 16th St', 'Phoenix', 'AZ', '85020', 33.55, -112.042, 5.0, 39, 1, 'Electricians;Home Services;Professional Services;Local Services'),
        ('G5ERFWvPfHy7IDAUYlWL2A', 'All Colors Mobile Bumper Repair', None, '7137 N 28th Ave', 'Phoenix', 'AZ', '85051', 33.448, -112.074, 1.0, 4, 1, 'Auto Detailing;Automotive'),
        ('g6KfICYxIFoXnz7KHzQDpw', 'Chase Bank', None, '705 S Green Valley Pkwy', 'Henderson', 'NV', '89052', 36.003, -115.084, 2.0, 6, 1, 'Financial Services;Banks & Credit Unions'),
        ('G8_i64QVjdUy7ts_6TeU6w', 'VCA Woodland South Animal Hospital', 'Southside', '2816 Philips Hwy', 'Jacksonville', 'FL', '32207', 30.313, -81.628, 4.0, 34, 1, 'Pets;Veterinarians'),
        ('G8wR2Oum23tqvfTgEXlIGQ', 'Winners Bar & Grill', None, '2971 Whipple Ave NW', 'Canton', 'OH', '44708', 40.839, -81.384, 4.0, 10, 1, 'American (Traditional);Sports Bars;Nightlife;Bars;Restaurants'),
        ('gqUVjTjCpV8xLVEc4jJwQA', 'CrossFit FSI', 'South Las Vegas', '7585 Commercial Way, Ste 180', 'Henderson', 'NV', '89011', 35.994, -115.071, 4.5, 7, 1, 'Gyms;Fitness & Instruction'),
        ('GRDy1pFhlFOEHy_JBfSVwA', "Carmine's Italian Bakery", 'Spring Valley', '3170 E Sunset Rd, Ste D', 'Las Vegas', 'NV', '89120', 36.071, -115.092, 5.0, 152, 1, 'Food;Bakeries;Desserts;Coffee & Tea'),
        ('HZwqA6K_6QQzzp7P0f8AOg', "Landini's Pizzeria", 'Kearny Mesa', '1827 India St', 'San Diego', 'CA', '92101', 32.721, -117.168, 4.0, 1286, 1, 'Pizza;Restaurants'),
        ('JemtKt3WQZP6I0Qb2C2qCw', 'Just For You', 'Del Mar', '13038 Del Mar St', 'Garden Grove', 'CA', '92841', 33.769, -117.983, 5.0, 12, 1, 'Convenience Stores;Shopping;Tobacco Shops;Vape Shops'),
        ('ju0PnXccU1tBUXZ1WAkoJg', 'Rachael E Morgan', 'Camelback East', '740 E Highland Ave', 'Phoenix', 'AZ', '85014', 33.508, -112.067, 5.0, 16, 1, 'Life Coach;Psychics & Astrologers;Supernatural Readings;Professional Services'),
        ('Kmqnj7mLd5KucU2PE64SPw', 'Steele Creek Animal Hospital', 'Steele Creek', '9729 S Tryon St', 'Charlotte', 'NC', '28273', 35.135, -80.937, 4.0, 15, 1, 'Pets;Veterinarians;Pet Services'),
        ('lbxfIXUNUdSRO2t7z2PxPA', 'Budget Car Rental', None, '7125 E Shea Blvd, Ste 101', 'Scottsdale', 'AZ', '85254', 33.581, -111.928, 2.0, 6, 1, 'Hotels & Travel;Car Rental'),
        ('Lhtl6hEr4BaAR4aA3RQDNQ', 'Dairy Queen', None, '475 W Craig Rd', 'North Las Vegas', 'NV', '89032', 36.239, -115.148, 2.0, 57, 1, 'Food;Ice Cream & Frozen Yogurt'),
        ('lLAcGhvKl6ePcrz74HmtNg', 'Curves', None, '20235 N Cave Creek Rd, Ste 110', 'Phoenix', 'AZ', '85024', 33.674, -112.034, 3.0, 6, 1, 'Gyms;Fitness & Instruction'),
        ('LlOulew5vekJYUeevG7E1w', 'Ahwatukee Commons Veterinary Hospital', 'Ahwatukee', '4902 E Warner Rd, Ste 14', 'Phoenix', 'AZ', '85044', 33.333, -111.978, 4.0, 29, 1, 'Veterinarians;Pets;Pet Groomers;Pet Services'),
        ('lLRL6XDkLJUbQ6tJT28hUQ', 'Panera Bread', None, '10250 W McDowell Rd, Ste 120', 'Avondale', 'AZ', '85392', 33.467, -112.301, 2.5, 133, 1, 'Bakeries;Sandwiches;Cafes;Restaurants;Salad;Soup'),
        ('mzyeFJGhiNnqY7bH4W6mFw', 'Echo Hill Playground', None, '8015 W Glenrosa Ave', 'Phoenix', 'AZ', '85033', 33.495, -112.204, 2.0, 5, 1, 'Parks;Playgrounds'),
        ('NW8beR0L7I-Ifz1NfX5k0Q', 'Pappadeaux Seafood Kitchen', 'Northeast', '11975 E 40th Ave', 'Denver', 'CO', '80239', 39.772, -104.847, 3.5, 1023, 1, 'Seafood;Cajun/Creole;Restaurants;Bars'),
        ('o0sGS5hY95d6b1VLHnUzLw', 'Mainstreet Keg & Grill', 'Milliken', '126 Main St S', 'Newmarket', 'ON', 'L3Y 3Y7', 44.048, -79.456, 4.0, 16, 1, 'Sports Bars;Restaurants;Nightlife;Bars'),
        ('obtkepj5E9C25ocYpOK2fA', 'Naya Express', 'Chelsea', '20 W 23rd St', 'New York', 'NY', '10010', 40.742, -73.99, 4.0, 116, 1, 'Lebanese;Mediterranean;Restaurants;Middle Eastern'),
        ('oQ8go4yPKm2bAAEQ0fMHMg', '7-Eleven', 'Paradise Valley', '6801 N 32nd St', 'Phoenix', 'AZ', '85018', 33.523, -112.012, 2.0, 12, 1, 'Convenience Stores;Food;Automotive;Gas Stations'),
        ('oXig2Df5PXf8dDZjy_27_g', 'Bella Napoli', 'Sunrise', '1500 E Sunset Rd', 'Las Vegas', 'NV', '89119', 36.072, -115.124, 4.0, 204, 1, 'Italian;Restaurants'),
        ('p8keQs0xw0TzP0JjYPiZPQ', 'The Enfield Fox', None, '285 Enfield Place', 'Mississauga', 'ON', 'L5B 3Y6', 43.591, -79.636, 1.5, 3, 0, 'Bars;Restaurants;Pubs;British;Nightlife'),
        ('pbt3SBcEmxCfZPdnmU9tNA', 'The Cuyahoga Room', None, '740 Munroe Falls Ave', 'Cuyahoga Falls', 'OH', '44221', 41.14, -81.472, 1.0, 3, 0, 'Wedding Planning;Caterers;Event Planning & Services;Venues & Event Spaces'),
        ('pFc4n-CM9VI05zT6w38Mpw', "Abby's Closet", 'Downtown', '7301 SW Beveland St, Ste 200', 'Tigard', 'OR', '97223', 45.428, -122.768, 4.5, 5, 1, 'Formal Wear;Shopping;Fashion;Bridal'),
        ('Q-9xV2PFTRZh2fo6NL_6yA', 'Zen University', 'Ahwatukee', '4404 E Broadway Rd, Ste 108', 'Phoenix', 'AZ', '85040', 33.407, -112.015, 4.5, 12, 1, 'Tai Chi;Health & Medical;Professional Services;Martial Arts'),
        ('q2g-hEI9lEugvZ45HSwzVw', 'Fresh Off The Hook', 'Roosevelt', '4161 N 44th St', 'Phoenix', 'AZ', '85018', 33.508, -111.986, 4.0, 388, 1, 'Seafood;Restaurants;Cajun/Creole'),
        ('q4jWzJvwKQWZAPXr0GZYZg', 'Petvalu', 'Greece', '2674 W Ridge Rd', 'Rochester', 'NY', '14626', 43.214, -77.697, 4.5, 4, 1, 'Pet Stores;Pets'),
        ('rADSWp2iQbjv-FdEKzHbEQ', 'The Fry\'s Family Farm', 'Southwest', '6057 Westwood Blvd', 'Orlando', 'FL', '32821', 28.359, -81.49, 4.5, 11, 1, 'Farmers Market;Food;Specialty Food;Grocery;Shopping'),
        ('rrHt6ptD-vjuVqIksXxb6g', 'Green Planet Smoke Shop', 'Spring Valley', '7365 W Sahara Ave', 'Las Vegas', 'NV', '89117', 36.143, -115.245, 4.5, 49, 1, 'Shopping;Tobacco Shops;Head Shops;Vape Shops'),
        ('U3EUCP9H9Sdbjta6rqeB3A', 'B&H', None, '520 9th Ave', 'New York', 'NY', '10018', 40.754, -73.993, 3.5, 1833, 1, 'Electronics;Photography Stores & Services;Shopping;Local Services;Professional Services'),
        ('v3dt_tGgQcBI0bqeDKQQCA', 'Omni Dry Cleaners', 'Ahwatukee', '4729 E Ray Rd', 'Phoenix', 'AZ', '85044', 33.321, -111.981, 4.5, 11, 1, 'Dry Cleaning & Laundry;Laundry Services;Local Services'),
        ('vx9iHgEBP9Cy_3Or4O2JZQ', 'Bella On The Avenue', 'Scottsdale', '6941 N Hayden Rd, Ste 114', 'Scottsdale', 'AZ', '85250', 33.531, -111.907, 5.0, 46, 1, 'Hair Salons;Beauty & Spas;Nail Salons'),
        ('WdQP8kl9SzcOdubWz0Rs5g', 'Red Beard Bodywork And Structural Integration', 'Capitol', '301 S Bedford St', 'Madison', 'WI', '53703', 43.066, -89.389, 5.0, 10, 1, 'Rolfing;Health & Medical;Beauty & Spas;Massage'),
        ('wE-3J2xOKdJk5w_5YjsL0w', 'Zest', 'Greenwood Village', '8260 Northfield Blvd', 'Denver', 'CO', '80238', 39.786, -104.885, 4.5, 74, 1, 'Restaurants;American (New);Breakfast & Brunch'),
        ('wzyVjPCxZkTeSQQpZkDDVw', "Vincent's Nightclub", None, '25 S Arizona Pl', 'Chandler', 'AZ', '85225', 33.302, -111.839, 4.5, 49, 0, 'Nightlife;Bars;Dance Clubs'),
        ('x-wvkn-JiPIUYzE23s9-2Q', 'Luvspun', None, '1701 McElderry St', 'Baltimore', 'MD', '21205', 39.305, -76.586, 5.0, 14, 1, 'Shopping;Fashion;Local Services;Used, Vintage & Consignment;Thrift Stores'),
        ('Xmdta4Hhxbw5fA4QheuVcQ', "Fox's Pizza Den", 'Elyria', '633 Lake Ave', 'Elyria', 'OH', '44035', 41.382, -82.109, 4.0, 3, 1, 'Pizza;Restaurants;Food'),
        ('xxCrRqqICzQyR0Q-iqCrNw', 'Subway', 'Plaza Midwood', '1300 The Plz', 'Charlotte', 'NC', '28205', 35.221, -80.81, 2.0, 13, 1, 'Fast Food;Sandwiches;Restaurants'),
        ('XZ-Mcg4XWabj44F_U6Ynzg', 'Zocalo Mexican Cuisine & Tequileria', None, '35 Stanhope St', 'Boston', 'MA', '02116', 42.347, -71.078, 4.0, 581, 1, 'Mexican;Bars;Restaurants;Nightlife'),
        ('yX3sW9bgfBkYVLHbPVHbPw', 'Sunshine Dry Cleaners & Alterations', 'North Las Vegas', '1524 W Carey Ave', 'North Las Vegas', 'NV', '89032', 36.201, -115.126, 4.0, 10, 1, 'Sewing & Alterations;Dry Cleaning & Laundry;Local Services;Laundry Services'),
        ('yzAB_pRwk8FJl3aILiiySA', 'CenturyLink Spring Valley', None, '4850 S Fort Apache Rd, Ste 100', 'Las Vegas', 'NV', '89147', 36.101, -115.297, 1.5, 35, 0, 'Home Services;Television Service Providers;Professional Services;Internet Service Providers;Utilities'),
        ('Z3RZmy8Lw6fsd5gk1p5jrQ', 'Salerno by Celestino', None, '1780 N Goldenrod Rd', 'Orlando', 'FL', '32807', 28.562, -81.276, 4.5, 82, 1, 'Italian;Restaurants;Pizza'),
        ('zID2tl8l5Mn5m2qZ6-2tvw', 'Bowl Of Heaven', 'Boulder City', '501 Nevada Hwy', 'Boulder City', 'NV', '89005', 35.979, -114.834, 4.5, 11, 1, 'Acai Bowls;Restaurants'),
        ('ZlD1pDl0G42iNuKk0CpgvQ', 'AZ Transmissions', 'Southwest', '4131 E University Dr', 'Phoenix', 'AZ', '85034', 33.421, -112.014, 3.5, 10, 1, 'Transmission Repair;Auto Repair;Automotive')
    ]

    c.executemany(''' INSERT INTO hulk_business VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''', hulk_business_data)
    conn.commit()

    questions = [
        ("Welcome to the ICC World Cup database, where the excitement of cricket unfolds! Within the 'icc_world_cup' table, we've neatly organized columns for Team_1, Team_2, and Winner. Your mission: unearth the total matches played, victories secured, and defeats encountered by each team. Your goal is to present this data sorted by the number of wins, revealing the true champions of the cricketing world!", 
         [("India", 2, 2, 0), ("NZ", 1, 1, 0), ("Eng", 2, 1, 1), ("Aus", 2, 1, 1), ("SL", 2, 0, 2), ("SA", 1, 0, 1)]),
        ("Can you devise a query to calculate both the count of new customers and repeated customers for each order date from the provided Customer_orders table? Provide the result sorted in ascending order by order date, with the format: order_date, new_customer_count, repeat_customer_count.", 
         [('2022-01-01', 3, 0), ('2022-01-02', 2, 1), ('2022-01-03', 1, 2)]),
        ("Given is a table 'Entries', which contains the details of employees' entries in a company, specifying the resources they use. However, each employee can only enter a floor once per day. There's a loophole where if the same person has different email IDs, they can enter multiple times. Your task is to find, for each employee name, the total number of entries, the most visited floor, and the resources they used. Present the results in the format: name, total_visits, most_visited_floor, resources_used.", 
         [('A', 3, 1, 'CPU,DESKTOP'), ('B', 3, 2, 'DESKTOP,MONITOR')]),
        ("Consider two tables: 'Person' and 'Friend'. Write a query to retrieve the PersonID, Name, number of friends, and total score of individuals who have friends with a combined score exceeding 100. This query will help identify individuals with significant social connections and academic achievements. Give your result in the formate : personid, total_friend_score, no_of_friends,	person_name", 
         [(2, 115, 2, 'Bob'), (4, 101, 3, 'Tara')]),
        ('''Consider two tables: 'Tripes' and 'Users_Details', Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03" Round Cancellation Rate to two decimal points. The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day. Give your result in the formate : request_at, cancelled_trip_count, total_trips, cancelled_percent''', 
         [('2013-10-01', 1, 3, 33.33), ('2013-10-02', 0, 2, 0.0), ('2013-10-03', 1, 2, 50.0)]),
        ('''You need to write an SQL query to analyze the payment processing time for each order. **Payment Processing Time**: The time it took (in minutes) to process the payment for the order. This should be calculated as the difference between the paid time of the current ticket and the paid time of the previous ticket for the same order. If there is no previous ticket for the same order, the payment processing time should be considered as None for that ticket. **Average Payment Processing Time**: The average payment processing time (in minutes) for all tickets of the same order. This should be calculated as a window function, averaging the payment processing times for all tickets of the same order. Your query should return results for all tickets, ordered by Order ID and Paid Time, Round the payment_time and Average Payment_time upto 6 decimal points. Output Order Of columns : Order_id, Order_status, brand, locality, city, payment_time , Average Payment_time''', 
         [(101, "Completed", "Brand A", "Locality X", "City 1", None, 5.0), (101, "Completed", "Brand A", "Locality X", "City 1", 5.0, 5.0), (102, "Failed", "Brand B", "Locality Y", "City 2", None, 10.0), (102, "Failed", "Brand B", "Locality Y", "City 2", 10.0, 10.0), (103, "Completed", "Brand C", "Locality Z", "City 3", None, None), (104, "Completed", "Brand D", "Locality X", "City 1", None, 5.0), (104, "Completed", "Brand D", "Locality X", "City 1", 5.0, 5.0), (105, "Completed", "Brand E", "Locality Y", "City 2", None, None), (106, "Completed", "Brand F", "Locality Z", "City 3", None, 5.0), (106, "Completed", "Brand F", "Locality Z", "City 3", 5.0, 5.0), (107, "Completed", "Brand G", "Locality X", "City 1", None, None), (108, "Completed", "Brand H", "Locality Y", "City 2", None, None), (109, "Completed", "Brand I", "Locality Z", "City 3", None, 5.0), (109, "Completed", "Brand I", "Locality Z", "City 3", 5.0, 5.0), (110, "Completed", "Brand J", "Locality X", "City 1", None, None) ]),
        ('''Consider a table named transactions representing financial transactions in a bank. Your task is to write a query to find the account id's that have had at least three consecutive Positive transactions . Display the account_id, the starting date of the consecutive transactions, and the ending date of the consecutive transactions. Output Order Of columns : account_id, start_date, end_date''',
         [(101, '2023-01-01', '2023-01-30'), (102, '2023-01-02', '2023-01-25')]),
        ('''Write a SQL query to find the "player_name", "country" & "runs_scored" of players who have scored more than 5000 runs. Rank the players based on their "runs_scored" in descending order, and assign the rank as "Top Scorer, " "High Scorer, " or "Moderate Scorer" based on the following conditions: "Top Scorer": Rank 1. "High Scorer": Rank 2 to 5 (inclusive). "Moderate Scorer": Rank 6 and above. Output Order Of columns : player_name, country, runs_scored, scoring_rank''',
         [('Virat Kohli', 'India', 12000, 'Top Scorer'), ('Joe Root', 'England', 9000, 'High Scorer'), ('Steve Smith', 'Australia', 8000, 'High Scorer'), ('Rohit Sharma', 'India', 8000, 'High Scorer'), ('AB de Villiers', 'South Africa', 8000, 'High Scorer'), ('David Warner', 'Australia', 7000, 'Moderate Scorer'), ('Ross Taylor', 'New Zealand', 7000, 'Moderate Scorer'), ('Kane Williamson', 'New Zealand', 6500, 'Moderate Scorer'), ('Shikhar Dhawan', 'India', 6500, 'Moderate Scorer'), ('Babar Azam', 'Pakistan', 6000, 'Moderate Scorer'), ('Faf du Plessis', 'South Africa', 5500, 'Moderate Scorer')]),
        ('''You've been tasked with identifying the top 5 products that generated the highest total revenue during the first half of 2022, specifically from January to June. You aim to find these products and report their product IDs and total revenues. Order the results in descending order of Total revenue. Total_revenue for each product is a sum of (cost * unit_solds). Output Order Of columns : product_id, revenue''',
         [(2, 207), (3, 201), (5, 199), (1, 65), (6, 56)]),
        ('''You are an aspiring entrepreneur and are looking for the best business in several states to study their case study. List the top 5 states where the majority of businesses have received five stars. You have to find out the State name and the number of 5- star businesses in the state, and the results are sorted according to the number of 5- star firms. If there is a tie for the number of businesses in the different states, return all separate states. If the results from two states are identical, order the states alphabetically. Output Order Of columns : state, num_5_star_businesses''',
         [("AZ", 6), ("ON", 2), ("CA", 1), ("IL", 1), ("MD", 1)])
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
        ],
        [
            {
                "Column Name": ["ticket_id", "order_id", "paid_time", "reason"],
                "Data Type": ["INTEGER", "INTEGER", "DATETIME", "TEXT"],
                "Description": ["Unique identifier for each ticket", "Order ID associated with the ticket", "Time when the payment was made", "Reason for the ticket (e.g., Successful Payment, Refund Issued)"]
            },
            {
                "Column Name": ["order_id", "order_status", "mid"],
                "Data Type": ["INTEGER", "TEXT", "INTEGER"],
                "Description": ["Unique identifier for each order", "Status of the order (e.g., Completed, Failed)", "ID of the associated merchant"]
            },
            {
                "Column Name": ["mid", "brand", "locality", "city"],
                "Data Type": ["INTEGER", "TEXT", "TEXT", "TEXT"],
                "Description": ["Unique identifier for each merchant", "Brand name of the merchant", "Locality of the merchant", "City of the merchant"]
            }
        ],
        {
                "Column Name": ["transaction_id", "account_id", "transaction_date", "amount"],
                "Data Type": ["INT", "INT", "DATE", "DECIMAL(10, 2)"],
                "Description": [ "Unique identifier for each transaction", "ID of the account associated with the transaction", "Date of the transaction", "Amount of the transaction" ]
        },
        [
            {
                "Column Name": ["player_id", "player_name", "country", "batting_style", "bowling_style", "matches_played", "runs_scored", "wickets_taken", "batting_average", "bowling_average"],
                "Data Type": ["INTEGER", "TEXT", "TEXT", "TEXT", "TEXT", "INTEGER", "INTEGER", "INTEGER", "DECIMAL(5,2)", "DECIMAL(5,2)"],
                "Description": ["Unique identifier for each player", "Name of the player", "Country of the player", "Batting style of the player", "Bowling style of the player", "Total matches played by the player", "Total runs scored by the player", "Total wickets taken by the player", "Batting average of the player", "Bowling average of the player"]
            },
            {
                "Column Name": ["team_id", "team_name", "country", "coach", "captain", "player_id"],
                "Data Type": ["INTEGER", "TEXT", "TEXT", "TEXT", "TEXT", "INTEGER"],
                "Description": ["Unique identifier for each team", "Name of the team", "Country of the team", "Coach of the team", "Captain of the team", "ID of the player associated with the team"]
            }
        ],
        {
                "Column Name": ["product_id", "promotion_id", "cost_in_dollars", "customer_id", "date", "units_sold"],
                "Data Type": ["INT", "INT", "INT", "INT", "DATE", "INT"],
                "Description": ["Identifier for the product", "Identifier for the promotion", "Cost of the product in dollars", "Identifier for the customer", "Date of the sale", "Number of units sold"]
        },
        {
                "Column Name": ["business_id", "name", "neighborhood", "address", "city", "state", "postal_code", "latitude", "longitude", "stars", "review_count", "is_open", "categories"],
                "Data Type": ["VARCHAR(50)", "VARCHAR(100)", "VARCHAR(50)", "VARCHAR(100)", "VARCHAR(50)", "VARCHAR(20)", "VARCHAR(10)", "FLOAT", "FLOAT", "FLOAT", "INT", "INT", "VARCHAR(100)"],
                "Description": ["Identifier for the business", "Name of the business", "Neighborhood of the business", "Address of the business", "City where the business is located", "State where the business is located", "Postal code of the business location", "Latitude coordinate of the business location", "Longitude coordinate of the business location", "Rating of the business", "Number of reviews for the business", "Indicator if the business is open (1 for open, 0 for closed)", "Categories of the business"]
        }
    ]

    schema_title = [["Table : ICC_World_Cup"],["Table : Customer_orders"],["Table : Entries"],["Table : Person","Table : Friend"],["Table: Trips", "Table: Users_Details"],["Table: Ticket_Records", "Table: Order_Records", "Table: Mid_Records"],["Table: Customer_orders"],["Table: CricketPlayer_Table","Table: Team_Table"],["Table: Product_Sales"],["Table: Hulk_Business"]]
    expected_out_col = [["Team","Total_Matches_Played","Victories_Secured","Defeats_Encountered"],["order_date","new_customer_count","repeat_customer_count"],['name', 'total_visits', 'most_visited_floor', 'resources_used'], ['personid','total_friend_score','no_of_friends','person_name'],['request_at', 'cancelled_trip_count', 'total_trips', 'cancelled_percent'],['Order_id', 'Order_status', 'brand', 'locality', 'city', 'payment_time' , 'Average_Payment_time'],["account_id", "start_date", "end_date"],[ "player_name", "country", "runs_scored", "scoring_rank" ],["product_id", "revenue"],["state", "num_5_star_businesses"]]
    return conn, c, questions, schema_set, schema_title, expected_out_col
