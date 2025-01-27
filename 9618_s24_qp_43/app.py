class Tree:
    def __init__(self, TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen):
        self.__TreeName = TreeName
        self.__HeightGrowth = HeightGrowth
        self.__MaxHeight = MaxHeight
        self.__MaxWidth = MaxWidth
        self.__Evergreen = Evergreen

    def GetTreeName(self):
        return self.__TreeName

    def GetGrowth(self):
        return self.__HeightGrowth
    
    def GetMaxHeight(self):
        return self.__MaxHeight

    def GetMaxWidth(self):
        return self.__MaxWidth
    
    def GetEvergreen(self):
        return self.__Evergreen

def ReadData():
    NewTree = []
    try:
        with open('source/Trees.txt', 'rt') as file:
            lines = file.readlines()
            for line in lines:
                name = line.split(',')[0]
                growth = line.split(',')[1]
                maxHeight = line.split(',')[2]
                maxWidth = line.split(',')[3]
                evergreen = line.split(',')[4]

                NewTree.append(Tree(name, int(growth), int(maxHeight), int(maxWidth), evergreen))
    except FileNotFoundError:
        print("File was not found!")

    return NewTree

def PrintTrees(TreeObj):
    name = TreeObj.GetTreeName()
    growth = TreeObj.GetGrowth()
    maxHeight = TreeObj.GetMaxHeight()
    maxWidth = TreeObj.GetMaxWidth()
    evergreen = TreeObj.GetEvergreen()

    if evergreen == "Yes":
        print(f"{name} has a maximum height {maxHeight} a maximum width {maxWidth} and grows {growth} cm a year. It does not lose trees")
    
    else:
        print(f"{name} has a maximum height {maxHeight} a maximum width {maxWidth} and grows {growth} cm a year. It loses its leaves each year")

def ChooseTree(Tree):
    matchedTrees = []
    maxHeight = int(input("Enter the max height for the tree: "))
    maxWidth = int(input("Enter the max width for the tree: "))
    evergreen = input("Enter if you would like your tree to be evergreen or not (Yes/No): ")

    for tree in Tree:
        if (tree.GetMaxHeight() <= maxHeight) and 
            tree.GetMaxWidth() <= maxWidth and
            evergreen == tree.GetEvergreen():
            matchedTrees.append(tree)

    
    if not matchedTrees:
        print("No matches found")
    
    PrintTrees(matchedTrees)

    chosenTreeName = input("Enter the tree you would like to choose: ")
    chosenTree = next((tree for tree in matchedTrees if tree.GetTreeName == chosenTreeName), None)

    if chosenTree is None:
        print("Invalid Tree Selection")
    
    treeHeight = int(input("Enter the current height of the tree: "))
    timeToMaxHeight = (chosenTree.GetMaxHeight() - treeHeight) / chosenTree.GetGrowth()

def main():
    treeArray = ReadData()
    PrintTrees(treeArray[0])
    ChooseTree(treeArray)

if __name__ == "__main__":
    main()
