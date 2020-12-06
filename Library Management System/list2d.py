def list2d(l1):
    lib = open("books.txt","r")
    for i in lib:
        l1.append(i.split(","))
    lib.close()
    return 



