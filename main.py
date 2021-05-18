from maze import getMaze
from qlearning import qlearn, solve
from createAnimation import createAnimation
import matplotlib
import matplotlib.pyplot as plt
import sys

# get options from command line
if len(sys.argv) > 1:
	if sys.argv[1].lower()[0] not in ['s', 'm', 'l']:
		exit('Invalid maze size "{}". Use "s" for small, "m" for medium, or "l" for large'.format(sys.argv[1]))
	else:
		size = sys.argv[1].lower()[0]
		enemies = False

if len(sys.argv) == 3:
	if sys.argv[2].lower()[0] != 'e':
		exit('Invalid enemy flag "{}". Add "e" after maze size to enable enemies'.format(sys.argv[2]))
	else:
		enemies = True

# get specified maze
starting_pos, maze = getMaze(size, enemies)

if sys.argv[1].lower()[0] == 's':
	size_string = 'small'
elif sys.argv[1].lower()[0] == 'm':
	size_string = 'medium'
else:
	size_string = 'large'

if enemies:
	enemies_string = 'with'
else:
	enemies_string = 'without'

print('Using {} maze {} enemies'.format(size_string, enemies_string))

print('Starting Q learning...', flush=True)
q_table, n_time_steps = qlearn(maze, starting_pos)
print('Q learning complete')

print('Finding best path...', end=' ', flush=True)
moves = solve(maze, starting_pos, q_table)
print('done')

print('Path:', moves)

print('Animating / Creating GIF...', end=' ', flush=True)
createAnimation(maze, starting_pos, moves)
print('done')

print('Animation saved as "animation.gif"')

plt.plot(n_time_steps)
plt.xlabel('Episode')
plt.ylabel('Number of time steps')
plt.show()