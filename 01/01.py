elf_temp = 0
elf_most = 0

with open("input.txt") as f:
	for cals in f:
		if cals == "\n":
			if elf_temp > elf_most:
				elf_most = elf_temp
			elf_temp = 0
		else:
			elf_temp += int(cals)

print(elf_most)