QueueArray = ['' for i in range(10)] # declared as string

headPointer = 0 # declared as integer
tailPointer = 0 # declared as integer
numberOfItems = 0   # declared as integer

def Enqueue(QueueArray, headPointer, tailPointer, numberOfItems, dataToAdd):
    if numberOfItems == 10:
        return tailPointer, numberOfItems, False
    
    QueueArray[tailPointer] = dataToAdd
    if tailPointer >= 9:
        tailPointer = 0
    else:
        tailPointer += 1
    
    numberOfItems += 1
    return tailPointer, numberOfItems, True

def Dequeue(QueueArray, headPointer, tailPointer, numberOfItems):
    if numberOfItems == 0:
        return headPointer, numberOfItems, None
    
    removedDataItem = QueueArray[headPointer]
    if headPointer >= 9:
        headPointer = 0
    else:
        headPointer += 1

    numberOfItems -= 1
    return headPointer, numberOfItems, removedDataItem


# main program
for i in range (11):
    dataItem = input("Enter the data item you want to add: ")
    tailPointer, numberOfItems, status = Enqueue(QueueArray, headPointer, tailPointer, numberOfItems, dataItem)
    if status:
        print("Data item added successfully")
    else:
        print("Queue is full. Data item was not added")

headPointer, numberOfItems, item = Dequeue(QueueArray, headPointer, tailPointer, numberOfItems)
print(item)
headPointer, numberOfItems, item = Dequeue(QueueArray, headPointer, tailPointer, numberOfItems)
print(item)