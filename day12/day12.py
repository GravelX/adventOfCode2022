import os
import math

# ==========================================
# Puzzle description:
# https://adventofcode.com/2022/day/12
# ==========================================

# ------------------------------------------
# Params
file_name = "test_input.txt"

# ------------------------------------------
# Load the contents of the input file into a grid.
# Each square in the grid has: [elevation, visited, distance]
# Also returns starting point and destination coordinates.
def loadHeightMap():
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
    data = [d.strip() for d in open(file_path, "r").readlines()]
    grid, start, end = [], [], []

    for i, line in enumerate(data):
        row = []
        for j, d in enumerate(line):
            if d == 'S':
                start = [i, j]
                row.append([ord('a'), True, 0])
            elif d == 'E':
                end = [i, j]
                row.append([ord('z'), False, math.inf])
            else:
                row.append([ord(d), False, math.inf])
        grid.append(row)

    return grid, start, end

# ------------------------------------------
# Finds the fewest steps required to move from start point
# to the end point.
def findSmallestPath(grid, start, end):
    dijkstraTick(grid, start, grid[start[0]][start[1]][2])
    return grid[end[0]][end[1]][2]

def dijkstraTick(grid, pos, prev_dist):
    current_node = grid[pos[0]][pos[1]]

    # Set visited to true
    current_node[1] = True

    # Update distance score
    if prev_dist+1 < current_node[2]:
        current_node[2] = prev_dist+1

    # If there's a node above AND we can reach it AND we havent visited it yet, move there
    if pos[0]-1 >= 0 and grid[pos[0]-1][pos[1]][0] <= current_node[0]+1:
        # if already visited, just go there if distance is smaller
        if grid[pos[0]-1][pos[1]][1]:
            if grid[pos[0]-1][pos[1]][2] > current_node[2]+1: dijkstraTick(grid, [pos[0]-1, pos[1]], current_node[2])
        else:
            dijkstraTick(grid, [pos[0]-1, pos[1]], current_node[2])
        
    # If there's a node below and we can reach it, move there
    if pos[0]+1 < len(grid) and grid[pos[0]+1][pos[1]][0] <= current_node[0]+1:
        #print("Sending dijkstra over there!")
        if grid[pos[0]+1][pos[1]][1]:
            if grid[pos[0]+1][pos[1]][2] > current_node[2]+1: dijkstraTick(grid, [pos[0]+1, pos[1]], current_node[2])
        else:
            dijkstraTick(grid, [pos[0]+1, pos[1]], current_node[2])
            
    # If there's a node on the left and we can reach it, move there
    if pos[1]-1 >= 0 and grid[pos[0]][pos[1]-1][0] <= current_node[0]+1:
        if grid[pos[0]][pos[1]-1][1]:
            if grid[pos[0]][pos[1]-1][2] > current_node[2]+1: dijkstraTick(grid, [pos[0], pos[1]-1], current_node[2])
        else:
            dijkstraTick(grid, [pos[0], pos[1]-1], current_node[2])
    # If there's a node on the right and we can reach it, move there
    if pos[1]+1 < len(grid[0]) and grid[pos[0]][pos[1]+1][0] <= current_node[0]+1:
        if grid[pos[0]][pos[1]+1][1]:
            if grid[pos[0]][pos[1]+1][2] > current_node[2]+1: dijkstraTick(grid, [pos[0], pos[1]+1], current_node[2])
        else:
            dijkstraTick(grid, [pos[0], pos[1]+1], current_node[2])
        
    #displayGrid(grid)
    #print("-------------------------------")

def displayGrid(grid):
    for i,_ in enumerate(grid):
        for j,_ in enumerate(grid[0]):
            print('{:3.0f}'.format(grid[i][j][2]), end=" ")
        print()

# ------------------------------------------
# Main
def main():
    grid, start, end = loadHeightMap()
    #displayGrid(grid)
    print(findSmallestPath(grid, start, end))
    #print("------------------------------------------------")
    #displayGrid(grid)

if __name__ == "__main__":
    main()