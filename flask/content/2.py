from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/user/<user>')
def user(user):
    return "hi %s" %user

@app.route('/guest/<guest>')
def guest(guest):
    return "hi %s" %guest

@app.route('/un/<un>')
def un(un):
    if un=="joel":
        return redirect(url_for('user'))
    else:
        return redirect(url_for('guest',guest=john))

app.run(debug=True)
