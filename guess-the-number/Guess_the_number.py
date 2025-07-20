#Guess the number Game
import random
p=0
print("Welcome to Guess the number Game:")
level=input("Choose the Level; e for Easy, m for Medium and h for Hard:").lower()
e=random.randint(1,10)
m=random.randint(1,50)
h=random.randint(1,100)
while True:
    p+=1
    if(level=="e"):
        user=int(input("Enter your guess between 1 and 10:"))
        if(user==e):
            print(f"Congratulations!You guessed it right in {p} tries")
            break
        elif(user>e):
            print("Enter the lower one")
        else:
            print("Enter the higher number")
            
        
    elif(level=="m"):
        user=int(input("Enter your guess between 1 and 10:"))
        if(user==m):
            print(f"Congratulations!You guessed it right in {p} tries")
            break
        elif(user>m):
            print("Enter the lower one")
        else:
            print("Enter the higher number")
     
    elif(level=="h"):
        user=int(input("Enter your guess between 1 and 100:"))
        if(user==h):
            print(f"Congratulations!You guessed it right in {p} tries")
            break
        elif(user>h):
            print("Enter the lower one")
        else:
            print("Enter the higher number")
               
            
       
    
