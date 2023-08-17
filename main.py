rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
list_of_choices = [rock, paper, scissors]
choice = 0
computer_score = 0
user_score = 0
while choice == 0:
  user_move = int(input("\n1. Rock \n2. Paper \n3. Scissor \nChoose 1 for rock, 2 for paper and 3 for scissors \n"))
  if user_move >3 or user_move<1:
    print("You chose an invalid number\n\n")
    print("Please choose again")
  else:
    computer_move = random.randint(1,3)
    print(list_of_choices[user_move-1])
    print("Computer choice \n",list_of_choices[computer_move-1])
    if user_move == computer_move:
      print("It's a Draw")
    elif user_move == 1: 
      if computer_move == 2:
        computer_score+=1
        print("Sorry, you lose..")
      else:
        user_score+=1
        print("Congratulations, You win!!")
    elif user_move == 2: 
      if computer_move == 3:
        computer_score+=1
        print("Sorry, you lose..")
      else:
        user_score+=1
        print("Hurrayyy.., You win!!")
    elif user_move == 3: 
      if computer_move == 1:
        computer_score+=1
        print("Sorry, you lose..")
      else:
        user_score+=1
        print("Hurrayyy.., You win!!")

    print(f"\nYour score: {user_score} \nComputer score: {computer_score}\n")
  
    choice = int(input('\n0. Play again \n1. Exit \nPress 0 to continue or 1 for quitting the game\n'))