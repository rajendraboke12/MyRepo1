mirror="Acd$er123#kjlbv?1@jbkk"
print("Original : "+mirror)
mylist=[]
for ch in mirror:
    mylist.append(ch)
i=0
j=len(mylist)
while(i<len(mylist)/2):
    j=j-1
    if(not mylist[i].isalnum() and mylist[j].isalnum()):
        j=j+1
        i=i+1
        continue
    elif(not mylist[j].isalnum() and mylist[i].isalnum()):
        i=i-1
        i=i+1
        continue
    elif(not mylist[j].isalnum() and not mylist[i].isalnum()):
        i=i+1
        continue
    temp=mylist[i]
    mylist[i]=mylist[j]
    mylist[j]=temp
    i=i+1
reverse=""
for ch in mylist:
    reverse=reverse+ch
print("finalStr : "+reverse)

