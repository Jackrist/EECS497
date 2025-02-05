from flask import Flask, request, jsonify, render_template, redirect, url_for
from jinja2 import Environment, FileSystemLoader, select_autoescape
import sqlite3
import db_stuff as db

app = Flask(__name__,template_folder='templates')

# jinja2 template environment initialization
tmplt_env = Environment(
    loader=FileSystemLoader("./"),
    autoescape=select_autoescape()
)

# Define new (sometimes API ?) endpoints as needed below.

@app.route('/signup/', methods=['GET', 'POST'])
def register_user():
    '''Handles user registration & initial preference setting.'''
    # 1. Grab html form values
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get ('email')
        # 2. (a) Call db func for adding new users
        db.new_user(username, password)
        # 4. Redirect or return a response
        return redirect(url_for('show_login')) # redirect to set_pref?  
    else: # 'GET'
        return render_template('signup.html')
    

@app.route('/preferences/', methods=['GET', 'POST'])
def set_preferences():
    '''Set/update user notification preferences'''
    if request.method == 'POST':

        userID = request.form.get('user_id')
        item_pickup = request.form.get ('item_pickup')
        item_dropoff = request.form.get ('item_dropoff')
        new_messages = request.form.get ('new_messages')

        db.set_preferences(userID, item_pickup, item_dropoff, new_messages)    
        return redirect(url_for('show_homepage'))
    else:
        logname, user_id = db.get_logged_in_user()
        context = {"logname": logname, "userID": user_id}

        return render_template('prefs.html', **context)


@app.route('/submitlost/', methods=['GET', 'POST'])
def submit_lost():
    '''Adds a new item to the lost_items table.'''
    if request.method == 'POST':
        userID = request.form.get('user_id')
        item_name = request.form.get ('item_name')
        description = request.form.get ('description')
        date_lost = request.form.get ('date_lost')
        location = request.form.get('location')

        db.lost_item(userID, item_name, description, date_lost, location)
        return redirect(url_for('show_account'))
    else: # GET
        logname, user_id = db.get_logged_in_user()
        context = {"logname": logname, "userID": user_id}

        return render_template('submitL.html', **context)


@app.route('/submitfound/', methods=['GET', 'POST'])
def submit_found():
    '''Adds a new item to the found_items table.'''
    if request.method == 'POST':
        userID = request.form.get('user_id')
        item_name = request.form.get ('item_name')
        description = request.form.get ('description')
        date_found = request.form.get ('date_found')
        location = request.form.get('location')

        db.found_item(userID, item_name, description, date_found, location)
        return redirect(url_for('show_account'))
    else: # GET
        logname, user_id = db.get_logged_in_user()
        context = {"logname": logname, "userID": user_id}

        return render_template('submitF.html', **context)


@app.route('/home/') # REFER HERE FOR EXAMPLE OF CONTEXT CREATION AND TEMPLATE RENDERING !!!
def show_homepage():
    '''Deaf-friendly lost n' found homepage.'''
    
    # Context-gathering & combination
    logname, user_id = db.get_logged_in_user()
    context = {"logname": logname, "userID": user_id}
    

    return render_template('home.html', **context)


@app.route('/', methods=['GET', 'POST']) # We want this to be the default page so that we can always get logged_in_user first for template rendering and personalization of other pages. 
def show_login():
    '''Deaf-friendly lost n' found login page.'''
    # Database initialization (if needed)
    db.init()
    # Use set_logged_in_user() at some point in here
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        verify = db.check_pswd(username, password)

        if verify:
            db.set_logged_in_user(username)
            return redirect(url_for('show_homepage'))
        else:
            return redirect(url_for('login_error'))
    else: # 'GET'
        return render_template('login.html')


@app.route('/reminders/', methods=['GET'])
def show_reminders():
    logname, user_id = db.get_logged_in_user()
    context = {"logname": logname, "userID": user_id}

    return render_template('reminders.html', **context)


@app.route('/account/', methods=['GET'])
def show_account():
    logname, user_id = db.get_logged_in_user()
    losts = db.get_losts(user_id)
    founds = db.get_founds(user_id)
    context = {"logname": logname, "userID": user_id, "losts": losts, "founds": founds}

    return render_template('account.html', **context)


@app.route('/about/', methods=['GET'])
def show_about():
    logname, user_id = db.get_logged_in_user()
    context = {"logname": logname, "userID": user_id}

    return render_template('about.html', **context)


@app.route('/loginerr/')
def login_error():
    return render_template('logerr.html')


if __name__ == '__main__':
    app.run()