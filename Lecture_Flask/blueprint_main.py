from flask import Flask, render_template
import blueprint_sub

app = Flask(__name__)
app.register_blueprint(blueprint_sub.app)    #, url_prefix='/pages'

@app.route('/template_base/<user>')
def template_base(user):
   return render_template('template_base.html', myname = user)

if __name__ == '__main__':
   app.run(debug = True)