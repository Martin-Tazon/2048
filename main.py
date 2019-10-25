import numpy as np
import random

random.seed(0)

n=4
grid=np.zeros([n,n]).astype(int)

def print_grid(g):
	gn = g.shape[0]
	art = ''
	for row in range(gn):
		for col in range(gn):
			art = art + str(g[row][col]) + ' '
		art = art + '\n'
	print()	
	print (art)
	print()	

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
		print ('GAME OVER!')
		return True
	else:
		return False

def make_move(g):
	gn = g.shape[0]
	# Get the move
	while True:
		move = input("Please enter a move... ")
		if move in ['a','s','d','w']: break
	
	if move == 'w':
		first = True
		change = True
		while change:
			change = False
			for row in range(gn):
				for col in range(gn): 
					if row == 0: continue
					if g[row][col] != 0:
						if g[row-1][col] == 0:
							g[row-1][col] = g[row][col]
							g[row][col] = 0
							change=True
			if first and not change:
				print ('Invalid move, try again!')
				print_grid(g)
				make_move(g)
			first = False
	elif move == 's':
		first = True
		change = True
		while change:
			change = False
			for row in range(gn):
				for col in range(gn): 
					if row == 3: continue
					if g[row][col] != 0:
						if g[row+1][col] == 0:
							g[row+1][col] = g[row][col]
							g[row][col] = 0
							change=True
			if first and not change:
				print ('Invalid move, try again!')
				print_grid(g)
				make_move(g)
			first = False

	elif move == 'd':
		first = True
		change = True
		while change:
			change = False
			for row in range(gn):
				for col in range(gn): 
					if col == 3: continue
					if g[row][col] != 0:
						if g[row][col+1] == 0:
							g[row][col+1] = g[row][col]
							g[row][col] = 0
							change=True
						#elif g[row][col+1] == g[row][col]:
						#	change = True
			if first and not change:
				print ('Invalid move, try again!')
				print_grid(g)
				make_move(g)
				return g
			first = False
		for row in range(gn):
			for col in range(gn):
				if col == 3: continue
				if g[row][col] != 0:
					if g[row][col+1] == g[row][col]:
						g[row][col+1] = g[row][col+1]*2
						g[row][col] = 0
		change = True
		while change:
			change = False
			for row in range(gn):
				for col in range(gn): 
					if col == 3: continue
					if g[row][col] != 0:
						if g[row][col+1] == 0:
							g[row][col+1] = g[row][col]
							g[row][col] = 0
							change=True

	elif move == 'a':
		first = True
		change = True
		while change:
			change = False
			for row in range(gn):
				for col in range(gn): 
					if col == 0: continue
					if g[row][col] != 0:
						if g[row][col-1] == 0:
							g[row][col-1] = g[row][col]
							g[row][col] = 0
							change=True
						elif g[row][col-1] == g[row][col]:
							change=True
			if first and not change:
				print ('Invalid move, try again!')
				print_grid(g)
				make_move(g)
				return g
			first = False
		for row in range(gn):
			for col in range(gn):
				if col == 0: continue
				if g[row][col] != 0:
					if g[row][col-1] == g[row][col]:
						g[row][col-1] = g[row][col-1]*2
						g[row][col] = 0
		change = True
		while change:
			change = False
			for row in range(gn):
				for col in range(gn): 
					if col == 0: continue
					if g[row][col] != 0:
						if g[row][col-1] == 0:
							g[row][col-1] = g[row][col]
							g[row][col] = 0
							change=True

	return g

# Init board
grid = add_new(grid)

# Main loop
while True:
	if check_if_gameover(grid): break
	# Possibildad de undo ?
	grid = add_new(grid)
	print_grid(grid)
	if check_if_gameover(grid): break
	
	grid = np.zeros([n,n]).astype(int)
	grid[0][0]=2
	grid[0][1]=2
	print_grid(grid)
	# Make move
	make_move(grid)
	print ('Move done')
	print_grid(grid)

