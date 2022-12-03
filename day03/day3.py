import os

# ==========================================
# Puzzle description:
# https://adventofcode.com/2022/day/3
# ==========================================

# ------------------------------------------
# Params
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)

# ------------------------------------------
# Add the priorities of all missplaced items
def addPriorities():
    data = open(file_path, "r").readlines()
    priorities = 0

    for line in data:
        bag = line.strip()
        if len(bag)%2 != 0: raise Exception("Sheesh dog!")
        pocket_size = int(len(bag) / 2)
        first_pocket = bag[:pocket_size]
        second_pocket = bag[-pocket_size:]

        for item in first_pocket:
            if item in second_pocket:
                priorities += getPriority(item)
                break
    
    print("The sum of all missplaced items' priorities is", priorities, end=".\n")

# ------------------------------------------
# Returns the priority value of the item
def getPriority(item):
    if ord(item) > 96 and ord(item) < 123:
        # Lowercase item types 'a' through 'z' have priorities 1 through 26
        return ord(item) - 96
    elif ord(item) > 64 and ord(item) < 91:
        # Uppercase item types 'A' through 'Z' have priorities 27 through 52
        return ord(item) - 38
    else:
        raise Exception("Invalid item: Cannot find a priority.")

# ------------------------------------------
# Add the priority scores of the badges of each team
def addBadges():
    data = open(file_path, "r")
    priorities = 0

    while True:
        elf1 = data.readline().strip()
        if elf1 == "": break # End of file reached
        elf2 = data.readline().strip()
        elf3 = data.readline().strip()
        if elf2 == "" or elf3 == "": raise Exception("Cannot form a complete trio of Elves.")

        for item in elf1:
            if item in elf2 and item in elf3:
                # Badge item found
                priorities += getPriority(item)
                break

    print("The sum of all badges' priorities is", priorities, end=".\n")

# ------------------------------------------
# Main
def main():
    # Part 1
    addPriorities()

    # Part 2
    addBadges()

if __name__ == "__main__":
    main()