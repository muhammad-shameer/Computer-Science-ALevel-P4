class Node:
    '''
    PUBLIC Data : INTEGER
    PUBLIC LeftPointer: INTEGER
    PUBLIC RightPointer: INTEGER
    '''
    def __init__(self, Data):
        self.__Data = Data
        self.__LeftPointer = -1
        self.__RightPointer = -1
    
    def GetLeft(self):
        return self.__LeftPointer
    
    def GetRight(self):
        return self.__RightPointer
    
    def GetData(self):
        return self.__Data

    def SetLeft(self, LP):
        self.__LeftPointer = LP
    
    def SetRight(self, RP):
        self.__RightPointer = RP
    
    def SetData(self, DT):
        self.__Data = DT

class TreeClass:
    def __init__(self):
        self.__FirstNode = -1
        self.__NumberNodes = 0
        self.__Tree = [] # 20 elements of type Node
        for _ in range(20):
            self.__Tree.append(Node(-1))

    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__FirstNode = 0
            self.__NumberNodes += 1
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            NodeAccess = self.__FirstNode
            direction = ""
            while NodeAccess != -1:
                previous = NodeAccess
                if NewNode.GetData() < self.__Tree[NodeAccess].GetData():
                    NodeAccess = self.__Tree[NodeAccess].GetLeft()
                    direction = "left"
                elif NewNode.GetData() > self.__Tree[NodeAccess].GetData():
                    NodeAccess = self.__Tree[NodeAccess].GetRight()
                    direction = "right"

            if direction == "left":
                self.__Tree[previous].SetLeft(self.__NumberNodes)
            else:
                self.__Tree[previous].SetRight(self.__NumberNodes)
        self.__NumberNodes += 1

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No Nodes")
        else:
            for i in range(0, self.__NumberNodes):
                print(f"{self.__Tree[i].GetLeft()} {self.__Tree[i].GetData()} {self.__Tree[i].GetRight()}")


TheTree = TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()