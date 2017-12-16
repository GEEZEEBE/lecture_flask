from flask import Flask, render_template, request, url_for
import sqlite3 as sql
import uuid, time, datetime
from pagination_class import Pagination

app = Flask(__name__)

def create_table():
    conn = sql.connect('sqlite3_database.db')
    print ("Opened database successfully");
    
    conn.execute('CREATE TABLE pagination_list (uniqueId TEXT, insertDate TEXT)')
    print ("Table created successfully");
    
    conn.close()

def addrecord():
    try:
        with sql.connect("sqlite3_database.db") as con:
            cur = con.cursor()
            for i in range(200):
                time.sleep(0.01)
                uniqueId = str(uuid.uuid4())
                insertDate = str(datetime.datetime.now())
                cur.execute("INSERT INTO pagination_list (uniqueId,insertDate) VALUES (?,?)",(uniqueId,insertDate) )
            con.commit()
            msg = "Record successfully added" + con.total_changes()
    except:
        con.rollback()
        msg = "error in insert operation"
  
    finally:
        print(msg)
        con.close()
            
@app.route('/pagination_list/', defaults={'page': 1})
@app.route('/pagination_list/<int:page>')
def pagination_list(page):
    con = sql.connect("sqlite3_database.db")
    con.row_factory = sql.Row
   
    per_page = 10
    
    cur = con.cursor()
    
    query = "select count(*) cnt from pagination_list"
    total_count = cur.execute(query).fetchone()
    pagination = Pagination(page, per_page, total_count['cnt'])
    
    if page != 1:
        offset = per_page * (page - 1)
    else:
        offset = 0
           
    query = "select * from pagination_list " + "LIMIT ? OFFSET ?"
    rows = cur.execute(query,(per_page,offset)).fetchall()
   
    return render_template("pagination_list.html",rows = rows,pagination=pagination)

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

app.jinja_env.globals['url_for_other_page'] = url_for_other_page

if __name__ == '__main__':
#     create_table()
#     addrecord()
    
    app.run(debug = True)