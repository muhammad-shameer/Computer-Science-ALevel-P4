class Picture:
    def __init__(self, description, width, height, frameColour):
        self.__description = description
        self.__width = width
        self.__height = height
        self.__frameColour = frameColour
    
    def GetDescription(self):
        return self.__description
    
    def GetWidth(self):
        return self.__width
    
    def GetHeight(self):
        return self.__height
    
    def GetColour(self):
        return self.__frameColour
    
    def SetDescription(self, newDescription):
        self.__description = newDescription

global pictureElements
pictureElements = [] # 100 elements of type Picture

def readData():
    global pictureElements
    try:
        with open("Pictures.txt", "r") as file:
            lines = file.readlines()
            for i in range(len(lines), 4):
                description = lines[i].strip()
                width = int(lines[i + 1].strip())
                height = int(lines[i + 2].strip())
                colour = lines[i + 3].strip()
                pictureElements.append(Picutre(description, width, height, colour))

    except FileNotFoundError:
        print("file was not found")
    
    numberOfPictures = len(pictureElements)
    return numberOfPictures

# main
readData()