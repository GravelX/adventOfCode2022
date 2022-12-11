import os
from Monkey import Monkey

# ------------------------------------------
# Displays monkeys (debugging)
def displayMonkeys(monkeys):
    print("---------------------------------")
    for i, monko in enumerate(monkeys):
        print("Monkey",i)
        print("  items:",monko.items)
        print("  rule:",monko.rule,end="\n\n")

# ------------------------------------------
# Load Monkers : Generate the monkey objects from input
def loadMonkers():
    file_name = "input.txt"
    monkeys = []
    items, args, rule = None, None, []

    # Load file
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
    data = [d.strip() for d in open(file_path, "r").readlines()]

    # Parse data
    for line in data:
        if "Starting items" in line:
            items = [int(val) for val in line.split("Starting items: ")[1].split(", ")]
        elif "Operation" in line:
            args = line.split("new = old ")[1]
        elif "Test" in line:
            rule.append(int(line.split("divisible by ")[1]))
        elif "If true" in line:
            rule.append(int(line[-1]))
        elif "If false" in line:
            rule.append(int(line[-1]))
            if items is None or args is None or not rule:
                raise Exception("Cannot create monkey: Invalid arguments\nitems:",items,"\nargs:",args,"\nrule:",rule)
            monkeys.append(Monkey(items, args, rule))
            items, args, rule = None, None, []

    return monkeys