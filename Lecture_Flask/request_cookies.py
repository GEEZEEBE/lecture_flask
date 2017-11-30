from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/request_cookies_submit')
def request_cookies_submit():
    return render_template('request_cookies_submit.html')

@app.route('/request_cookies_set',methods = ['POST', 'GET'])
def request_cookies_set():
    if request.method == 'POST':
       user = request.form['myname']
   
       resp = make_response(render_template('request_cookies_read.html'))
       resp.set_cookie('userID', user)
   
    return resp

@app.route('/request_cookies_get')
def request_cookies_get():
   myname = request.cookies.get('userID')
   return '<h1>welcome '+myname+'</h1>'

if __name__ == '__main__':
   app.run(debug = True)