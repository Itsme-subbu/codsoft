import random
user_score=0
computer_score=0
list1=["rock","paper","scissors"]

print(" \t 1.play \t 2.quit")
choice=int(input("enter your choice"))
if choice==1:
    while True:
        print("\t you have choose to play")
        print(" 1.Rock \t 2.paper \t 3.scissors")
        user_choice=int(input("enter a number that will indicates the above three : "))
        computer_choice=random.choice(list1)
        if user_choice==1:
            choice=(list1[user_choice-1])
        elif user_choice==2:
            choice=(list1[user_choice-1])
        elif user_choice==3:
            choice=(list1[user_choice-1])   
        if (choice=="rock" and computer_choice=="scissors") or (choice=="paper" and computer_choice=="rock") or (choice=="scissors" and computer_choice=="paper"):
            print(f"you:{choice} \t computer : {computer_choice}")
            print("you won")
            user_score+=1
            print(f"your score : {user_score}  computer_score : {computer_score}")
        elif choice==computer_choice:
            print("Braw")        
            print(f"your score : {user_score}  computer_score : {computer_score}")
        else:
            if user_choice>=4:
                print("wrong choice")
            else:    
                print("you lost") 
                computer_score+=1   
                print(f"your score : {user_score}  computer_score : {computer_score}")
        print("if you continue the game press 1 otherwise press  2 to quit the game")
        cont=int(input())
        if cont == 2 :
            print("you choose to quit the game")
            break
  

            

