import os

# ------------------------------------------
# Params
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
data = open(file_path, "r").readlines()
# [key: hand sign, value: wins over] (ex: A(rock) wins over Z(scissors))
winCons = {
    "A": "Z",
    "B": "X",
    "C": "Y",
    "X": "C",
    "Y": "A",
    "Z": "B"
}
# Points for sign thrown
points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

# ------------------------------------------
# Compute the score : shape you selected plus the score for the outcome of the round
def roshamboScore(opps, player):
    score = 0
    if opps == winCons[player]:
        # Player win
        score += 6
    elif player != winCons[opps]:
        # Draw
        score += 3
    return score + points[player]

# ------------------------------------------
# Add up scores of all rounds
def addTotalScores():
    total_score = 0

    for line in data:
        opps, player = line.split(" ")
        total_score += roshamboScore(opps, player.strip())

    print("Part1 - Total score from the strategy guide is",total_score)

# # ------------------------------------------
# Returns what shape you should play to achieve outcome
def whatToPlay(opps, outcome):
    choices = ["X", "Y", "Z"]
    losingSign = winCons[opps]
    winningSign = [k for k, v in winCons.items() if v == opps].pop()
    choices.remove(winningSign)
    choices.remove(losingSign)
    drawSign = choices.pop()

    if outcome == "Z":
        # Need to win
        return winningSign
    elif outcome == "X":
        # Need to lose
        return losingSign
    elif outcome == "Y":
        # Need to draw
        return drawSign
    else:
        raise Exception("Invalid outcome key.")

# ------------------------------------------
# Add up scores but with new strategy
def playTheGuide():
    total_score = 0

    for line in data:
        opps, outcome = line.split(" ")
        player = whatToPlay(opps, outcome.strip())
        total_score += roshamboScore(opps, player)

    print("Part2 - Total score from the strategy guide is",total_score)

# ------------------------------------------
# Main
def main():
    # Part 1
    addTotalScores()

    # Part 2
    playTheGuide()

if __name__ == "__main__":
    main()