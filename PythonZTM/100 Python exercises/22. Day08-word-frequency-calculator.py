"""
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
"""

string = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'

words = string.split()

word_count = {}

for word in words:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

for k,v in word_count.items():
  print(f'{k}:{v}')
