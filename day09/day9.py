import os

# ==========================================
# Puzzle description:
# https://adventofcode.com/2022/day/9
# ==========================================

# ------------------------------------------
# Params
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
data = [d.strip() for d in open(file_path, "r").readlines()]

# ------------------------------------------
# Node objects move through the grid (knots)
class Node:
    def __init__(self):
        self.prev_x = None
        self.prev_y = None
        self.x = 0
        self.y = 0

    def move(self, direction):
        self.prev_x = self.x
        self.prev_y = self.y
        if   direction=="L": self.x-=1
        elif direction=="R": self.x+=1
        elif direction=="U": self.y+=1
        elif direction=="D": self.y-=1
        else: raise Exception("Wrong direction:", direction)

    def follow(self, target):
        vx = self.x-target.x
        vy = self.y-target.y
        if abs(vx)>1 or abs(vy)>1: # knot gets pulled
            self.prev_x = self.x
            self.prev_y = self.y
            if abs(vx)>abs(vy): # horizontal pull
                self.x = target.x-1 if vx<0 else target.x+1
                self.y = target.y
            elif abs(vy)>abs(vx): # vertical pull
                self.x = target.x
                self.y = target.y-1 if vy<0 else target.y+1
            elif abs(vx)==abs(vy): # diagonal pull
                self.x = target.prev_x
                self.y = target.prev_y
            else: raise Exception("If you see this, maths aren't real. Give up.")

# ------------------------------------------
# Simulates the movements of the rope and count
# how many positions its tail visit at least once.
def simulateRope(knots):
    visited_positions = [[0,0]]
    rope = [Node() for i in range(knots)]
    # Apply each move
    for move in data:
        direction, steps = move.split(" ")
        for s in range(int(steps)):
            # move head
            rope[0].move(direction)
            # apply physics to the rest of the rope
            for n in range(1,len(rope)):
                rope[n].follow(rope[n-1])
            # count newly visited positions by the tail
            if [rope[-1].x,rope[-1].y] not in visited_positions:
                visited_positions.append([rope[-1].x,rope[-1].y])

    print("The tail of the rope visited",len(visited_positions),"positions at least once.")

# ------------------------------------------
# Displays the grid and the nodes in it (debugging)
def printGridState(rope):
    # grid size hardcoded for part 1 test input
    grid = [["." for i in range(5)] for j in range(6)]
    for k, knot in enumerate(reversed(rope)):
        if k==len(rope)-1:grid[knot.x][knot.y]="H"
        else:grid[knot.x][knot.y]=str(len(rope)-1-k)
    for x in reversed(range(len(grid[0]))):
        for y in range(len(grid)):print(grid[y][x],end=" ")
        print("")

# ------------------------------------------
# Main
def main():
    # Part 1
    print("Part 1: ",end="")
    simulateRope(2)
    # Part 2
    print("Part 2: ",end="")
    simulateRope(10)

if __name__ == "__main__":
    main()