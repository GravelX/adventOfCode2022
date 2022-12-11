# ------------------------------------------
# Monkeys handle their items, how the modify them
# and who they throw them to.
class Monkey():
    def __init__(self, items, args, rule, div_by):
        self.inspections = 0
        self.items = items
        self.update_item = self.generate_operation(args)
        self.rule = rule # [divisible by, if true, if false]
        self.div_by = div_by
        self.worry_cap = 1000 # Max worry level allowed

    # Generates the function that will become self.update_item()
    def generate_operation(self, args):
        operator, val = args.split(" ")
        if val=="old":
            if operator=="+":
                def f(self, i): self.items[i] = (self.items[i] + self.items[i]) // self.div_by
            elif operator=="*":
                def f(self, i): self.items[i] = (self.items[i] * self.items[i]) // self.div_by
        else:
            if operator=="+":
                def f(self, i): self.items[i] = (self.items[i] + int(val)) // self.div_by
            elif operator=="*":
                def f(self, i): self.items[i] = (self.items[i] * int(val)) // self.div_by
        
        return f

    # Inspect an item: Update the worry levels then return where to throw the item
    def inspect_item(self, i):
        self.update_item(self, i)
        #self.keep_item_small(i)
        self.inspections += 1

        if self.items[i]%self.rule[0]==0: return self.rule[1]
        else: return self.rule[2]

    # Replaces the item (worry level) by the smallest value with same modulo behavior
    def keep_item_small(self, i):
        if self.items[i] > self.worry_cap:
            target = self.getModuloProfile(self.items[i])
            self.items[i] = 1
            while self.getModuloProfile(self.items[i]) != target:
                self.items[i] += 1

    # Returns dictionary with modulo results from 2-9 of given number
    def getModuloProfile(self, number):
        res = {}
        for i in range(2,10):
            res[i]=number%i

        return res