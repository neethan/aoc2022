from dataclasses import *
from pprint import pprint

@dataclass
class Directory:
	items: int = 0
	subdirs: list[str] = field(default_factory=list)

total = 0
dirs = {}
limit = 100000

# Read size of a directory
def read_directory(d):
	if dirs[d].items > limit: return limit + 1
	dir_total = 0
	for subdir in dirs[d].subdirs:
		dir_total += read_directory(d + subdir)

	return dir_total + dirs[d].items if dir_total + dirs[d].items < limit else limit + 1

cwd = []
with open("input.txt") as f:
	temp = Directory()
	for line in f:
		line = line.strip().split(" ")
		if line[0] == "$":
			if line[1] == "cd":
				if line[2] == "..":
					cwd.pop()
				else:
					cwd.append(line[2])
			if line[1] == "ls":
				temp = Directory()
			continue

		# Read dir
		if line[0] == "dir":
			temp.subdirs.append(line[1])
		else:
			temp.items += int(line[0])
		dirs["".join(cwd)] = temp	

for d in dirs:
	if dirs[d].items > limit: continue
	dir_total = 0
	for subdir in dirs[d].subdirs:
		dir_total += read_directory(d + subdir)

	if dir_total + dirs[d].items < limit:
		total += dir_total + dirs[d].items

print(total)