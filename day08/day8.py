import os
import numpy as np

# ==========================================
# Puzzle description:
# https://adventofcode.com/2022/day/8
# ==========================================

# ------------------------------------------
# Params
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
data = [list(d.strip()) for d in open(file_path, "r").readlines()]
tree_grid = (np.array(data)).astype(np.int32)

# ------------------------------------------
# Returns array as viewed from given position and direction
def look(array, pos, direction):
    if direction=="left":
        return array[pos[0]][:pos[1]]
    elif direction=="right":
        return array[pos[0]][-(array.shape[1]-pos[1]-1):]
    elif direction=="up":
        return array[:,pos[1]][:pos[0]]
    elif direction=="down":
        return array[:,pos[1]][-(array.shape[0]-pos[0]-1):]
    else:
        raise Exception("Invalid direction.")

# ------------------------------------------
# Returns the number of trees visible from outside the grid
def analyseVisibility():
    visible_trees = 0
    # Count visible trees
    with np.nditer(tree_grid, flags=['multi_index']) as it:
        for tree in it:
            if it.multi_index[0]==0 or it.multi_index[0]==tree_grid.shape[0]-1 or it.multi_index[1]==0 or it.multi_index[1]==tree_grid.shape[1]-1:
                # tree on the border (visible by default)
                visible_trees+=1
            else:
                # Look left
                max_to_its_left = np.amax(look(tree_grid, it.multi_index, "left"))
                if tree > max_to_its_left:
                    visible_trees+=1
                    continue # No need to perform other checks
                # Look righ
                max_to_its_right = np.amax(look(tree_grid, it.multi_index, "right"))
                if tree > max_to_its_right:
                    visible_trees+=1
                    continue # No need to perform other checks
                # Look up
                max_above = np.amax(look(tree_grid, it.multi_index, "up"))
                if tree > max_above:
                    visible_trees+=1
                    continue # No need to perform other checks
                # Look down
                max_below = np.amax(look(tree_grid, it.multi_index, "down"))
                if tree > max_below:
                    visible_trees+=1

    print("There are",visible_trees,"trees visible from outside the grid.")

# ------------------------------------------
# Returns the highest scenic score possible
def analyseScenery():
    best_score = 0
    # Compute scenic score for every tree and track the best score
    with np.nditer(tree_grid, flags=['multi_index']) as it:
        for tree in it:
            l_trees,r_trees,u_trees,d_trees = 0,0,0,0

            # Look left
            if it.multi_index[1]!=0:
                # Not on left border
                l_view = look(tree_grid, it.multi_index, "left")
                for t in reversed(l_view):
                    l_trees+=1
                    if t>=tree:break
            else:
                continue # Tree score is 0
            # Look right
            if it.multi_index[1]!=tree_grid.shape[1]-1:
                # Not on right border
                r_view = look(tree_grid, it.multi_index, "right")
                for t in r_view:
                    r_trees+=1
                    if t>=tree:break
            else:
                continue # Tree score is 0
            # Look up
            if it.multi_index[0]!=0:
                # Not on top border
                u_view = look(tree_grid, it.multi_index, "up")
                for t in reversed(u_view):
                    u_trees+=1
                    if t>=tree:break
            else:
                continue # Tree score is 0
            # Look down
            if it.multi_index[0]!=tree_grid.shape[0]-1:
                # Not on bottow border
                d_view = look(tree_grid, it.multi_index, "down")
                for t in d_view:
                    d_trees+=1
                    if t>=tree:break
            else:
                continue # Tree score is 0

            # Update high score
            score = l_trees*r_trees*u_trees*d_trees
            if score>best_score: best_score=score

    print("The highest scenic score on the grid is",best_score,end=".\n")

# ------------------------------------------
# Main
def main():
    # Part 1
    analyseVisibility()
    # Part 2
    analyseScenery()

if __name__ == "__main__":
    main()