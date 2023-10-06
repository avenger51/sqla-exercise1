
"""Blogly application."""

from flask import Flask, render_template, request, redirect, flash, session, abort, current_app, url_for
from models import db, connect_db, User
#from flask_sqlalchemy import SQLAlchemy #NEEDED IN APP.PY?????
#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///blogly"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'typicalbs'

#db.init_app(app) THIS BREAKS BASIC HOME PAGE FUNCTIONALITY
connect_db(app)


#with db.app.app_context():  #no clue..
#dcreate_all()  #IS THIS NEEDED ON ALL SUBSEQUENT CODE?

#toolbar = DebugToolbarExtension(app) #THIS NEVER WORKS

#@app.route("/")
#def user_list():
#    """Get list of users"""
#    users = User.query.all()
#    return render_template("home.html", users=users)

@app.route("/", methods=['GET', 'POST'])
def add_user():
    
    """Add a new user to the database"""
    if request.method == 'POST':
        # Get user input from the form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        image_url = request.form['image_url']
        
        # Create a new User object and add it to the database
        new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
        db.session.add(new_user)
        db.session.commit()
        
        # Redirect to the user list page
        return redirect('/user_listing')
    
    return render_template("home.html")  # Pass user_id to the template



@app.route ('/user_listing')
def display_users():
      """Get list of users"""
      users = User.query.all()
      return render_template("user_listing.html", users=users) 

@app.route('/user_details/<int:user_id>')
def display_user_details(user_id):
    """Display user details based on user ID"""
    user = User.query.get_or_404(user_id)
    return render_template("user_details.html", user=user)

#NOTE:  CANNOT GET 'user_id' to function

#@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
#def edit_user_submit(user_id):
#    user = User.query.get_or_404(user_id)
#
#    if request.method == "POST":
#       
#        user.first_name = request.form['first_name']
#        user.last_name = request.form['last_name']
#        user.image_url = request.form['image_url']
#        
#    
#        db.session.commit()
#       
#        return redirect('/user_listing')  # Update this URL as needed
#
#    return render_template('edit_user.html', user=user)
#
##@app.route("/edit_user/<int:user_id>", methods=["GET"])
##def edit_user_form(user_id):
##    user = User.query.get_or_404(user_id)
#    return render_template('edit_user.html', user=user)










#ORIGINAL BROKEN:
#@app.route("/edit_user/<int:user_id>")
#def edit_user(user_id):
#      # NEED TO DISPLAY THE PAGE WITH FORMS/
#      #if request.method == 'POST':
#        user = User.query.get_or_404(user_id)
#       # if user is None:
#        # Handle the case where the user with the specified ID doesn't exist
#            #abort(404)
#        return render_template('edit_user.html', user=user)
#    
#@app.route("/edit_user/<int:user_id>", methods=["POST"])
#def users_edit(user_id):
#    """Show a form to edit an existing user"""
#   
#    
#    user_id.first_name = request.form['first_name']
#    user_id.last_name = request.form['last_name']
#    user_id.image_url = request.form['image_url']
#    
#    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
#    db.session.add(new_user)
#    db.session.commit()
#        
#        # Redirect to the user list page
#    return redirect('/user_listing')
#  
#   @app.route("/user_details/<int:user_id>/edit")

#ORIGINAL AND NOT SURE WHAT I WAS DOING WITH THIS:
#def display_user_details(user_id):
#    #SHOW A FORM TO ENTER A USER ID.
#   
#    user = User.query.get_or_404(user_id)
#    if user is None:
#        # Handle the case where the user with the specified ID doesn't exist
#        abort(404)
#     
#    # Perform some actions with the user data and return a response
#    return render_template("user_details.html", user=user)