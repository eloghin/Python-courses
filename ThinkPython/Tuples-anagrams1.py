	
"""
1. Write a program that reads a word list from a file (see “Reading
Word Lists”) and prints all the sets of words that are anagrams.

Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted','slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']

Hint: you might want to build a dictionary that maps from a
collection of letters to a list of words that can be spelled with
those letters. The question is, how can you represent the
collection of letters in a way that can be used as a key?
"""

import re

def signature(word):
	chars = sorted(list(word.lower()))
	result = "".join(chars)
	return result


def find_anagrams(file):
	anagrams = {}

	with open(file, 'r') as my_file:
		for line in my_file:
			for word in re.split(r'[^a-zA-Z]', line):
				word = word.lower()
				if len(word) > 1:
					s = signature(word)
					if s in anagrams:
						if word not in anagrams[s]:
							anagrams[s].append(word)
					else:
						anagrams[s] = [word]

	print_sorted_anagrams(anagrams)


def print_anagrams(dict):
	for key in dict:
		if len(dict[key]) > 1:
			print(dict[key]) 

def print_sorted_anagrams(dict):
	list_len = []
	for key in dict:
		if len(dict[key]) > 1:
			list_len.append((len(dict[key]), dict[key]))
	
	for item in sorted(list_len, reverse=True):
		print(item[1])

# find_anagrams('Tuples-anagrams.txt')
find_anagrams('prideAndPrejudice.txt')



