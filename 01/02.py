elves = []
elf_temp = 0

with open("input.txt") as f:
	for cals in f:
		if cals == "\n":
			elves.append(elf_temp)
			elf_temp = 0
		else:
			elf_temp += int(cals)

elves.append(elf_temp)
elves.sort(reverse=True)

print(elves[0] + elves[1] + elves[2])