class Balloon:
    '''
    PRIVATE DefenceItem: STRING
    PRIVATE Coulour: STRING
    PRIVATE Health: INTEGER
    '''
    def __init__(self, DefenceItem, Colour):
        self.__DefenceItem = DefenceItem
        self.__Colour = Colour
        self.__Health = 100

    def GetDefenceItem(self):
        return self.__DefenceItem
    
    def ChangeHealth(self, Change):
        self.__Health += Change

    def CheckHelth(self):
        return True if self.__Health >= 0 else False
    
def Defend(balloonObj):
    opponentStrength = int(input("Enter Opponent Strength: "))
    amendedBalloonObj = balloonObj.ChangeHealth(-opponentStrength)
    print(balloonObj.GetDefenceItem())
    if balloonObj.CheckHelth():
        print("Health Remaining")
    else:
        print("No Health Remaining")

    return amendedBalloonObj

# main
usrDefenceItem = input("Enter a defence item: ")
usrColour = input("Enter a colour: ")

Balloon1 = Balloon(usrDefenceItem, usrColour)
Defend(Balloon1)