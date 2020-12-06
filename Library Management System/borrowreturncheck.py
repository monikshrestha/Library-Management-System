def recordborrow(l1,l2,name,sno):
    for i in l2:
        if name  in i and l1[int(sno)][1] in i and i[2]=="YES" and i[4]=="NO":
            print("NOT ALLOWED TO BORROW\nYOU HAVE NOT RETURNED PREVIOUS BOOKS\n")
            return False
    return True
        
def recordreturn(l1,l2,name,sno,l4):
    a = 0
    for i in l2:
        a += 1
        if name  in i and l1[int(sno)][1] in i and i[2]=="YES" and i[4]=="NO":
            l4.append(a-1)
            return True,a-1
    return False,None
        
        
