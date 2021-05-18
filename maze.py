import numpy as np

# maze representation constants
b = 'b'
w = 'w'
t = 't'
e = 'e'

def getMaze(size, enemies):
	if enemies:
		if size == 's':
			starting_pos = (0, 0)
			maze = np.array([[b, b, t],
							 [e, e, b],
			 				 [t, b, b]])
		elif size == 'm':
			starting_pos = (2, 2)
			maze = np.array([[t, b, b, w, t],
							 [w, w, e, w, b],
							 [b, w, b, w, b],
							 [b, b, b, w, b],
							 [t, w, b, b, b]])
		elif size == 'l':
			starting_pos = (0, 0)
			maze = np.array([[b, b, e, t, b, b, b, b, t],
							 [b, w, w, b, w, w, w, w, w],
							 [b, w, w, b, b, b, b, b, b],
							 [b, w, w, w, w, w, w, w, b],
							 [b, w, b, b, b, b, b, b, b],
							 [b, w, b, w, w, w, w, w, w],
							 [b, w, b, b, b, b, b, b, b],
							 [b, w, w, w, w, w, w, w, b],
							 [b, b, b, b, b, b, b, b, b]])
		else:
			return ValueError('Invalid maze size "{}"'.format(size))
	else:
		if size == 's':
			starting_pos = (0, 0)
			maze = np.array([[b, b, t],
							 [b, b, b],
			 				 [t, b, b]])
		elif size == 'm':
			starting_pos = (2, 2)
			maze = np.array([[t, b, b, w, t],
							 [w, w, b, w, b],
							 [b, w, b, w, b],
							 [b, b, b, w, b],
							 [t, w, b, b, b]])
		elif size == 'l':
			starting_pos = (15, 9)
			maze = np.array([[b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b],
							 [t, w, w, w, b, w, w, w, b, w, b, w, w, w, b, w, w, w, t],
							 [b, w, w, w, b, w, w, w, b, w, b, w, w, w, b, w, w, w, b],
							 [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
							 [b, w, w, w, b, w, b, w, w, w, w, w, b, w, b, w, w, w, b],
							 [b, b, b, b, b, w, b, b, b, w, b, b, b, w, b, b, b, b, b],
							 [w, w, w, w, b, w, w, w, b, w, b, w, w, w, b, w, w, w, w],
							 [w, w, w, w, b, w, b, b, b, b, b, b, b, w, b, w, w, w, w],
							 [w, w, w, w, b, w, b, w, w, b, w, w, b, w, b, w, w, w, w],
							 [w, w, w, w, b, b, b, w, b, b, b, w, b, b, b, w, w, w, w],
							 [w, w, w, w, b, w, b, w, w, w, w, w, b, w, b, w, w, w, w],
							 [w, w, w, w, b, w, b, b, b, t, b, b, b, w, b, w, w, w, w],
							 [w, w, w, w, b, w, b, w, w, w, w, w, b, w, b, w, w, w, w],
							 [b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b],
							 [b, w, w, w, b, w, w, w, b, w, b, w, w, w, b, w, w, w, b],
							 [t, b, b, w, b, b, b, b, b, b, b, b, b, b, b, w, b, b, t],
							 [w, w, b, w, b, w, b, w, w, w, w, w, b, w, b, w, b, w, w],
							 [b, b, b, b, b, w, b, b, b, w, b, b, b, w, b, b, b, b, b],
							 [b, w, w, w, w, w, w, w, b, w, b, w, w, w, w, w, w, w, b],
							 [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b]])
		else:
			return ValueError('Invalid maze size "{}"'.format(size))

	return starting_pos, maze