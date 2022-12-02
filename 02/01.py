ROCK = 1
PAPER = 2
SCISSORS = 3
LOSS = 0
DRAW = 3
WIN = 6
lookuptable = {
	"AY": PAPER + WIN,
	"AX": ROCK + DRAW,
	"AZ": SCISSORS + LOSS,
	"BY": PAPER + DRAW,
	"BX": ROCK + LOSS,
	"BZ": SCISSORS + WIN,
	"CY": PAPER + LOSS,
	"CX": ROCK + WIN,
	"CZ": SCISSORS + DRAW
}
totalscore = 0
with open("input.txt") as f:
	for line in f:
		line = line.replace(" ", "").strip()
		totalscore += lookuptable[line]

print(totalscore)

