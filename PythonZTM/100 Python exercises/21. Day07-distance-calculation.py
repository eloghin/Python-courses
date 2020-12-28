"""
    A robot moves in a plane starting from the original point (0,0). 
    The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
    The trace of robot movement is shown as the following:

		UP 5
		DOWN 3
		LEFT 3
		RIGHT 2

    The numbers after the direction are steps. Please write a program to compute the distance 
    from current position after a sequence of movement and original point. 
    If the distance is a float, then just print the nearest integer. 
    Example: If the following tuples are given as input to the program:

		UP 5
		DOWN 3
		LEFT 3
		RIGHT 2

    Then, the output of the program should be:

		2

"""

# ***********
# ***SOL 1***
# ***********

from math import dist
import sys
# import pdb

class RobotPosition():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move_up(self, steps):
		self.y += steps

	def move_down(self, steps):
		self.y -= steps

	def move_left(self, steps):
		self.x -= steps

	def move_right(self, steps):
		self.x += steps		 

r = RobotPosition(0,0)

moves = [line.splitlines() for line in sys.stdin]

for move in moves:

	direction, steps = move[0].split()

	if direction == 'UP':
		r.move_up(int(steps))

	elif direction == 'DOWN':
		r.move_down(int(steps))

	elif direction == 'RIGHT':
		r.move_right(int(steps))

	elif direction == 'LEFT':
		r.move_left(int(steps))

	else:
		print('Wrong direction! Input again')

print(round(dist([0, 0], [r.x, r.y])))


# ***********
# ***SOL 2***
# ***********

import  math

x,y = 0,0
while True:
    s = input().split()
    if not s:
        break
    if s[0]=='UP':                  # s[0] indicates command
        x-=int(s[1])                # s[1] indicates unit of move
    if s[0]=='DOWN':
        x+=int(s[1])
    if s[0]=='LEFT':
        y-=int(s[1])
    if s[0]=='RIGHT':
        y+=int(s[1])
                                    # N**P means N^P
dist = round(math.sqrt(x**2 + y**2))  # euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
print(dist)

