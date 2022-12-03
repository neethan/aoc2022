from itertools import islice
print(-1 % 58)
totalscore = 0
with open("input.txt") as f:
	while True:
		first = f.readline().strip()
		second = f.readline().strip()
		third = f.readline().strip()
		if not first:
			break

		common = "".join(set(first) & set(second) & set(third))
		totalscore += (ord(common) - 96) % 58

print(totalscore)

