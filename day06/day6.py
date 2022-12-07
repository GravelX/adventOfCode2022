import os

# ==========================================
# Puzzle description:
# https://adventofcode.com/2022/day/5
# ==========================================

# ------------------------------------------
# Params
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
data = open(file_path, "r").readline()

# ------------------------------------------
# Find datastream start
# k: kernel width
def findMarker(k):
    start_pos = -1
    for i in range(k, len(data)+1):
        window = data[i-k:i]
        start = True
        for c in window:
            if window.count(c) >= 2:
                start = False
                break
        if start:
            start_pos = i
            break

    return start_pos

# ------------------------------------------
# Main
def main():
    # Part 1
    pos = findMarker(4)
    print("Datastream starts on the "+str(pos)+"th character.")

    # Part 2
    pos = findMarker(14)
    print("Message starts on the "+str(pos)+"th character.")


if __name__ == "__main__":
    main()