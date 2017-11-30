from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/request_sessions_submit')
def request_sessions_submit():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/request_sessions_out'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/request_sessions_in'></b>" + \
      "click here to log in</b></a>"

@app.route('/request_sessions_in', methods = ['GET', 'POST'])
def request_sessions_in():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('request_sessions_submit'))
    return render_template('request_sessions_submit.html')

@app.route('/request_sessions_out')
def request_sessions_out():
    session.pop('username', None)
    return redirect(url_for('request_sessions_submit'))

if __name__ == '__main__':
   app.run(debug = True)