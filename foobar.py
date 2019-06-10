for i in range(1,1001):
    if(i%3 == 0 and i%5 == 0 and i%10 != 0):
        print(str(i)+":"+"foo-bar")
    elif(i%3 == 0 and i%10 != 0):
        print(str(i)+":"+"foo")
    elif(i%5 == 0 and i%10 != 0):
        print(str(i)+":"+"bar")

