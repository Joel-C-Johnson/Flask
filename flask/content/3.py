from flask import Flask
app=Flask(__name__)

@app.route('/jj/<name>')
def name(name):
    return "hai %s" %name

app.run(debug=True)
