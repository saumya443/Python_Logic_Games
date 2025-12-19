import random
'''
1 for snake
-1 for water
0 for gun'''
i =0
computer = random.choice([-1,0,1])
yourstr = input("Enter your choice : ")
yourdict ={ "s":1,"w":-1,"g":0}
reversedict = {1:"s",-1:"w",0:"g"}
you=yourdict[yourstr]

print(f"you chose : {(reversedict[you])}\ncomputer chose : {(reversedict[computer])}")
if(computer == you):
    print("Its draw")
else:
    # if(computer-you==-1 or computer-you==2)
    # print("you lose")
# else:
#     print(you win)
        if(computer ==-1 and you==1):
            print("You win!")
        elif(computer ==-1 and you==0):
            print("You Lose!")
        elif(computer ==1 and you==-1):
            print("You Lose!")
        elif(computer ==1 and you==0):
            print("You Win!")
        elif(computer ==0 and you==-1):
            print("You Win!")
        elif(computer ==0 and you==1):
            print("You Lose!")
        else:
            print("Something went wrong")