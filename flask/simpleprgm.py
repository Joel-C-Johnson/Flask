from flask import Flask
app=Flask(__name__)

@app.route("/hai")
def hello():
  return "Hai"

app.run()
