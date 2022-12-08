import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''

class FileObj:
      
    def __init__(self, name, filesize, type):
        self.name = name
        self.filesize = filesize
        self.type = type
        self.children = []
        self.parent = None
    
    def __str__(self):

        for child in self.children:
            print(child)

        tabs = ""
        for deapth in range(0, findRootDepth(self)):
            tabs += "\t"

        return f"{tabs} [{self.type}] {self.name} ({self.filesize}) " #{[print(child) for child in self.children]}

    def addFile(self, f):
        
        self.children.append(f)

        f.parent = self

        self.calculateParentsFilesize(f);

        return f

    def calculateParentsFilesize(self, f):
        parent = f.parent;
        if (parent == None):
            return;

        parent.filesize = 0

        for child in parent.children:
            parent.filesize += child.filesize

        return self.calculateParentsFilesize(parent)       

    
def parse_input(s):
    return [x.strip().split("\n") for x in s.strip().split("$ ")]


root = FileObj("/", 0, "d");
cwd = root;

def addFilesToCurrentDir(cwd, files):

    #print(files)

    for file in files:
        fileData = file.split(" ")
        typeOrSize = fileData[0]
        name = fileData[1]
        if(typeOrSize == "dir"):
            cwd.addFile(FileObj(name, 0, "d"))
        else:
            cwd.addFile(FileObj(name, int(typeOrSize), "f"))

    return cwd

def findRoot(f):
    if (f.parent == None):
        return f
    
    return findRoot(f.parent)


def findRootDepth(f, c=0):
    if (f.parent == None):
        return c
        
    return findRootDepth(f.parent, c+1)


def findChild(f, fileName, type):
    for file in f.children:
        if (file.type == type and file.name == fileName):
            return file

def processCmd(commandData, ret, cwd):
    commandArgs = commandData.split(" ")
    command = commandArgs[0]
    args = commandArgs[1:]
    
    #print(commandArgs)
    #print(command)
    #print(args, "\n")
    
    if (command == "cd"):
        if (args[0] == "/"):
            return findRoot(cwd)
        elif (args[0] == ".."): 
            return cwd.parent
        else: 
            return findChild(cwd, args[0], "d")

    elif (command == "ls"):
        return addFilesToCurrentDir(cwd, ret)
    
    return cwd

def processInput(data, cwd):

    for cmd in data:
        commandData = cmd[0]
        if(commandData != ""):
            ret = cmd[1:]
            cwd = processCmd(commandData, ret, cwd)
            
    return ""


def calc(cwd):

    total = 0
        
    for file in cwd.children:
        if (file.type == "d"):
            if (file.filesize <= 100000):
                #print(file.name, file.filesize)
                total += file.filesize;

            total += calc(file)
    return total

def calc2(cwd, space_needed ):

    closest = 999999999
    
    for file in cwd.children:
        if (file.type == "d"):
            if (file.filesize >= space_needed):
                closest = min(file.filesize, closest)
                closest = min(closest, calc2(file, space_needed))
                
    return closest


def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_DATA) #INPUT_TEST_DATA
    processInput(data, cwd)
        
    print(root)

    space_needed = 30000000 - (70000000 - root.filesize)

    print("Space needed:", space_needed)

    print(calc2(root, space_needed))

    return 0

if __name__ == "__main__":
    main()