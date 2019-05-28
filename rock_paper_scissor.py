list1 = ["r","p","s"]
print("Enter player1 name :")
player1 = raw_input()
print("Enter player2 name :")
player2 = raw_input()
while(True):
    while(True):
        print("player1 choose r,p,s : ")
        player1Input = raw_input()
        if(player1Input in list1):
            break
        else:
            print("Enter correct option(r,p,s)")
    while(True):
        print("player2 choose r,p,s : ")
        player2Input = raw_input()
        if(player2Input in list1):
            break
        else:
            print("Enter correct option(r,p,s)")
    if(player1Input == player2Input):
        print("Match Draw")
    elif(player1Input == "r" and player2Input == "s"):
        print("Winner : "+player1)
    elif(player1Input == "s" and player2Input == "p"):
        print("Winner : "+player1)
    elif(player1Input == "p" and player2Input == "r"):
        print("Winner : "+player1)
    elif(player2Input == "r" and player1Input == "s"):
        print("Winner : "+player2)
    elif(player2Input == "s" and player1Input == "p"):
        print("Winner : "+player2)
    elif(player2Input == "p" and player1Input == "r"):
        print("Winner : "+player2)
    print("Do you want to exit ? (Y/N)")
    choice = raw_input()
    if(choice=="Y" or choice=="y"):
        print("Bye")
        exit(0)
