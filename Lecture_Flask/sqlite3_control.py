from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sqlite3_home.html')

@app.route('/enternew')
def enternew():
    return render_template('sqlite3_submit.html')

@app.route('/addrecord',methods = ['GET','POST'])
def addrecord():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
         
            with sql.connect("sqlite3_database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin) \
               VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
      
        finally:
            con.close()
            return render_template("sqlite3_result.html",msg = msg)
    return render_template("sqlite3_result.html")

@app.route('/list')
def list():
    con = sql.connect("sqlite3_database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from students")
   
    rows = cur.fetchall();
    return render_template("sqlite3_list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)