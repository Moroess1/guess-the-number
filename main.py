import eel
import random

eel.init('ui')

currentNumber = None
min = 1
max = 100


@eel.expose
def startGame(minValue, maxValue):
    global min, max, currentNumber
    min = int(minValue)
    max = int(maxValue)
    currentNumber = random.randint(min, max)
    print(currentNumber)

@eel.expose
def restartGame():
    global min, max, currentNumber
    currentNumber = random.randint(min, max)
    print(currentNumber)

@eel.expose
def checkGuess(guess):
    global currentNumber
    guess = int(guess)
    if (guess < currentNumber):
        return ">"
    elif (guess > currentNumber):
        return "<"
    else:
        return "="


eel.start('mode/index.html', size=(960, 640), position=(500, 200), mode="edge")