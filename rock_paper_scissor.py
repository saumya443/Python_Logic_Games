import random
print("      \"Welcome to ROCK -PAPER -SCISSOR GAME\" \n     If You do not want to play game press No ")
for i in range(1,128):
    
    
        
            computer = random.choice(["r","p","s"])
            you = input("Enter your choice : ")
            computer = random.choice(["r","p","s"])
            # yourdict ={ "s":"s","w":"r","g":"p"}
            # reversedict = {"s":"s","r":"w","p":"g"}
            # you=yourdict[yourstr]
            if(you=="No"):
                print("Thanks! Game Ends")
                break
            
            elif(computer == you):
                print(f"you chose : {you}\ncomputer chose : {computer}")
                print("Its draw")
            
            elif(computer =="r" and you=="s"):
                  print(f"you chose : {you}\ncomputer chose : {computer}")
                  print("You Lose!")
            elif(computer =="r" and you=="p"):
                  print(f"you chose : {you}\ncomputer chose : {computer}")
                  print("You Win!")
            elif(computer =="s" and you=="r"):
                  print(f"you chose : {you}\ncomputer chose : {computer}")
                  print("You Win!")
            elif(computer =="s" and you=="p"):
                  print(f"you chose : {you}\ncomputer chose : {computer}")
                  print("You Lose!")
            elif(computer =="p" and you=="r"):
                  print(f"you chose : {you}\ncomputer chose : {computer}")
                  print("You Lose!")
            elif(computer =="p" and you=="s"):
                  print(f"you chose : {you}\ncomputer chose : {computer}")
                  print("You Win!")
            else:
                  print("something went wrong")
                            