totalscore = 0
with open("input.txt") as f:
	for line in f:
		ranges = sum([x.split("-") for x in line.strip().split(",")], [])
		first = set(range(int(ranges[0]), int(ranges[1]) + 1))
		second = set(range(int(ranges[2]), int(ranges[3]) + 1))

		if len(first.intersection(second)) > 0:
			totalscore += 1

print(totalscore)

