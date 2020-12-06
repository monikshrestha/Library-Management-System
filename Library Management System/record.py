import datetime
def record(name,l1,types,sno):
    hh = open("record.txt", "a")
    hh.write(name)
    hh.write(",")
    hh.write(l1[int(sno)][1])#book_name
    hh.write(",")
    hh.write("YES")#borrow_book
    hh.write(",")
    hh.write(str(datetime.date.today()))#borrowed_time
    hh.write(",")
    hh.write("NO")#reutrn_book
    hh.write(",")
    hh.write("NO")#return_time
    hh.write(",")
    hh.write(str(l1[int(sno)][4]))#price
    hh.write("\n")
    
    hh.close()
    
def recordReturn(l2,a):
    rec = open("record.txt","w")
    l2[a][4] = "YES"
    l2[a][5] = str(datetime.date.today())
    for i in l2:
        i = ','.join(i)
        rec.write(i)
    rec.close()
    
