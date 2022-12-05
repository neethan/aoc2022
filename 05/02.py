import re

stacks = []

with open("input.txt") as f:
	for line in f:
		line = line.rstrip('\n')
		# Stop parsing after data in
		if not line:
			break

		# Strip off everything not a number and split
		split = [line[i:i+4].strip() for i in range(0, len(line), 4)]
		split = [re.sub('[\]\[]', '', x) for x in split]

		# Skip number line
		if split[-1].isnumeric():
			continue

		# Init stacks
		if stacks == []:
			stacks = [[] for i in range(len(split))]

		# Insert crates
		for i, crate in enumerate(split):
			stacks[i].insert(0, crate)

	# Remove blank crates
	for i, stack in enumerate(stacks):
		stacks[i] = [x for x in stacks[i] if x]

	for line in f:
		line = line.strip()
		split = line.split(" ")
		split = [int(i) for i in split if i.isnumeric()]
		
		items = []
		for i in range(0, split[0]):
			items.insert(0, stacks[split[1] - 1].pop())

		stacks[split[2] - 1].extend(items)

for stack in stacks:
	print(stack[-1], end = '')

print("")

