total = 0
grid = []

def check_direction(y, x):
	left, right, up, down = [False] * 4

	for i in range(0, len(grid)):
		if y == i: continue
		if grid[i][x] >= grid[y][x] and i < y:
			up = True
		if grid[i][x] >= grid[y][x] and i > y:
			down = True


	for i in range(0, len(grid[0])):
		if x == i: continue
		if grid[y][i] >= grid[y][x] and i < x:
			left = True
		if grid[y][i] >= grid[y][x] and i > x:
			right = True

	return left & right & up & down

with open("input.txt") as f:
	for line in f:
		grid.append([i for i in line.strip()])

	total += len(grid[0]) * 2 + len(grid) * 2 - 4

	for j in range(1, len(grid) - 1):
		for i in range(1, len(grid[0]) - 1):
			if not check_direction(j, i):
				total += 1
print(total)