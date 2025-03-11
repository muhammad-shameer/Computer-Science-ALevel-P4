global playerScores
playerScores = [['', 0] for i in range(11)]

def ReadHighScores():
    global playerScores
    with open('HighScore.txt', 'rt') as file:
        for i in range(10):
            line1 = file.readline().strip()
            line2 = file.readline().strip()

            playerScores[i][0] = line1
            playerScores[i][1] = int(line2)

def OutputHighScores():
    global playerScores
    for i in range(10):
        print(f"{playerScores[i][0]} {playerScores[i][1]}")

def NewPlayerInfo(playerName, playerScore):
    global playerScores
    playerList = [playerName, playerScore]
    if playerList > min(playerScores, key=lambda x: x[1]):
        newList = True
    if newList:
        playerScores.append(playerList)
        playerScores.sort(key=lambda x: x[1], reverse=True)
        playerScores = playerScores[:10]
    
def WriteTopTen():
    global playerScores
    with open('NewHighScore.txt', 'w') as file:
        for i in range(10):
            file.write(f"{playerScores[i][0]} {playerScores[i][1]}\n")

# main program
ReadHighScores()
OutputHighScores()

usrPlayerName = input("Enter a 3 letter player name: ")
while len(usrPlayerName) > 3:
    usrPlayerName = input("Enter a 3 letter player name: ")

usrPlayerScore = int(input("Enter a score between 1 and 100000 inclusive: "))
while usrPlayerScore > 100_000 or usrPlayerScore < 1:
    usrPlayerScore = int(input("Enter a score between 1 and 100000 inclusive: "))

NewPlayerInfo(usrPlayerName, usrPlayerScore)

OutputHighScores()
WriteTopTen()