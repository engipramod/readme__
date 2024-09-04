import random
print("  welcome to rps")
user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name here: ")
print("""
      winning rules:
      1. rock vs scissor --> paper
      2. rock vs scissor --> rock
      3. scissor --> scissor""")
choice = int(input("enter your choice from 1-3: "))
print()
while choice > 3 or choice < 1:
    choice = int(input("enter valid input"))
    
if choice ==1:
    user_choice = "rock"
elif choice == 2:
    user_choice = "paper"
else:
    user_choice = "scissor"

print("The user's choice is", user_choice)
print("Now it is computer turn")
computer = random.randint(1,3)


if computer == 1:
    comp_choice = "rock"
elif computer == 2:
    comp_choice = "paper"
else:
    comp_choice = "scissor"

print("The computer choice is", comp_choice)

if ((user_choice =="paper" and comp_choice == "rock") or(user_choice == "rock" and comp_choice == "paper")):
    print("paper wins")
    result = "paper"
elif ((user_choice =="scissor" and comp_choice == "rock") or(user_choice == "rock" and comp_choice == "scissor")):
    print("rock wins")
    result = "rock"
elif (user_choice == comp_choice):
    print("it is tie")
    result = "Tie"
else:
    print("scissor wins")
    result = "scissor"
if result == "Tie":
    ties +=1
elif result == user_choice:
    print("user wins")
    user_score +=1
else:
    print("computer win")
    comp_score += 1
print("Scores are ")
print(name,"'s score is", user_score)
print("computer's score is", comp_score)
print("ties are",ties)