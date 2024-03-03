

import streamlit as st
import pymysql

# Create a connection object
cnx = pymysql.connect(user='root', password='admin@123',
                              host='127.0.0.1',
                              database='jawan')

# Create a cursor object
cursor = cnx.cursor()

# Create a table to store user details
table_name = 'user_details'
create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))"
cursor.execute(create_table_query)

# Get user input
name = st.text_input('Enter your name')
email = st.text_input('Enter your email')
password = st.text_input('Enter your password', type='password')

# Insert user details into the table
if st.button('Submit'):
    insert_query = f"INSERT INTO {table_name} (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, email, password))
    cnx.commit()
    st.success('User details have been successfully registered!')

# Close the cursor and connection objects
cursor.close()
cnx.close()