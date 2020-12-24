"""
Play rock, paper, scissors with the computer
"""

from random import choice

def play():
	user = input("Enter your choice - rock(r), paper(p), scissors(s): ").lower()
	computer = choice(['r', 'p', 's'])
	print(f'computer: {computer}')

	if user == computer:
		print('It\'s a tie!')
	else:
		is_win(user, computer)


def is_win(user, computer):
	# r > s; s > p; p > r
	if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
		print("You win!")
	else:
		print("You lost!")

play()