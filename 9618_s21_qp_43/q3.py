# start time: 10:30

class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points

    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, usrAnswer):
        return True if usrAnswer == self.__answer else False
    
    def getPoints(self, numberOfAttempts):
        match numberOfAttempts:
            case 1:
                return self.__points
            case 2:
                return self.__points // 2
            case 3 | 4:
                return self.__points // 4
            case _:
                return 0

def readData():
    global arrayTreasure
    arrayTreasure = [["", "", 0] for i in range(5)]
    try:
        with open("TreasureChestData.txt", "r") as file:
            for i in range(5):
                question = file.readline().strip()
                answer = file.readline().strip()
                points = file.readline().strip()
                arrayTreasure[i] = TreasureChest(question, answer, points)
    except FileNotFoundError:
        print(f"{file} not found")

# main
readData()
# print(arrayTreasure)
numberOfAttempts = 1
questionNumber = int(input("Enter a question number between 1 and 5: "))

while questionNumber > 5 or questionNumber < 1:
    questionNumber = int(input("You entered a wrong choice, enter again: "))
questionDisplay = arrayTreasure[questionNumber - 1]
print(questionDisplay.getQuestion())

usrAnswer = input("Enter the answer: ")
questionDisplay.checkAnswer(usrAnswer)
while not questionDisplay.checkAnswer(usrAnswer):
    usrAnswer = input("Wrong Answer, try again: ")
    numberOfAttempts += 1
numberOfPoints = questionDisplay.getPoints(numberOfAttempts)
print(f"Number of Points received: {numberOfPoints}")

# End Time 11:00