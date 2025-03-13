class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

linkedList = [node(1, 1),
              node(5, 4),
              node(6, 7),
              node(7, -1),
              node(2, 2),
              node(0, 6),
              node(0, 8),
              node(56, 3),
              node(0, 9),
              node(0, -1)]

startPointer = 0
emptyList = 5

def outputNodes(arr, startPointer):
    index = startPointer
    while index != -1:
        print(arr[index].data, end=' ')
        index = arr[index].nextNode
    print()

def addNode(arr, startPointer, emptyList):
    dataToBeAdded = int(input("Enter the data item you want to add to the linked list: "))
    if emptyList == -1:
        return startPointer, emptyList, False
    
    newNodeIndex = emptyList
    emptyList = arr[emptyList].nextNode

    index = startPointer
    if index == -1:
        startPointer = newNodeIndex
    else:
        while arr[index].nextNode != -1:
            index = arr[index].nextNode
        arr[index].nextNode = newNodeIndex
    
    arr[newNodeIndex] = node(dataToBeAdded, -1)
    return startPointer, emptyList, True

outputNodes(linkedList, startPointer)
startPointer, emptyList, status = addNode(linkedList, startPointer, emptyList)
if status:
    print("Data item added to the linked list successfully")
else:
    print("Data item was not added to the linked list")
outputNodes(linkedList, startPointer)
