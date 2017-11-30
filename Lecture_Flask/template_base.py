from flask import Flask, render_template

app = Flask(__name__)

@app.route('/template_base/<user>')
def template_base(user):
   return render_template('template_base.html', myname = user)

if __name__ == '__main__':
   app.run(debug = True)