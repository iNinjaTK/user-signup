from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_form():
    return render_template('signup_form.html')

@app.route("/", methods=['POST'])
def index():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    #confirm if any fields (username, password, verify_password) are empty
    if username == '':
        username_error = "That's not a valid username."
    if password == '':
        password_error = "That's not a valid password."
        password = ''
    if verify_password == '':
        verify_password_error = "Passwords don't match."
        verify_password = ''

    #confirm if username is not valid
    if " " in username:
        username_error = "Username cannot have blank space(s)."
    elif len(username) < 3 and not len(username) == 0:
        username_error = "Username cannot have less than three (3) characters."
    elif len(username) > 20:
        username_error = "Username cannot have more than twenty (20) characters."

    #confirm if password matches verify_password
    if not password == verify_password:
        password_error = "Passwords don't match."
        password = ''
        verify_password = ''

    #confirm if email is valid (like username, +@, +.)
    if "@" not in email or "." not in email or " " in email:
        email_error = "That's not a valid email address."
    elif len(email) < 3:
        email_error = "Email address cannot be less than three (3) characters."
    elif len(email) > 20:
        email_error = "Email address cannot be more than twenty (20) characters."

    if not username_error and not password_error and not verify_password_error and not email_error:
        # success message
        return render_template('successful_signup.html', name = username)
        #redirect('/valid-time?time={0}'.format(time))
    else:
        return render_template('signup_form.html', 
        username_error=username_error, 
        username=username, 
        password_error=password_error, 
        password=password, 
        verify_password_error=verify_password_error, 
        verify_password=verify_password, 
        email_error=email_error, 
        email=email)

@app.route("/successful")
def successful():
    username = request.form['username']
    return render_template('successful_signup.html', name = username)

app.run()