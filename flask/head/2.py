from flask import Flask
app=Flask(__name__)

@app.route("/")
def car():
    return "my car is audi"

app.run(debug=True)
