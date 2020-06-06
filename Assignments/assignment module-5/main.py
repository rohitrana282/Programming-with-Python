import sqlite3

book=sqlite3.connect('booklist.db')
curbook=book.cursor()

inp=input("Book Title:  ")
i=0
sql="Select * from books WHERE Title='"+inp+"';"
curbook.execute(sql)
k=1
price=0
while k==1:
    record=curbook.fetchone()
    if record==None:
        if i==0:
            print("Unavailable..!!!")
        else:
            k=0
    else:
        print(*record,sep=" , ")
        n=int(input("\n\nNo. of Copies:  "))
        price+=record[3]*n
        i+=1
    m=input("Add more books? Y/N ")
    if m=='Y' or m=='y':
        i=0
        k=1
        inp=input("Book Title:  ")
        sql="Select * from books WHERE Title='"+inp+"';"
        curbook.execute(sql)
    else :
        break

print("\n\nTotal Cost {}".format(price))



    


