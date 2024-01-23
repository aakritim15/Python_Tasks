import random
print("WE ARE PLAYING ROCK, PAPER AND SCISSORS!!")
while True:
  print("Enter your choice of number:\n1. Rock \n2. Paper \n3. Scissors\n")
  choice = int(input("Enter your choice:"))
  while choice > 3 or choice <1:
    choice = int(input("Enter a valid number , Please."))
  if choice == 1:
    choice_name = 'Rock'
  elif choice == 2:
    choice_name = 'Paper'
  else:
    choice_name = 'Scissors'
  print("Your choice is",choice_name,".")
  print("Now its computer's turn:")
  com= random.randint(1, 3)
  while com== choice:
    com = random.randint(1, 3)
  if com == 1:
    com_choice_name = 'Rock'
  elif com== 2:
    com_choice_name = 'Paper'
  else:
    com_choice_name = 'Scissors'
  print("Computer's choice is ",com_choice_name,".")
  print(choice_name, 'VS', com_choice_name)
  if choice == com:
    print("Its a draw.\n")
    result = 'Draw'
  if choice ==1 and com== 2:
    print("Paper wins!\n", end="")
    result='Computer'
  elif choice == 2 and com == 1:
    print("Rock wins!\n", end="")
    result='User'
  if choice ==1 and com== 3:
    print("Rock wins!\n", end="")
    result='User'
  elif choice ==3 and com == 1:
    print("Rock wins!", end="")
    result='Computer'
  if choice ==2 and com== 3:
    print("Scissors wins!", end="")
    result='Computer'
  elif choice ==3 and com == 2:
    print("Scissors wins!", end="")
    result='User'
  if (result == 'Draw'):
    print("Its a draw.")
  if (result == 'Computer'):
    print("\nHurray,Computer wins!")
    print("\nBetter luck next time!")
  elif (result == 'User'):
    print("\nHurray,User wins!")
  a = input("Do you want to play again (Y/N)")
  if (a == 'N' or  a== 'n'):
    break
print("Thanks for playing.")