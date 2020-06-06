import sqlite3
book=sqlite3.connect('booklist.db')
curbook=book.cursor()

inp=input("Do you want to add records (Y/N) : ")
while (inp=='Y' or inp=='y'):
    bookid=int(input("Enter book id : "))
    tit=input("Enter title : ")
    auth=input("Enter author name : ")
    prc=float(input("Enter Price : "))
    curbook.execute("INSERT INTO books (BookId,Title,Author,Price)VALUES(?,?,?,?)",(bookid,tit,auth,prc))
    book.commit()
    print("Record Added Successfully")
    inp=input("Do you want to add one more record (Y/N) : ")
else :
    exit()
