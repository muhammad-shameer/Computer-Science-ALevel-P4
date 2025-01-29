class Tree:
    '''
    PRIVATE TreeName: STRING
    PRIVATE HeightGrowth: INTEGER
    PRIVATE MaxHeight: INTEGER
    PRIVATE MaxWidth: INTEGER
    PRIVATE Evergreen: STRING
    '''
    def __init__(self, TN, HG, MH, MW, EG):
        self.__TreeName = TN
        self.__HeightGrowth = HG
        self.__MaxHeight = MH
        self.__MaxWidth = MW
        self.__Evergreen = EG

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
    TreeData = [] # type Tree
    # Exception Handling
    try:
        # opening and reading the Trees.txt file
        with open('9618_s24_qp_43\source\Trees.txt', 'rt') as file:
            lines = file.readlines()
            for line in lines:
                name = line.split(',')[0]
                growth = line.split(',')[1]
                max_height = line.split(',')[2]
                max_width = line.split(',')[3]
                evergreen = line.split(',')[4].strip()
                TreeData.append(Tree(name, int(growth), int(max_height), int(max_width), evergreen))
    except FileNotFoundError:
        print("The file was not found")
    # returns the list
    return TreeData

def PrintTrees(TreeObj): # takes a single tree object as parameter
    name = TreeObj.GetTreeName()
    growth = TreeObj.GetGrowth()
    max_height = TreeObj.GetMaxHeight()
    max_width = TreeObj.GetMaxWidth()
    evergreen = TreeObj.GetEvergreen()

    if evergreen.strip() == "Yes":
        print(f"{name} has a maximum height {max_height} a maximum width {max_width} and grows {growth} cm a year. It does not lose its leaves")
    else:
        print(f"{name} has a maximum height {max_height} a maximum width {max_width} and grows {growth} cm a year. It loses its leaves each year")


def ChooseTree(TreeObjArr): # takes a list of all the tree objects created
    MatchedTrees = [] # all the tree objects that meet the requirement
    
    usr_max_height = int(input("Enter the height you want the tree to be (cm): "))
    usr_max_width = int(input("Enter the max width you want the tree to be (cm): "))
    usr_evergreen = input("Enter if you want the tree to be evergreen or not (Yes/No): ")

    # Check if any tree meets the requirements
    for TreeObj in TreeObjArr:
        max_height = TreeObj.GetMaxHeight()
        max_width = TreeObj.GetMaxWidth()
        evergreen = TreeObj.GetEvergreen()

        if max_height <= usr_max_height:
            if max_width <= usr_max_width:
                if evergreen == usr_evergreen:
                    MatchedTrees.append(TreeObj)
                # endif
            # endif
        # endif
    
    for tree in MatchedTrees:
        PrintTrees(tree)

    usr_tree_choice = input("Enter the tree you would like to choose: ") # TODO: make logic for tree selection for the array

    final_tree = next((tree for tree in MatchedTrees if tree.GetTreeName().lower().strip() == usr_tree_choice.lower().strip()), None)

    if final_tree is not None:
        tree_height = int(input(f"Enter the current height of the tree {final_tree.GetTreeName()} (cm): "))
        time_taken = (final_tree.GetMaxHeight() - tree_height) / final_tree.GetGrowth()
        print(f"It will take {time_taken} years for {final_tree.GetTreeName()} to grow to maximum height")
    else:
        print("The tree you selected is not in the matched trees list.")


def main():
    TreeList = ReadData()
    # PrintTrees(TreeList[0])
    ChooseTree(TreeList)

if __name__ == "__main__":
    main()