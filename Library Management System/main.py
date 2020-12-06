import showBooks
import list2d
import borrowBook
import returnBook
import record
import record2dlist 
import borrowreturncheck as b
import bill
#importing the required module for the program
l3 = [] #creating empty list 
l4=[]

first_name = input("Enter your first name: ").upper()
last_name = input("Enter your last name: ").upper()
name = first_name+' '+ last_name
a = 'y'
while a == 'y':
    l1 = []
    l2 = []
    list2d.list2d(l1)
    record2dlist.record2dlist(l2)
    ans = True
    while (ans == True):
        types = input("Enter 1 to borrow book\nEnter 2 to return book\n")
        if types == '1' or types =='2':
            ans = False
        else:
            print("invalid\nEnter again\n")
    ans = True
    showBooks.showBooks(l1)
    if types == '1':
            while (ans == True):
                try:
                    sno = int(input("Enter serial number to borrow book"))
                    if int(sno)>0 and int(sno)<len(l1):
                        ans = False
                    else:
                        print("invalid\nEnter again\n")
                except:
                    print("invalid \n Enter again\n")
            an = b.recordborrow(l1,l2,name,sno)
            if an == True:
                l3.append(int(sno))
                borrowBooks = borrowBook.borrowBook(l1,sno)
                print("Book borrowed")
                records = record.record(name,l1,types,sno)
    else:
        while (ans == True):
            try:
                sno = input("Enter serial number to return book")
                if int(sno)>0 and int(sno)<len(l1):
                    ans = False
                else:
                    print("invalid\nEnter again\n")
            except:
                print("invalid\n Enter again\n")
        an,a = b.recordreturn(l1,l2,name,sno,l4)
        if an == True:
            if int(sno) in l3:
                l3.remove(int(sno))
            returnBook.returnBook(l1,sno)
            print("book returned")
            records = record.recordReturn(l2,a)
        else:
            print("NO RECORD FOUND\nYOU HAVE NOT BORROWED BOOK FROM THIS LIBRARY\n")
        
    while ans == False:
        print(l3)
        a = input("Press y to take/return more books and n exit: ").lower()
        if a == "y" or a =="n":
            ans = True
        else:
            ans = False

bill.billborrow(l1,l3)
bill.billreturn(l2,l4)
