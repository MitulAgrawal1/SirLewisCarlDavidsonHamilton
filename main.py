import mysql.connector
import random 
from datetime import date

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database="library"
)

cursor = mydb.cursor()
def login():
    global a
    username = input("Enter the user_id of the user: ")
    userpassword = input("Enter the user password: ")
    sql = "SELECT * FROM user_id where userid = %s"
    values = (username,)
    cursor.execute(sql,values)
    rows = cursor.fetchall()
    if rows[0][1] == username and rows[0][2] == userpassword and rows[0][3] == 1:
        a = username
        normaluser()
    elif rows[0][1] == username and rows[0][2] == userpassword and rows[0][3] == 2:
        adminuser()
    else:
        print("Error in login ...")

def normaluser():
    while True:
        print("\n1.Search by Author")
        print("2.Checkout a Book")
        print("3.View Past Transactions")
        print("4.Exit\n")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            searchbyauth()
        if ch == 2:
            checkout()
        if ch == 3:
            print("Good Bye")
            break
        if ch == 4:
            print("Good Bye")
            break
    print("normaluser")  

def searchbyauth():
    authorname = input("\nEnter the author whose books you want to view: ")
    sql = "SELECT * FROM book_id where Author = %s"
    values = (authorname,)
    cursor.execute(sql,values)
    rows = cursor.fetchall()
    for i in rows:
        print("\nBook name =",i[0],"            Copies left =",i[3])

def checkout():
    global a
    global today
    booknum = input("Enter the ISBN number of the book: ")
    booknum = (booknum,)
    sql = "SELECT * FROM book_id where bookid = %s"
    cursor.execute(sql,booknum)
    rows = cursor.fetchall()
    print("\nBook Name =",rows[0][0],"\nBook ISBN number:",rows[0][1],"\nBook Author:",rows[0][2])
    confirm = input("\nDo you want to checkout this book (yes or no): ")
    if confirm == "yes" and rows[0][3] != "0":
        print("\n Proccessing ....... \n")
        today = date.today()
        sql = "INSERT into history values(%s,%s,%s,%s)"
        values = (booknum[0],a,today,None)
        cursor.execute(sql,values)
        mydb.commit()
        sql = "UPDATE book_id SET Copies = %s WHERE bookid = %s"
        values = (str(int(rows[0][3]) - 1), booknum[0])
        cursor.execute(sql, values)
        mydb.commit()
        print("Book Checked out  \n")
    else:
        print("\n ERROR TRY AGAIN LATER ....... \n")

def userformer():
    username = input("Enter the name of the user: ")
    userpassword = input("Enter the user password: ")
    sql = "SELECT userid FROM user_id"
    cursor.execute(sql)
    rows = cursor.fetchall()
    userid = username + str(random.randrange(10000))
    print(rows[0],rows)
    for i in rows: 
        if userid not in i[0]:
            continue
        else:
            print("Try again later")
            return
    print("\nUsername =",username)
    print("Userpassword =",userpassword)
    print("User_Id =",userid,"\n")
    correct = input("If above information is correct enter yes: ")
    if correct == "yes":
        sql = "INSERT into user_id values(%s,%s,%s,1)"
        values = (username,userid,userpassword)
        cursor.execute(sql,values)
        mydb.commit()
        print("User has been created ....\n")


def addbook():
   bookname=input("Enter book name: ")
   booknumber=input("Enter book ISBN number: ")
   bookauthor=input("Enter the name of the author of the book: ")
   bookgenre=input("Enter book genre: ")
   bookcopies = int(input("Number of copies of book: "))
   sql = "INSERT into book_id values (%s,%s,%s,%s,%s)"
   values = (bookname.upper(), booknumber,bookauthor.upper(),bookgenre.upper(),bookcopies)
   cursor.execute(sql, values)
   mydb.commit()
       


def allcheck():
    library_id = int(input("Please enter your 4 digit library number: "))



def adminuser():
    print("adminuser")  

while True:
    a = ""
    print("###################################################")
    print("Library Login .....")
    print("###################################################\n")
    login()







