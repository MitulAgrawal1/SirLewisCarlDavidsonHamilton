
import mysql.connector
 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database="library"
)
 
cursor = mydb.cursor()

sql = "Create table book_id (Name char(20), bookid char(20) Primary Key, Author char(20), Copies integer)"
cursor.execute(sql) 
mydb.commit()
sql = "Create table user_id (Nameuser char(20), userid char(20) Primary Key, Password char(20), Role integer)"
cursor.execute(sql)
mydb.commit()
sql = "Create table history (Name char(20), bookid char(20), userid char(20), check_out date, check_in date, due_date date)"
cursor.execute(sql)
mydb.commit()

