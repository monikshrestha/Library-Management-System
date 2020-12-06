import datetime
def billborrow(l1,l3):
    total = 0
    for i in l3:
        total += float(l1[i][-1])
    print("you have to pay",total)
        
def billreturn(l2,l4):
    for i in l4:
        string_date = l2[i][3]
        format = "%Y-%m-%d"
        datetime_object = datetime.datetime.strptime(string_date, format)
        t =datetime.datetime.today()-datetime_object 
        
 
