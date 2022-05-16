fname = input("Enter file name: ")
fh = open(fname)
list=[]
for line in fh:
    l=line.strip()
    l=l.split(" ")
    l.sort()
    list.append(l)
list.sort()    
print(list)