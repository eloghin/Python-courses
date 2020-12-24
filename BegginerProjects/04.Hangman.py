"""
Play hangman in max 10 steps
"""

from random import choice
from words import words

def play_hangman(lives):
	word = choice(words)
	to_be_guessed = set(word)
	guessed_letter = []
	print_word(word, guessed_letter)
	steps = 0

	while to_be_guessed and lives > 0 :
		letter = input(f"You have {lives} more lives. Guess a letter: ")

		if letter in word and letter not in guessed_letter:
			guessed_letter.append(letter)
			print_word(word, guessed_letter)
			to_be_guessed.remove(letter)
		else:
			print("wrong!\n")
			lives -= 1
		steps += 1

	if to_be_guessed:
		print(f"You lost! The word was {word}\n")
	else:
		print(f"Good job! You guessed {word} in {steps} guesses\n")


def print_word(word, guessed_letter):
	for char in word:
		if char in guessed_letter:
			print(char, end="")
		else:
			print("_", end="")
	print()	

play_hangman(10)