import random

stone = '''
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

sizzer = '''
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image_choice = [stone,paper,sizzer] 

print('stone paper sizerer game choose 0-stone, 1-paper, 2-sizzer')

user_choice = int(input('Enter your choise : '))  #user choice 
print('Your choice:\n')
print(image_choice[user_choice])  

computer_choice = random.randint(0,2)  #computer choice

print('Computer choice:\n')
print(image_choice[computer_choice])

if user_choice >2 or user_choice<0:
    print('You lose !! (Because choice wrong input )')
elif user_choice == 0 and computer_choice == 2:
    print('you win !!')
elif computer_choice == 0 and user_choice == 2:
    print('You Lose !!')
elif computer_choice>user_choice:
    print('you Lose !')
elif user_choice>computer_choice:
    print('you win !!')
elif user_choice == computer_choice:
    print('It\'s Draw !!!')