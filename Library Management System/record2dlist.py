def record2dlist(l2):
	rec = open("record.txt","r")
	for i in rec:
		l2.append(i.split(","))
