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

    def inspect_item(self, i):
        self.update_item(self, i)
        self.inspections += 1

        if self.items[i]%self.rule[0]==0: return self.rule[1]
        else: return self.rule[2]