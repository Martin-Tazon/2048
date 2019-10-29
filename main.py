import numpy as np
import random
import matplotlib.pyplot as plt

# plt.imshow on grid to print a heatmap
# Cuando ass_new llena el grid, puede no ser game over si hay movimientos possibles!!

random.seed(0)

n=4
grid=np.zeros([n,n]).astype(int)

def print_grid(g):
	gn = g.shape[0]
	art = ' '
	for row in range(gn):
		for col in range(gn):
			art = art + str(g[row][col]) + '\t'
		art = art + '\n\n '
	print()	
	print (art)

def check_if_free(g,i,j):
	return g[i][j] == 0

def add_new(g):
	#First check if game over
	gn = g.shape[0]
	added = False
	while not added:
		i = random.randint(0,gn-1)
		j = random.randint(0,gn-1)
	
		if g[i][j] == 0:
			g[i][j] = 2
			added = True
	return g

def check_if_gameover(g): # Need to check if any move possible
	# THIS IS WRONG
	if 0 not in g:
		print ('GAME OVER!')
		return True
	else:
		return False

def move_down(g):
	gn = g.shape[0]
	posinv = False
	first = True
	possible = True
	# Group
	while possible:
		possible = False
		for row in range(gn):
			for col in range(gn): 
				if row == gn-1: continue
				if g[row][col] != 0:
					if g[row+1][col] == 0:
						g[row+1][col] = g[row][col]
						g[row][col] = 0
						possible=True
		# Check if may be invalid
		if first and not possible:
			posinv = True
		first = False
	
	# Add
	added=False
	for row in reversed(range(n)):
		for col in range(gn): 
			if row == 0: continue
			if g[row][col] != 0:
				if g[row-1][col] == g[row][col]:
					g[row][col] = g[row-1][col] * 2
					g[row-1][col] = 0
					added=True
		
	# Check if invalid and if is ask for new move then return
	if posinv and not added:
		print ('Invalid move, try again!')
		print_grid(g)
		g = make_move(g)
		return g

	# Group
	possible = True
	while possible:
		possible = False
		for row in range(gn):
			for col in range(gn): 
				if row == gn-1: continue
				if g[row][col] != 0:
					if g[row+1][col] == 0:
						g[row+1][col] = g[row][col]
						g[row][col] = 0
						possible=True

	return g

def move_up(g):
	gn = g.shape[0]
	posinv = False
	first = True
	possible = True
	# Group
	while possible:
		possible = False
		for row in range(gn):
			for col in range(gn): 
				if row == 0: continue
				if g[row][col] != 0:
					if g[row-1][col] == 0:
						g[row-1][col] = g[row][col]
						g[row][col] = 0
						possible=True
		# Check if may be invalid
		if first and not possible:
			posinv = True
		first = False
	
	# Add
	added=False
	for row in range(gn):            	
		for col in range(gn): 
			if row == gn-1: continue              
			if g[row][col] != 0:
				if g[row+1][col] == g[row][col]:
					g[row][col] = g[row+1][col] * 2
					g[row+1][col] = 0
					added=True
	
	# Check if invalid and if is ask for new move then return
	if posinv and not added:
		print ('Invalid move, try again!')
		print_grid(g)
		g = make_move(g)
		return g

	# Group
	possible = True
	while possible:
		possible = False
		for row in range(gn):
			for col in range(gn): 
				if row == 0: continue
				if g[row][col] != 0:
					if g[row-1][col] == 0:
						g[row-1][col] = g[row][col]
						g[row][col] = 0
						possible=True

	return g

def move_right(g):
	gn = g.shape[0]
	posinv = False
	first = True
	possible = True
	# Group
	while possible:
		possible = False
		for row in range(gn):
			for col in range(gn): 
				if col == gn-1: continue
				if g[row][col] != 0:
					if g[row][col+1] == 0:
						g[row][col+1] = g[row][col]
						g[row][col] = 0
						possible=True
		# Check if may be invalid
		if first and not possible:
			posinv = True
		first = False
	
	# Add
	added=False
	for row in range(gn):            	
		for col in reversed(range(gn)): 
			if col == 0: continue
			if g[row][col] != 0:
				if g[row][col-1] == g[row][col]:
					g[row][col] = g[row][col-1] * 2
					g[row][col-1] = 0
					added=True
	
	# Check if invalid and if is ask for new move then return
	if posinv and not added:
		print ('Invalid move, try again!')
		print_grid(g)
		g = make_move(g)
		return g

	# Group
	possible = True
	while possible:
		possible = False
		for row in range(gn):
			for col in range(gn): 
				if col == gn-1: continue
				if g[row][col] != 0:
					if g[row][col+1] == 0:
						g[row][col+1] = g[row][col]
						g[row][col] = 0
						possible=True

	return g

def move_left(g):
	gn = g.shape[0]
	posinv = False
	first = True
	possible = True
	# Group
	while possible:
		possible = False
		for row in range(gn):
			for col in range(gn): 
				if col == 0: continue
				if g[row][col] != 0:
					if g[row][col-1] == 0:
						g[row][col-1] = g[row][col]
						g[row][col] = 0
						possible=True
		# Check if may be invalid
		if first and not possible:
			posinv = True
		first = False
	
	# Add
	added=False
	for row in range(gn):            	
		for col in reversed(range(gn)): 
			if col == gn-1: continue
			if g[row][col] != 0:
				if g[row][col+1] == g[row][col]:
					g[row][col] = g[row][col+1] * 2
					g[row][col+1] = 0
					added=True
	
	# Check if invalid and if is ask for new move then return
	if posinv and not added:
		print ('Invalid move, try again!')
		print_grid(g)
		g = make_move(g)
		return g

	# Group
	possible = True
	while possible:
		possible = False
		for row in range(gn):
			for col in range(gn): 
				if col == 0: continue
				if g[row][col] != 0:
					if g[row][col-1] == 0:
						g[row][col-1] = g[row][col]
						g[row][col] = 0
						possible=True

	return g


def make_move(g):
	'''	A move is:
			1.Group (If no movs possible invalid)
			2.Add	(If possible and no add -> invalid move)
			3.Group'''

	gn=g.shape[0]
	while True:
		move = input("Please enter a move... ")
		if move in ['a','s','d','w']: break
		
	if move == 's':
		return move_down(g)
	elif move == 'w':
		return move_up(g)
	elif move == 'd':
		return move_right(g)
	elif move == 'a':
		return move_left(g)


# Init board
grid = add_new(grid)

# Main loop
while True:
	if check_if_gameover(grid): break
	# Possibildad de undo ?
	grid = add_new(grid)
	print_grid(grid)
	if check_if_gameover(grid): break

	# Make move
	make_move(grid)
	print_grid(grid)


