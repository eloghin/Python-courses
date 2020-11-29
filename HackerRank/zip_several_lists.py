#The task
#The National University conducts an examination of N students in X subjects.
#Your task is to compute the average scores of each student.

# Input Format
# The first line contains N and X separated by a space.
# The next X lines contains the space separated marks obtained by students in a particular subject. 

import sys

n, x = map(int, input().split()) 

grades = []
for _ in range(x):
  grades.append(list(map(float, input().rstrip().split())))

# the * operator can be used to unpack an iterable into the arguments in the function call
for lista in zip(*grades):
  print(sum(lista)/len(lista))