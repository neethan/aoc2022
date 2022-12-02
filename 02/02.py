ROCK = 1
PAPER = 2
SCISSORS = 3
LOSS = 0
DRAW = 3
WIN = 6
lookuptable = {
	"AY": ROCK + DRAW,
	"AX": SCISSORS + LOSS,
	"AZ": PAPER + WIN,
	"BY": PAPER + DRAW,
	"BX": ROCK + LOSS,
	"BZ": SCISSORS + WIN,
	"CY": SCISSORS + DRAW,
	"CX": PAPER + LOSS,
	"CZ": ROCK + WIN
}
totalscore = 0
with open("input.txt") as f:
	for line in f:
		line = line.replace(" ", "").strip()
		totalscore += lookuptable[line]

print(totalscore)

