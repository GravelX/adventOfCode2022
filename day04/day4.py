import os

# ==========================================
# Puzzle description:
# https://adventofcode.com/2022/day/4
# ==========================================

# ------------------------------------------
# Params
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
data = open(file_path, "r").readlines()
visualize_overlaps = False
# CLeanup
data = [d.strip() for d in data]

# ------------------------------------------
# Counts in how many assignment pairs does one range fully contain the other
def findFullOverlaps():
    full_overlaps = 0
    for pairs in data:
        p1, p2 = pairs.split(",")
        range1 = [int(r) for r in p1.split("-")]
        range2 = [int(r) for r in p2.split("-")]
        if (range1[0]>=range2[0] and range1[1]<=range2[1]) or (range2[0]>=range1[0] and range2[1]<=range1[1]):full_overlaps += 1

    print("One range is fully contained in the other in", full_overlaps, "cases.")

# ------------------------------------------
# Counts how many assignment pairs have overlapping range
def findOverlaps():
    overlaps = 0
    for pairs in data:
        p1, p2 = pairs.split(",")
        range1 = [int(r) for r in p1.split("-")]
        range2 = [int(r) for r in p2.split("-")]
        if (range2[0] <= range1[0] <= range2[1]) or (range2[0] <= range1[1] <= range2[1]):
            if visualize_overlaps:printOverlap(range1,range2)
            overlaps += 1
        elif (range1[0] <= range2[0] <= range1[1]) or (range1[0] <= range2[1] <= range1[1]):
            if visualize_overlaps:printOverlap(range1,range2)
            overlaps += 1

    print("Assignements contain",overlaps,"overlaps.")

# ------------------------------------------
# Visualize overlaps (for debugging)
def printOverlap(range1,range2):
    kekw=0
    for i in range(0,range1[0]):
        print("-",end="")
        kekw += 1
    for i in range(range1[0],range1[1]+1):
        print("O",end="")
        kekw += 1
    for i in range(kekw+1,101):
        print("-",end="")
    print("")
    kekw=0
    for i in range(0,range2[0]):
        print("-",end="")
        kekw += 1
    for i in range(range2[0],range2[1]+1):
        print("O",end="")
        kekw += 1
    for i in range(kekw+1,101):
        print("-",end="")
    print("\n")

# ------------------------------------------
# Main
def main():
    # Part 1
    findFullOverlaps()

    # Part 2
    findOverlaps()

if __name__ == "__main__":
    main()