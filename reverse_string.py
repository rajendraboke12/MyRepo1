mirror="Acd$er123#kjlbv?1@jbkk"
print("Original : "+mirror)
specChar=["$","#","?","@"]
mylist=[]
for ch in mirror:
    mylist.append(ch)
i=0
j=len(mylist)
while(i<len(mylist)/2):
    j=j-1
    if(mylist[i] in specChar and mylist[j] not in specChar):
        j=j+1
        i=i+1
        continue
    elif(mylist[j] in specChar and mylist[i] not in specChar):
        i=i-1
        i=i+1
        continue
    elif(mylist[j] in specChar and mylist[i] in specChar):
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

