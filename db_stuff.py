import sqlite3

def db_init():
    # Connect to the database and create a cursor
    con = sqlite3.connect("497_Lost_n_Found.db")
    cur = con.cursor()

    # Create a "users" table if necessary
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(100) NOT NULL
        )
    """) # Add more user-related fields

    # Create a "lost_items" table if necessary
    cur.execute("""
        CREATE TABLE IF NOT EXISTS lost_items (
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        item_name VARCHAR(100) NOT NULL,
        description TEXT,
        date_lost DATE,
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


def db_new_user():
    return 0


def db_new_item():
    return 0


def db_edit_preferences(userID):
    return 0