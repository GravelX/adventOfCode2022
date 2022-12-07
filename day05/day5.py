import os
import re

# ==========================================
# Puzzle description:
# https://adventofcode.com/2022/day/5
# ==========================================

# ------------------------------------------
# Params
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
data = open(file_path, "r").readlines()
# CLeanup
data = [d.replace("\n","") for d in data]

# ------------------------------------------
# Extract stacks and the moves from the input
def init():
    # Init stacks
    stack_data = data[:8]
    stack_data = [l.replace("    ","-") for l in stack_data]
    stacks = [[] for i in range(9)]

    for l in reversed(stack_data):
        stack = 0
        for c in l:
            if (64 < ord(c) < 91):
                stacks[stack].append(c)
                stack += 1
            elif c == "-":
                stack += 1

    # Init moves
    moves = [re.findall(r'\d+',l) for l in data[-503:]] # [qty, from, to]
    moves = [[int(v) for v in m] for m in moves]

    return stacks, moves

# ------------------------------------------
# Display the crates on top of the stacks
def display(stacks, model):
    print("Crates on top after the rearrangement (v"+model+"): ",end="")
    for s in stacks:
        print(s[-1],end="")
    print("")

# ------------------------------------------
# Find the crates on top of the stacks after the rearrangement
# CrateMover 9000 algorithm
def topCrates9000(stacks, moves):
    # Apply the move on the stack
    for move in moves:
        qty, origin, dest = move
        for i in range(qty): stacks[dest-1].append(stacks[origin-1].pop())

    # Display
    display(stacks, "9000")

# ------------------------------------------
# Find the crates on top of the stacks after the rearrangement
# CrateMover 9001 algorithm
def topCrates9001(stacks, moves):
    # Apply the move on the stack
    for move in moves:
        qty, origin, dest = move
        payload = stacks[origin-1][-qty:]
        
        for crate in payload:
            stacks[origin-1].pop()
            stacks[dest-1].append(crate)

    # Display
    display(stacks, "9001")

# ------------------------------------------
# Main
def main():
    # Part 1
    stacks, moves = init()
    topCrates9000(stacks, moves)
    # Part 2
    stacks, moves = init()
    topCrates9001(stacks, moves)

if __name__ == "__main__":
    main()