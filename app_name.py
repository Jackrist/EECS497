from flask import Flask, request, jsonify, render_template, redirect, url_for
from jinja2 import Environment, FileSystemLoader, select_autoescape
import sqlite3
import db_stuff as db

app = Flask(__name__)

# jinja2 template environment initialization
tmplt_env = Environment(
    loader=FileSystemLoader("./"),
    autoescape=select_autoescape()
)

# Database initialization (if needed)
db.init()

# Define new (sometimes API ?) endpoints as needed below.

@app.route('/signup/', methods=['POST'])
def register_user():
    '''Handles user registration & initial preference setting.'''
    # 1. Grab html form values
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get ('email')
   
        # 2. (a) Call db func for adding new users
        db.new_user(username, password, email)
    # 4. Redirect or return a response
        return redirect(url_for('set_preferences')) # redirect to set_pref?  
    else:
        return "Invalid request method"
    

@app.route('/setpreferences/', methods=['GET', 'POST'])
def set_preferences():
    '''Set/update user notification preferences'''
    if request.method == 'POST':

        username = request.form.get('username')
        item_pickup = request.form.get ('item_pickup')
        item_dropoff = request.form.get ('item_dropoff')
        new_messages = request.form.get ('new_messages')

        # 2. (b) Retrieve user_id from "users" table
        user_id = db.retrieve_user_id(username)
        # 3. Call db func for setting preferences
        db.set_preferences(user_id, item_pickup, item_dropoff, new_messages)    
        # Redirect to home?
    else:
        compile = compile
    return 0


@app.route('/editpreferences/')
def edit_preferences():
    return 0


@app.route('/submitlost/')
def submit_lost_item():
    '''Adds a new item to the lost_items table.'''
    # 1. Grab html form values
    # 2. Call db func for adding new lost items
    db.lost_item()
    # 3. Redirect?


@app.route('/submitfound/')
def submit_found_item():
    '''Adds a new item to the found_items table.'''
    # 1. Grab html form values
    # 2. Call db func for adding found items
    db.found_item()
    # 3. Redirect?


@app.route('/home/') # REFER HERE FOR EXAMPLE OF CONTEXT CREATION AND TEMPLATE RENDERING !!!
def show_homepage():
    '''Deaf-friendly lost n' found homepage.'''
    
    # Context-gathering & combination
    logname, user_id = db.get_logged_in_user()
    losts = db.get_losts(user_id)
    founds = db.get_founds(user_id)
    context = {"logname": logname, "userID": user_id, "losts": losts, "founds": founds}

    return render_template('home.html', **context)


@app.route('/login/') # We want this to be the default page so that we can always get logged_in_user first for template rendering and personalization of other pages. 
def show_login():
    '''Deaf-friendly lost n' found login page.'''
    # Use set_logged_in_user() at some point in here


if __name__ == '__main__':
    app.run()

    # 