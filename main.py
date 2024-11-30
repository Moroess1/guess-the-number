import eel
import random

eel.init('ui')

currentNumber = None
min = 1
max = 100


@eel.expose
def setRange(minValue, maxValue):
    global min, max, currentNumber
    min = int(minValue)
    max = int(maxValue)
    currentNumber = random.randint(min, max)

@eel.expose
def startGame():
    global currentNumber
    currentNumber = random.randint(min, max)
    return f"Число загадано! Угадайте его от {min} до {max}."

@eel.expose
def checkGuess(guess):
    global currentNumber
    guess = int(guess)
    if (guess < currentNumber):
        return "Больше!"
    elif (guess > currentNumber):
        return "Меньше!"
    else:
        return "Вы угадали!"


eel.start('main/index.html', size=(960, 640), position=(500, 200), mode="edge")