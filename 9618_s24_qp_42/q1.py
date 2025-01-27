WordArray = [] # global array of string


def Play():
    correctAnswer = 0
    print(f"The main word is: {WordArray[0]} and the number of answers are {len(WordArray) - 1}")
    while True:
        usr_input = input("Enter a word that can be made from the main word, or enter 'no' to stop playing: ")
        missedAnswers = [] # contains the list of answers the user missed
        if usr_input.lower() == 'no':
            # percentage of answers correct
            percentageCorrect = (correctAnswer / (len(WordArray) - 1)) * 100    # correct / total * 100
            # The answers user did not enter
            for element in WordArray[1:]:
                if element == None:
                    continue
                else:
                    missedAnswers.append(element)
            print(f"You got {round(percentageCorrect, 2)}% answers correct")
            print(f"You missed {missedAnswers}")
            break
        else:
            if usr_input.lower() in WordArray[1:]:
                print("This is a correct answer!")
                correctAnswer += 1
                index = WordArray.index(usr_input) # gets the index of the word the user entered
                WordArray[index] = None
            else:
                print("This is not an answer")


def ReadWords(fileName):
    answers = 0
    with open(fileName, 'r') as file:
        for element in file:
            WordArray.append(element.strip())
            answers += 1
    answers -= 1 # every element except the first element
    Play()


def main():
    usr_input = input("Enter 'easy', 'medium', or 'hard': ")

    match usr_input:
        case 'easy':
            ReadWords("source/Easy.txt")
        case 'medium':
            ReadWords("source/Medium.txt")
        case 'hard':
            ReadWords("source/Hard.txt")


if __name__ == "__main__":
    main()