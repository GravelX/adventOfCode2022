import os
import itertools

# ==========================================
# Puzzle description:
# https://adventofcode.com/2022/day/13
# ==========================================

# ------------------------------------------
# Params
file_name = "input.txt"
verbose = False
# load input
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
data = [d.strip() for d in open(file_path, "r").readlines() if d != "\n"]

# ------------------------------------------
# Protects anything wack from being evaluated by the code in findPacketsOrder()
def inputSecured():
    characters_allowed = ["[","]",",","0","1","2","3","4","5","6","7","8","9"]
    for line in data:
        for char in line:
            if char not in characters_allowed: return False, char
    return True, None
# ------------------------------------------
# Adds the indices of the pairs of pack that are in the right order
def findOrderedPackets():
    secured, err = inputSecured()
    if not secured: raise Exception("Code should not be ran, unexpected character:",err)

    ordered_indices = []
    packet_index = 1

    # For every pair of packets
    for i in range(0, len(data), 2):
        left = eval(data[i])
        right = eval(data[i+1])
        if verbose: print("PAIR",packet_index,": ",left,"vs",right)

        # For each items in the packets
        for values in itertools.zip_longest(left, right):
            res = compareTwoValues(values[0], values[1])
            if res is True:
                ordered_indices.append(packet_index)
                if verbose: print("Packet at position",packet_index,"is ordered!")
                break
            elif res is False:
                if verbose: print("Packet at position",packet_index,"is in the wrong order!")
                break
        
        if verbose: print("----------------------------------------------------")
        packet_index += 1

    # Add up indices of ordered packet pairs
    print("Sum of the indices of ordered packet pairs:",sum(ordered_indices))

def compareExistence(a, b):
    if a is None: return True       # inputs are in the right order
    elif b is None: return False    # inputs are not in the right order
    else: return None               # continue

def compareTwoValues(a, b):
    if verbose: print("Compare",a,"to",b,end=" --> ")
    if (type(a) is not int and type(a) is not list and a is not None) or (type(b) is not int and type(b) is not list and b is not None):
        raise Exception("Error! Values can only be int or list, or None. Got",type(a),"and",type(b))
    
    ordered = compareExistence(a, b)
    if ordered is True:
        if verbose: print("Ordered!")
        return True
    elif ordered is False:
        if verbose: print("Wrong order!")
        return False
    else: # continue
        if type(a) is int and type(b) is int:
            if a < b:
                if verbose: print("Ordered!")
                return True
            elif a > b:
                if verbose: print("Wrong order!")
                return False
        elif type(a) is int:
            a = [a]
            return compareTwoValues(a, b)
        elif type(b) is int:
            b = [b]
            return compareTwoValues(a, b)
        else:
            sub_result = None
            for values in itertools.zip_longest(a, b):
                res = compareTwoValues(values[0], values[1])
                if res is True:
                    sub_result = True
                    break
                elif res is False:
                    sub_result = False
                    break

            if sub_result is True:
                if verbose: print("Ordered!")
                return True
            elif sub_result is False:
                if verbose: print("Wrong order!")
                return False

    if verbose: print("Continue (same value).")

def orderAllPackets():
    secured, err = inputSecured()
    if not secured: raise Exception("Code should not be ran, unexpected character:",err)

    # prepare input data
    packets = [eval(packet) for packet in data]
    # add divider packets
    packets.append([[2]])
    packets.append([[6]])

    made_a_change = True

    # While packets not all sorted out
    while made_a_change:
        made_a_change = False

        # For each two packets in the list
        for i in range(len(packets)-1):
            left = packets[i]
            right = packets[i+1]

            # For each items in the packets
            for values in itertools.zip_longest(left, right):
                res = compareTwoValues(values[0], values[1])
                if res is True:
                    break
                elif res is False:
                    packets[i], packets[i+1] = packets[i+1], packets[i]
                    made_a_change = True
                    break

    # Decode key is the indices of the two divider packets multiplied together
    key1, key2 = None, None
    for i, p in enumerate(packets):
        if p == [[2]]: key1 = i+1
        elif p == [[6]]: key2 = i+1
    print("Decodes key of the distress signal:",key1*key2)

# ------------------------------------------
# Main
def main():
    # Part 1
    findOrderedPackets()
    # Part 2
    orderAllPackets()

if __name__ == "__main__":
    main()