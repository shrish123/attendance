import sqlite3
 
conn = sqlite3.connect("t16.db")


cursor = conn.cursor()

 

cursor.execute("""CREATE TABLE grp
                  (id1 integer primary key autoincrement,na text) 
               """)
cursor.execute("""CREATE TABLE gr
                  (id2 integer primary key autoincrement,
                  nb text,
                  nc text
                  )
               """)
print('c')
conn.close()
                         
