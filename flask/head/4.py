from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>/<ad>/ph>/')
def success(name,ad,ph):
   return 'welcome %s %s %s' %(name,ad,ph)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      add = request.form['ad']
      phn = request.form['ph']
      return redirect(url_for('success',name = user, ad = add, ph = phn))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


app.run(debug = True)
