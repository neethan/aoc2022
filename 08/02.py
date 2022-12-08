bestscore = 0
grid = []

def find_score(y, x):
	left, right, up, down = [0] * 4

	for x_pos in range(x - 1, -1, -1):
		left += 1
		if not grid[y][x_pos] < grid[y][x]:
			break

	for x_pos in range(x + 1, len(grid[0])):
		right += 1
		if not grid[y][x_pos] < grid[y][x]:
			break

	for y_pos in range(y - 1, -1, -1):
		up += 1
		if not grid[y_pos][x] < grid[y][x]:
			break

	for y_pos in range(y + 1, len(grid)):
		down += 1
		if not grid[y_pos][x] < grid[y][x]:
			break

	return left * right * up * down

with open("input.txt") as f:
	for line in f:
		grid.append([i for i in line.strip()])

	for j in range(1, len(grid) - 1):
		for i in range(1, len(grid[0]) - 1):
			temp = find_score(j, i)
			if temp > bestscore: bestscore = temp

print(bestscore)