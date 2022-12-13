import os

# Copy pasting shit is part of every programmers day to day life.
# Fuck coding dijkstra manually son this shit aint worth it.
# I cheaped out for day 12, lord forgive me.

file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)

grid = { (x,y): c for y, line in enumerate(open(file_path).readlines()) 
               for x, c in enumerate(line.strip()) }

def adjecents(xy):
    (x, y) = xy
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def is_possible_move(xy, nxy):
    return ord(grid[nxy].replace("E", 'z')) - ord(grid[xy].replace("S", "a")) <= 1 if nxy in grid else False

def possible_adjecents(xy):
    return (nxy for nxy in adjecents(xy) if is_possible_move(xy, nxy))

def flood(dist, layers):
    edge = set(nxy for xy in layers[-1] 
                   for nxy in possible_adjecents(xy) if nxy not in dist)

    dist.update({ xy: len(layers) for xy in edge })

    if edge:    
        flood(dist, layers + [edge])

def distance(start, end):
    dist = { start: 0 }
    flood(dist, [{start}])
    return dist[end] if end in dist else 9999

def find_all(values):
    return (xy for (xy, v) in grid.items() if v in values)

def find(value):
    return next(find_all(value))

# ------------------------------------------
# Main
def main():
    print("Part 1:", distance(find("S"), find("E")))
    print("Part 2:", min(distance(start, find("E")) for start in find_all(['a', 'S'])))

if __name__ == "__main__":
    main()