global arrayData
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(target):
    global arrayData
    found = False
    index = 0
    while found == False and index < len(arrayData):
        if arrayData[index] == target:
            found = True
        else:
            index += 1
    return found

def bubbleSort():
    global arrayData
    temp = 0
    for x in range(len(arrayData)):
        for y in range(len(arrayData) - x - 1):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp


# main
usrInput = int(input("enter an integer value to search in the array: "))
found = linearSearch(usrInput)

if found:
    print("The value was found")
else:
    print("The value was not found")

bubbleSort()
print(arrayData)