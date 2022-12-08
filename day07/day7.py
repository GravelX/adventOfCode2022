import os

# ==========================================
# Puzzle description:
# https://adventofcode.com/2022/day/7
# ==========================================

# ------------------------------------------
# Params
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),file_name)
data = [d.replace("\n","") for d in open(file_path, "r").readlines()]
max_disk_space = 70000000
update_size = 30000000

# ------------------------------------------
# Directory class
# contents: contains ints (file sizes) and other dir
# name: name of the directory
class Directory:
    def __init__(self, name):
        self.name = name
        self.contents = []

    # Recursively computes the size of the folder
    def size(self):
        size = 0
        for item in self.contents:
            if type(item) is Directory:
                size += item.size()
            elif type(item) is File:
                size += item.size
            else:
                raise Exception("Unrecognized item in directory!")
        return size
    
    # Sums all folders within that are 100'000 or less in size
    def sumAllSmallFoldersWithin(self):
        size = 0
        for item in self.contents:
            if type(item) is Directory:
                sub_folder_size = item.size()
                if sub_folder_size <= 100000:
                    size += sub_folder_size
                size += item.sumAllSmallFoldersWithin()

        return size

    # Returns lower level directory if it exists
    def cd(self, dir_name):
        dir = None
        for item in self.contents:
            if (type(item) is Directory) and (item.name == dir_name):
                dir = item
                break
        if dir is None: raise Exception("Could not navigate to that directory (name \""+dir_name+"\"not found).")
        return dir

    # Add item to directory content
    def contains(self, item):
        self.contents.append(item)

    # Graphically displays contents of the dir
    def printContents(self, level=1):
        prefix = ""
        if level > 1:
            for i in range(level-1):
                prefix += "|  "
        if level > 0: prefix += "+--"
        if self.name =="/":
            print(prefix+"root/")
        else:
            print(prefix+self.name+"/")
        for item in self.contents:
            if type(item) is Directory:
                item.printContents(level+1)
            elif type(item) is File:
                index = prefix.find("+--")
                print(prefix[:index]+"|  "+prefix[index:]+item.name,"(size:",str(item.size)+")")
            else:
                raise Exception("Unrecognized item in directory!")

    # Returns list of sizes that reach minimum theshold
    def getSizesAtLeast(self, min):
        candidates = []

        for item in self.contents:
            if type(item) is Directory:
                folder_size = item.size()
                if folder_size >= min: candidates.append(folder_size)
                candidates += item.getSizesAtLeast(min)

        return candidates

# ------------------------------------------
# File class
class File():
    def __init__(self, size, name):
        self.size = size
        self.name = name

# ------------------------------------------
# Generates the filesystem tree from the input
def getFileSystemTree():
    current_location = []
    fileTree = Directory("Device")
    fileTreeBrowser = fileTree

    for line in data:
        args = line.split(" ")
        if line[0]=="$":
            # Command reached
            if args[1] == "cd" and args[2] == "..":
                # Go back one
                current_location.pop()
                fileTreeBrowser = findParent(current_location, fileTree)
            elif args[1] == "cd":
                # Go deeper
                fileTreeBrowser.contains(Directory(args[2]))
                fileTreeBrowser = fileTreeBrowser.cd(args[2])
                current_location.append(args[2])
            elif args[1] != "ls":
                raise Exception("Unrecognized command!")
        else:
            # Listing items
            if args[0] == "dir":
                # Encountered a directory
                fileTreeBrowser.contains(Directory(args[1]))
            else:
                # Encountered a file
                fileTreeBrowser.contains(File(int(args[0]), args[1]))

    return fileTree

# ------------------------------------------
# Returns the directory object at a given path in the file system
def findParent(path, fileTree):
    parent = fileTree
    for level in path:
        parent = parent.cd(level)
    return parent

# ------------------------------------------
# Returns the size of the smallest directory we can delete to install the update
def freeDiskSpace(fileSystem):
    free_space = max_disk_space - fileSystem.size()
    need_to_free = update_size - free_space

    candidates = fileSystem.getSizesAtLeast(need_to_free)
    candidates.sort()
    winner = candidates[0]

    print("To install the update, delete the folder with the size:", winner)

# ------------------------------------------
# Main
def main():
    # Load input
    fileTree = getFileSystemTree()
    print("FULL FILE SYSTEM:")
    fileTree.printContents()
    print("\n")

    # Part 1
    print("The sum of the total sizes of directories with a total size of at most 100000:",fileTree.sumAllSmallFoldersWithin())
    # Part 2
    freeDiskSpace(fileTree) 

if __name__ == "__main__":
    main()