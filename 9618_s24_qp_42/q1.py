WordArray = []
def Play():
    missedAnswers = []
    correct = 0
    global numberOfAnswers
    print(f"The main word is: {WordArray[0]} and the number of answers is {numberOfAnswers}")
    usrInput = input("Enter the answer, or type 'no' to exit: ")

    if usrInput.lower() == "no":
        # return
        percentageCorrect = (count / (len(WordArray) - 1)) * 100
        for element in WordArray[1:]:
            if element == None:
                continue
            else:
                missedAnswers.append(element)
        print(f"You got {round(percentageCorrect)}% answers correct!")
        print(f"You missed {missedAnswers}")

    else:
        if usrInput.lower() in WordArray[1:]:
            print("That is the correct answer!")
            correct += 1
            index = WordArray.index(usrInput)
            WordArray[index] = None
        else:
            print("This is not an answer")

def ReadWords(fileName):
    numberOfAnswers = 0
    with open(fileName, "r") as file:
        for element in file:
            WordArray.append(element.strip())    
    numberOfAnswers = len(WordArray) - 1
    Play()


# main
difficulty = input("Enter  the difficulty (easy, medium, or hard): ")
match difficulty.lower():
    case "easy":
        ReadWords("source/Easy.txt")
    case "medium":
        ReadWords("source/Medium.txt")
    case "hard":
        ReadWords("source/Hard.txt")