from flask import Flask
app=Flask(__name__)

#@app.route("/")
def mob():
    return "honor"

app.add_url_rule('/hh/',mob)
app.run(debug=True)
