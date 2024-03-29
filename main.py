import numpy as np
import random
import matplotlib.pyplot as plt

# plt.imshow on grid to print a heatmap
# Cuando add_new llena el grid, puede no ser game over si hay movimientos possibles!!


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

def check_if_gameover(g):
	if 0 not in g:
		# Check if moves possible
		gn = g.shape[0]
		for row in range(gn):
			for col in range(gn):
				if row == gn-1 and col == gn-1:
					continue
				elif row == gn-1:
					if g[row][col+1] == g[row][col]:
						return False
				elif col == gn-1:
					if g[row+1][col] == g[row][col]:
						return False
				else:
					if g[row+1][col] == g[row][col] or g[row][col+1] == g[row][col]:
						print('Moves are possible')
						return False
		# If function never exits with False, is Game Over!
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
		for col in range(gn): 
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

# --- MAIN --- #
# Init board
random.seed(0)

n=4


fn = input('Enter saved game name: (Press enter to start new) ')

if fn == '':
	grid=np.zeros([n,n]).astype(int)
	grid = add_new(grid)
	grid = add_new(grid)
else:
	fh = open(fn)
	gridList = []
	for line in fh:
		line = line.strip()
		gridList.append(line.split())
	grid = np.array(gridList).astype(int)

first=True
# Main loop
while True:
	# Possibildad de undo ?
	if not first:
		grid = add_new(grid)
	print_grid(grid)
	if check_if_gameover(grid): break

	# Make move
	make_move(grid)
	print_grid(grid)
	first = False


