Animal = [] # 20 Animals
Colour = [] # 10 Colours
global AnimalTopPointer
global ColourTopPointer
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush: str) -> bool:
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer += 1
        return True

def PopAnimal() -> str:
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData


def PushColour(DataToPush: str) -> bool:
    global ColourTopPointer
    if ColourTopPointer == 20:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer += 1
        return True

def PopColour() -> str:
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData

def ReadData():
    # seperate exception handlings for both files to make it clear which file was not found
    try:
        with open('source/AnimalData.txt', 'r') as file:
            for line in file:
                PushAnimal(line.strip())
        with open('source/ColourData.txt', 'r') as file:
            for line in file:
                PushColour(line.strip())                
    except(FileNotFoundError):
        print('file does not exist')

def OutputItem():
    AnimalReturned = PopAnimal()
    ColourReturned = PopColour()

    if ColourReturned == "":
        print("No Colour")
        PushAnimal(AnimalReturned)
    elif AnimalReturned == "":
        print("No Animal")
        PushColour(ColourReturned)
    else:
        print(ColourReturned, AnimalReturned)

def main():
    ReadData()
    OutputItem()
    OutputItem()
    OutputItem()
    OutputItem()

if __name__ == "__main__":
    main()