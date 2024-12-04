import eel
import random
import tkinter as tk
import socket

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


def getFreePort():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def getScreenSize():
    root = tk.Tk()
    root.withdraw()
    return root.winfo_screenwidth(), root.winfo_screenheight()

screenWidth, screenHeight = getScreenSize()

windowWidth, windowHeight = 960, 640

x = (screenWidth - windowWidth) // 2
y = (screenHeight - windowHeight) // 2
eel.start('mode/index.html', port=getFreePort(), size=(windowWidth, windowHeight), position=(x, y), mode="system")