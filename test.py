from flask import Flask, request, jsonify
import sqlite3
import db_stuff

app = Flask(__name__)

# Database initialization (if needed)
db_stuff.db_init()

# Define new (sometimes API ?) endpoints as needed below.

@app.route('/signup/')
def register_user():
    '''Handles user registration & initial preference setting.'''
    # 1. Grab html form values
    # 2. Call db_stuff func for adding new users
    # 3. Call db_stuff func for setting preferences
    # 4. Redirect?
    
@app.route('/preferences/')
def set_preferences():
    '''Set/update user notification preferences'''
    # 1. Call db_stuff func for setting preferences
    # 2. Redirect?

@app.route('/submit/')
def submit_lost_item():
    '''Adds a new item to the lost_items table.'''
    # 1. Grab html form values
    # 2. Call db_stuff func for adding new lost items
    # 3. Redirect?

@app.route('/')
def show_homepage():
    '''Deaf-friendly lost n' found homepage.'''

@app.route('/login/')
def show_login():
    '''Deaf-friendly lost n' found login page.'''


if __name__ == '__main__':
    app.run()