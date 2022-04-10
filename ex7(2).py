import sqlite3

def connect(dbname):
    connection=sqlite.connect(dbname)
    connection.execute("CREATE TABLE IF NOT EXISTS COLLEGES (NAME,ADDRESS,CONTACT,EMAIL)")
    PRINT("Table created successfully")
    connection.close()
    
def inserting(dbname,values):
    connection=sqlite3.connect(dbname)
    connection.execute("INSERT INTO COLLEGE(NAME,ADDRESS,CONTACT,EMAIL} VALUES(?,?,?,?)",values)
    connection.commit()
    connection.close()
    
def information(dbname):
    connection=sqlite3.connect(dbname)
    
    cursor_=connection.cursor()
    cursor.execute("SELECT * FROM COLLEGES")
    table_data=cursor.fetchall()
    for i in table_data:
        print(i)
    connection.close()
