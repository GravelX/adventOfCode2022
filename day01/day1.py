import os

# ==========================================
# Puzzle description:
# https://adventofcode.com/2022/day/1
# ==========================================

# ------------------------------------------
# Params
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)

# ------------------------------------------
# Returns the index of the Elf carrying the most calories
# as well as the number of calories he is carrying.
def findMaxCalories():
    data = open(file_path, "r").readlines()
    maxElf, maxCal, currentCount, elfCounter = 0, 0, 0, 0

    for line in data:
        if line == "\n":
            # End of a section
            if currentCount > maxCal:
                # New max
                maxCal = currentCount
                maxElf = elfCounter
            elfCounter += 1
            currentCount = 0
        else:
            currentCount += int(line)

    print("The Elf at position", maxElf, "is carrying the most calories ("+str(maxCal)+").")

# ------------------------------------------
# Returns the sum of the 3 elves carrying the most calories.
def addTop3():
    data = open(file_path, "r").readlines()
    totals = []
    currentCount = 0

    for line in data:
        if line == "\n":
            # End of a section
            totals.append(currentCount)
            currentCount = 0
        else:
            currentCount += int(line)

    # Add the last 3 elements of the sorted list of calories totals
    top3 = sum(sorted(totals)[-3:])
    print("The top 3 elves carry together",top3,"calories.")

# ------------------------------------------
# Main
def main():
    # Part 1
    findMaxCalories()

    # Part 2
    addTop3()

if __name__ == "__main__":
    main()
