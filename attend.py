import os
from flask import Flask, render_template, redirect, url_for, escape, request
from datetime import datetime
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def new():
   return render_template('homeat.html')


@app.route('/enternew')
def new_entry():
   return render_template('entryat.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      

         na = request.form['na']
         nb = request.form['nb']
         nc = request.form['nc']
    
      
         
         with sql.connect("t16.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO grp (na)VALUES (?)",(na,))
            cur.execute("INSERT INTO gr (nb,nc)VALUES (?,?)",(nb,nc))

            con.commit()
            ms = "Record added"
      
      
      
         return render_template("result1.html",ms = ms)
         con.close()



@app.route('/add')
def getid():
         return render_template('idw.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      nd= request.form['nd']
      na=nd
      con = sql.connect("t16.db")
      con.row_factory = sql.Row
   
      cur = con.cursor( )
   
      cur.execute("SELECT id1 FROM grp WHERE na=?",(na,))
      rows=cur.fetchone()[0]
      id2=rows
      cur.execute("SELECT * FROM gr WHERE id2=?",(id2,))
      ro=cur.fetchall()
  
    

      return render_template("listat.html",ro=ro)


 
if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0', port=2009)

    
 
