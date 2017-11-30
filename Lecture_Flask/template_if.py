from flask import Flask, render_template
app = Flask(__name__)

@app.route('/template_if/<int:score>')
def template_if(score):
   return render_template('template_if.html', marks = score)

if __name__ == '__main__':
   app.run(debug = True)