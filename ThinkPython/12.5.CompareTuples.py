"""
Play hangman in max 10 steps
"""

"""
Exercise 2  

In this example, ties are broken by comparing words, so words with the same length appear 
in reverse alphabetical order. For other applications you might want to break ties at random. 
Modify this example so that words with the same length appear in random order. 

Hint: see the random function in the random module. 

Solution: http://thinkpython.com/code/unstable_sort.py.
"""
from random import random

def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), random(), word))

    t.sort(reverse=True)

    res = []
    for length, rand, word in t:
        res.append(word)
    return res

words = ['elena', 'aron', 'amurg', 'ana', 'andrei', 'ioana', 'iarina', 'vicky', 'nora', 'ina', 'iris']

print(sort_by_length(words))