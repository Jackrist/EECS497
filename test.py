from flask import Flask, request, jsonify
import sqlite3
import db_stuff

app = Flask(__name__)

# Database initialization (if needed)
db_stuff.db_init()

# Define new (sometimes API ?) endpoints as needed below.

@app.route('/signup/', methods=['POST'])
def register_user():
    '''Handles user registration & initial preference setting.'''
    # 1. Grab html form values
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get ('email')
   
        # 2. (a) Call db_stuff func for adding new users
        db_stuff.db_new_user(username, password, email)
    # 4. Redirect or return a response
        return jsonify({"message": "User registered uccessfully"})  
    else:
        return "Invalid request method"
    
@app.route('/preferences/')
def set_preferences():
    '''Set/update user notification preferences'''
    if request.method == 'POST':

        username = request.form.get('username')
        item_pickup = request.form.get ('item_pickup')
        item_dropoff = request.form.get ('item_dropoff')
        new_messages = request.form.get ('new_messages')

        # 2. (b) Retrieve user_id from "users" table
        user_id = db_stuff.db_retrieve_user_id(username)
        # 3. Call db_stuff func for setting preferences
        db_stuff.db_edit_preferences(user_id, item_pickup, item_dropoff, new_messages)    # 2. Redirect?

@app.route('/submitlost/')
def submit_lost_item():
    '''Adds a new item to the lost_items table.'''
    # 1. Grab html form values
    # 2. Call db_stuff func for adding new lost items
    db_stuff.db_lost_item()
    # 3. Redirect?

@app.route('/submitfound/')
def submit_found_item():
    '''Adds a new item to the found_items table.'''
    # 1. Grab html form values
    # 2. Call db_stuff func for adding found items
    db_stuff.db_found_item()
    # 3. Redirect?

@app.route('/')
def show_homepage():
    '''Deaf-friendly lost n' found homepage.'''

@app.route('/login/')
def show_login():
    '''Deaf-friendly lost n' found login page.'''


if __name__ == '__main__':
    app.run()

    # 