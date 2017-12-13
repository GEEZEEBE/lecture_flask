from flask import Blueprint, Flask, redirect, url_for, request, render_template

# app = Flask(__name__)
app = Blueprint('/subs', __name__)

@app.route('/blueprint_success/<myname>')
def httpmethod_success(myname):
    return 'welcome '+ myname

@app.route('/blueprint_base/<user>',methods = ['POST', 'GET'])
def httpmethod(user):
#     return redirect(url_for('blueprint_sub.httpmethod_success',myname = user))
#     return 'welcome '+ user
    return render_template('template_base.html', myname = user)

if __name__ == '__main__':
    app.run(debug = True)