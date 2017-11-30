from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/httpmethod_success/<myname>')
def httpmethod_success(myname):
    return 'welcome '+myname

@app.route('/httpmethod',methods = ['POST', 'GET'])
def httpmethod():
   if request.method == 'POST':
      user = request.form['myname']
   else:
      user = request.args
   return redirect(url_for('httpmethod_success',myname = user))

if __name__ == '__main__':
   app.run(debug = True)