# ------------------------------------------
# Monkeys handle their items, how the modify them
# and who they throw them to.
class Monkey():
    def __init__(self, items, args, rule):
        self.inspections = 0
        self.items = items
        self.update_item = self.generate_operation(args)
        self.rule = rule # [divisible by, if true, if false]
        self.panicking = False
        self.ppcm = None # Multiple commun entre les monkeys

    # Generates the function that will become self.update_item()
    def generate_operation(self, args):
        operator, val = args.split(" ")
        if val=="old":
            if operator=="+":
                def f(self, i): self.items[i] = self.items[i] + self.items[i]
            elif operator=="*":
                def f(self, i): self.items[i] = self.items[i] * self.items[i]
        else:
            if operator=="+":
                def f(self, i): self.items[i] = self.items[i] + int(val)
            elif operator=="*":
                def f(self, i): self.items[i] = self.items[i] * int(val)
        
        return f

    # Inspect an item: Update the worry levels then return where to throw the item
    def inspect_item(self, i):
        self.update_item(self, i)
        self.handle_worries(i)
        self.inspections += 1

        if self.items[i]%self.rule[0]==0: return self.rule[1]
        else: return self.rule[2]

    # Replaces the item (worry level) by the smallest value but same behavior
    def handle_worries(self, i):
        if self.panicking:
            self.items[i] %= self.ppcm
        else:
            self.items[i] //= 3