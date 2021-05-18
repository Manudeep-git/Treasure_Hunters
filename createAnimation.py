import numpy as np
import copy
from exportGIF import to_gif

maze = None
sequence = []
current_pos = None

np.random.seed(0)

# maze visualization constants
b = 'b'
w = 'w'
t = 't'
p = 'p'
e = 'e'

def add_frame():
	'''Adds image of current maze state to sequence of frames, to be exported to GIF later'''

	global sequence

	temp = copy.copy(maze)
	temp[current_pos] = p
	sequence.append(temp)

def move(direction):
	'''Moves current player position in given direction, adds new frame to sequence.
	   Valid directions are "u" (up), "d" (down), "l" (left), and "r" (right)'''

	global current_pos

	if np.array_equal(maze[current_pos], t) or np.array_equal(maze[current_pos], e):
		maze[current_pos] = b

	if direction.lower() == 'u':
		if current_pos[0] == 0 or np.array_equal(maze[current_pos[0] - 1][current_pos[1]], w):
			print('Invalid move UP from position ({},{})'.format(current_pos[0], current_pos[1]))
		else:
			current_pos = (current_pos[0] - 1, current_pos[1])
			add_frame()
	elif direction.lower() == 'd':
		if current_pos[0] == len(maze) - 1 or np.array_equal(maze[current_pos[0] + 1][current_pos[1]], w):
			print('Invalid move DOWN from position ({},{})'.format(current_pos[0], current_pos[1]))
		else:
			current_pos = (current_pos[0] + 1, current_pos[1])
			add_frame()
	elif direction.lower() == 'l':
		if current_pos[1] == 0 or np.array_equal(maze[current_pos[0]][current_pos[1] - 1], w):
			print('Invalid move LEFT from position ({},{})'.format(current_pos[0], current_pos[1]))
		else:
			current_pos = (current_pos[0], current_pos[1] - 1)
			add_frame()
	elif direction.lower() == 'r':
		if current_pos[1] == len(maze[0]) - 1 or np.array_equal(maze[current_pos[0]][current_pos[1] + 1], w):
			print('Invalid move RIGHT from position ({},{})'.format(current_pos[0], current_pos[1]))
		else:
			current_pos = (current_pos[0], current_pos[1] + 1)
			add_frame()
	else:
		print('Unknown move command "{}"'.format(direction))

def createAnimation(input_maze, start_pos, player_moves):

	global sequence
	global maze
	global current_pos

	maze = input_maze
	current_pos = start_pos

	add_frame()

	for m in player_moves:
		move(m)

	add_frame()
	add_frame()
	add_frame()

	to_gif(sequence, 'animation.gif')