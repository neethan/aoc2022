totalscore = 0
with open("input.txt") as f:
	for line in f:
		line = line.strip()
		first, second = set(line[:len(line)//2]), set(line[len(line)//2:])
		common = "".join(first.intersection(second))
		totalscore += ord(common) - 96 if common.islower() else ord(common) - 38

print(totalscore)

