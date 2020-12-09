import sys 
import random

# ***********
# ** SOL 1 **
# ***********

answer = random.randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
	try:
		guess = int(input(f'Make a guess in interval [{int(sys.argv[1])}-{int(sys.argv[2])}]:  '))
		if int(sys.argv[1]) <= guess <= int(sys.argv[2]):
			if guess == answer:
				print("you did it!")
				break
	except ValueError:
		print(f'Hey, you! I said interval [{int(sys.argv[1])}-{int(sys.argv[2])}')
		continue


# ***********
# ** SOL 2 **
# ***********
  
# print("Let's start the guessing number game!") 
 

# number = random.randint(int(sys.argv[1]), int(sys.argv[2]))

# guess = int(input("Make a guess: "))


# while guess != number:

# 	if guess < number:
# 		print("Your guess is smaller than the target")
# 	else:
# 		print("Your guess is bigger than the target")

# 	guess = int(input("make another guess: "))

# print("You've made it! Brilliant")