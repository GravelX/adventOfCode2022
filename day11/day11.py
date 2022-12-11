from tqdm.auto import tqdm
from utils import loadMonkers, displayMonkeys

# ==========================================
# Puzzle description:
# https://adventofcode.com/2022/day/11
# ==========================================

# ------------------------------------------
# Simulate the monkeys throwing each other items
# for the specified amount of rounds.
# Rounds: number of rounds simulated
# Panic Mode: True if the worry levels should no longer be divided by 3
def simulateMonkeys(rounds, panic_mode):
    monkeys = loadMonkers(panic_mode)
    monkey_business = []

    for r in tqdm(range(rounds)):
    #for r in range(rounds):
        for m in monkeys:
            targets = []
            # For each item, compute new worry levels and what monkey to throw it to.
            for i in range(len(m.items)):
                targets.append(m.inspect_item(i))
            # Throw the items
            for i in range(len(m.items)):
                monkeys[targets[i]].items.append(m.items[i])
            m.items = []
    
    # Get number of inspections performed by each monkey
    for m in monkeys: monkey_business.append(m.inspections)
    monkey_business.sort()

    print("The two most active monkeys have a monkey business level of",monkey_business[-2]*monkey_business[-1], end=".\n")

# ------------------------------------------
# Main
def main():
    # Part 1
    simulateMonkeys(rounds=20, panic_mode=False)

    # Part 2
    simulateMonkeys(rounds=10000, panic_mode=True)

if __name__ == "__main__":
    main()