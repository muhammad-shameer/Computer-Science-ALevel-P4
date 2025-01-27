NumberArray = [100, 85, 644, 22, 15, 8, 1]

def RecursiveInsertion(IntegerArray: list[int], NumberElements: int) -> list[int]:
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem -= 1
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

sortedArray = RecursiveInsertion(NumberArray, 7)
print("Recursive")
print(sortedArray)