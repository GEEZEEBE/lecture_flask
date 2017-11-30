from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_USERNAME'] = 'otter.oh@gmail.com'
# app.config['MAIL_PASSWORD'] = '******'
app.config['MAIL_SERVER']='smtp.naver.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'otter35@naver.com'
app.config['MAIL_PASSWORD'] = '*******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/mail_submit")
def mail_submit():
    msg = Message('Hello world!', sender = app.config['MAIL_USERNAME'], recipients = ['otter.oh@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
#     app.run(host='172.30.1.5', port='80', debug = True)
    app.run(host='0.0.0.0', debug = True)