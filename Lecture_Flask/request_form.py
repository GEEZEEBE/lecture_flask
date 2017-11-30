from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/request_form_submit')
def request_form_submit():
    return render_template('request_form_submit.html')

@app.route('/request_form_result',methods = ['POST', 'GET'])
def request_form_result():
    if request.method == 'POST':
        result = request.form
        return render_template("/request_form_result.html",result = result)

if __name__ == '__main__':
    app.run(debug = True)