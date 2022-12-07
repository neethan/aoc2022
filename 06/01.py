chars = []
with open("input.txt") as f:
	for i, char in enumerate(f.readline().strip()):
		if len(chars) == 4: chars.pop()
		chars.insert(0, char)
		if len(set(chars)) == len(chars) and len(chars) == 4:
			print(i + 1)
			exit()