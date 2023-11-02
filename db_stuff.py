import sqlite3

def init():
    # Connect to the database and create a cursor
    con = sqlite3.connect("497_Lost_n_Found.db")
    cur = con.cursor()

    # Create a "users" table if necessary
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(255) NOT NULL
        )
    """) # Add more user-related fields

    # Create a "lost_items" table if necessary
    cur.execute("""
        CREATE TABLE IF NOT EXISTS lost_items (
        id INTEGER PRIMARY KEY,
        user_id INT,
        item_name VARCHAR(100) NOT NULL,
        description TEXT,
        date_lost DATE,
        location VARCHAR(100)
        )
    """) # Add more item-related fields

        # Create a "found_items" table if necessary
    cur.execute("""
        CREATE TABLE IF NOT EXISTS found_items (
        id INTEGER PRIMARY KEY,
        user_id INT,
        item_name VARCHAR(100) NOT NULL,
        description TEXT,
        date_found DATE,
        location VARCHAR(100)
        )
    """) # Add more item-related fields

    # Create a "notification_preferences" table if necessary
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notification_preferences (
        user_id INT PRIMARY KEY,
        item_pickup BOOLEAN,
        item_dropoff BOOLEAN,
        new_messages BOOLEAN
        )
    """) # Add more notification types

    # Commit the changes and close the connection
    con.commit()
    con.close()


# Helps track logged_in_user (Use on login page)
def set_logged_in_user(username):
    # Connect to the database and create a cursor
    con = sqlite3.connect("497_Lost_n_Found.db")
    cur = con.cursor()

    # Retrieve the user_id based on the username from the "users" table
    cur.execute("SELECT id FROM users WHERE username = ?", (username,))
    user_id = cur.fetchone()[0]

    # Tracks current user
    cur.execute("""DROP TABLE IF EXISTS logged_in_user""")
    cur.execute("""CREATE TABLE logged_in_user (
                id INT
                )""")
    cur.execute("""INSERT INTO logged_in_user
                VALUES (?)""", (user_id,))
    
    con.commit()
    con.close()


def get_logged_in_user():
     # Connect to the database and create a cursor
    con = sqlite3.connect("497_Lost_n_Found.db")
    cur = con.cursor()

    cur.execute("SELECT id FROM logged_in_user")
    user_id = cur.fetchone()[0]

    cur.execute("""SELECT username FROM users
                WHERE id = ?
                """, (user_id,))
    logname = cur.fetchone()[0]

    con.commit()
    con.close()

    return logname, user_id


def new_user(username, password):
    # Connect to the database and create a cursor
    con = sqlite3.connect("497_Lost_n_Found.db")
    # Creating a cursor makes a connection to connect theSQL server
    cur = con.cursor()
    cur.execute(""" 
                INSERT INTO users
                VALUES(?, ?, ?)
                """, (0, username, password,))
    
    con.commit()
    con.close()


def lost_item(user_id, item_name, description, date_lost, location):
    # Connect to the database and create a cursor
    con = sqlite3.connect("497_Lost_n_Found.db")
    # Creating a cursor makes a connection to connect the SQL server
    cur = con.cursor()
    cur.execute ("""
    INSERT INTO lost_items
    VALUES (?, ?, ?, ?, ?, ?)
    """, (0, user_id, item_name, description, date_lost, location,))
    con.commit()
    con.close()


def found_item(user_id, item_name, description, date_found, location):
    # Connect to the database and create a cursor
    con = sqlite3.connect("497_Lost_n_Found.db")
    # Creating a cursor makes a connection to connect the SQL server
    cur = con.cursor()
    cur.execute ("""
    INSERT INTO found_items
    VALUES (?, ?, ?, ?, ?, ?)
    """, (0, user_id, item_name, description, date_found, location,))
    con.commit()
    con.close()


def set_preferences(user_id, item_pickup, item_dropoff, new_messages):
    # Connect to the database and create a cursor
    con = sqlite3.connect("497_Lost_n_Found.db")
    # Creating a cursor makes a connection to connect the SQL server
    cur = con.cursor()
    cur.execute ("""INSERT INTO notification_preferences
                 VALUES (?, ?, ?, ?)
                 """, (user_id, item_pickup, item_dropoff, new_messages,))
    con.commit()
    con.close()


def edit_preferences(user_id, item_pickup, item_dropoff, new_messages):
    # Connect to the database and create a cursor
    con = sqlite3.connect("497_Lost_n_Found.db")
    # Creating a cursor makes a connection to connect the SQL server
    cur = con.cursor()
    cur.execute ("""
                 UPDATE notification_preferences
                 SET item_pickup = ?, item_dropoff = ?, new_messages = ?
                 WHERE user_id = ?
                 """, (item_pickup, item_dropoff, new_messages, user_id,))
    con.commit()
    con.close()

def get_losts(user_id):
    # Connect to the database and create a cursor
    con = sqlite3.connect("497_Lost_n_Found.db")
    # Creating a cursor makes a connection to connect the SQL server
    cur = con.cursor()
    cur.execute ("""
                 SELECT id, item_name, description, date_lost, location
                 FROM lost_items WHERE user_id = ?
                 """, (user_id,))
    
    losts = cur.fetchall()

    con.commit()
    con.close()

    return losts


def get_founds(user_id):
    # Connect to the database and create a cursor
    con = sqlite3.connect("497_Lost_n_Found.db")
    # Creating a cursor makes a connection to connect the SQL server
    cur = con.cursor()
    cur.execute ("""
                 SELECT id, item_name, description, date_found, location
                 FROM found_items WHERE user_id = ?
                 """, (user_id,))
    
    founds = cur.fetchall()

    con.commit()
    con.close()

    return founds


def check_pswd(user, pswd):
    # Connect to the database and create a cursor
    con = sqlite3.connect("497_Lost_n_Found.db")
    # Creating a cursor makes a connection to connect the SQL server
    cur = con.cursor()
    cur.execute ("""
                 SELECT password
                 FROM users WHERE username = ?
                 """, (user,))
    
    password = cur.fetchone()[0]

    con.commit()
    con.close()

    if password == pswd:
        return True
    else:
        return False