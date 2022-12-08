from dataclasses import *
from pprint import pprint

@dataclass
class Directory:
	items: int = 0
	subdirs: list[str] = field(default_factory=list)

dirs = {}
dirs_realspace = {}

# Read size of a directory
def read_directory(d):
	dir_total = 0
	for subdir in dirs[d].subdirs:
		dir_total += read_directory(d + subdir)
	return dir_total + dirs[d].items

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
	dir_total = 0
	for subdir in dirs[d].subdirs:
		dir_total += read_directory(d + subdir)
	dirs_realspace[d] = dir_total + dirs[d].items

current_space = 70000000 - int(dirs_realspace["/"])
sorted_dirs = sorted(list(dirs_realspace.values()))
best = 1000000000000
for size in sorted_dirs:
	if current_space + size > 30000000 and size < best: best = size

print(best)
