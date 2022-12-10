import os

# ==========================================
# Puzzle description:
# https://adventofcode.com/2022/day/10
# ==========================================

# ------------------------------------------
# Params
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
data = [d.strip() for d in open(file_path, "r").readlines()]

# ------------------------------------------
# CPU class holds register, tickcount and signal strength
class CPU():
    def __init__(self, crt):
        self.X = 1
        self.sig_strength_sum = 0
        self.cycle = 0
        self.crt = crt

    def tick(self):
        self.cycle += 1
        self.logSignalStrength()
        self.crt.draw(self.X)

    def execute(self, instruction, val=None):
        if instruction == "noop":
            self.tick()
        elif instruction == "addx":
            if type(val) is not int: raise Exception("addx instruction wasn't given a proper value:",val)
            self.tick()
            self.tick()
            self.X += val

    def logSignalStrength(self):
        # Increment the sum of signal strengths at the 20th cycle, then every 40 cycles
        if (self.cycle-20)%40 == 0: self.sig_strength_sum += (self.cycle * self.X)

# ------------------------------------------
# CRT class responsible to display screen
class CRT():
    def __init__(self):
        self.cycle = 0

    def draw(self, sprite_position):
        rel_pos = (self.cycle+1)%40
        # Draw sprite
        if sprite_position <= rel_pos <= sprite_position+2: print("#",end="")
        else: print(".",end="")
        # Change line
        if rel_pos==0 and self.cycle!=0: print()
        self.cycle += 1

# ------------------------------------------
# Feed the input instructions to a cpu object
def feedCPU(cpu):
    for instruction in data:
        args = instruction.split(" ")
        cpu.execute(args[0],int(args[1])) if len(args)>1 else cpu.execute(args[0])

# ------------------------------------------
# Main
def main():
    crt = CRT()
    cpu = CPU(crt)
    feedCPU(cpu) # Part 2
    # Part 1
    print("The sum of the signal strengths is",cpu.sig_strength_sum,end=".\n")

if __name__ == "__main__":
    main()