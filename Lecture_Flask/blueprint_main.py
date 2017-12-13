from flask import Flask, render_template
import blueprint_sub

app = Flask(__name__)

# register blueprints
app.register_blueprint(blueprint_sub.app, url_prefix='/bp_subs')
# app.register_blueprint(blueprint_sub.app, url_prefix=blueprint_sub.app.name)
# app.register_blueprint(blueprint_sub.app)    

@app.route('/blueprint_base/<user>')
def template_base(user):
   return render_template('template_base.html', myname = user)

if __name__ == '__main__':
   app.run(debug = True)