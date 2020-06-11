# *************************************************
#                 Word Search.py
#
# Description:  A program that generates word
#               searches.
# 
# Requirements: numpy and tkinter installed
#
# Dependencies: words.txt
#
# Execution:    python 'Word Search.py'
# 
# Author: Teddy Potter
# *************************************************

import random
import numpy as np
from tkinter import *

# Variables for dimensions of board and number of words to find; can be adjusted
size = 17   
numberOfWords = 25

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
           "Y", "Z"]
text_file = open("words.txt", "r")
words = text_file.read().splitlines()   # read in all the words from the dictionary

root = Tk()

# Checks to see if the word fits on the board
def checkWord(word, locX, locY, d, a):
    print("Checking " + word)
    for i in range(0, len(word)):
##        spot = Label(canvas, text = a[locX][locY], font=("Arial", 24), width = 2, bg = "green")
##        spot.grid(row = locX, column = locY)

        if d == 0 and (a[locX][locY + i] == "-" or a[locX][locY + i] == word[i:i+1]) and locY + len(word) < size:
            spot = Label(canvas, text = word[i:i+1], font=("Arial", 24), width = 2, bg = "green")
            spot.grid(row = locX, column = locY)
            continue

        elif d == 1 and (a[locX + i][locY] == "-" or a[locX + i][locY] == word[i:i+1]) and locX + len(word) < size:
            spot = Label(canvas, text = word[i:i+1], font=("Arial", 24), width = 2, bg = "green")
            spot.grid(row = locX, column = locY)
            continue

        elif d == 2 and (a[locX][locY - i] == "-" or a[locX][locY - i] == word[i:i+1]) and locY - len(word) > 0:
            spot = Label(canvas, text = word[i:i+1], font=("Arial", 24), width = 2, bg = "green")
            spot.grid(row = locX, column = locY)
            continue

        elif d == 3 and (a[locX - i][locY] == "-" or a[locX - i][locY] == word[i:i+1]) and locX - len(word) > 0:
            spot = Label(canvas, text = word[i:i+1], font=("Arial", 24), width = 2, bg = "green")
            spot.grid(row = locX, column = locY)
            continue

        elif d == 4 and (a[locX - i][locY + i] == "-" or a[locX - i][locY + i] == word[i:i+1]) and locX - len(word) > 0 and locY + len(word) < size:
            spot = Label(canvas, text = word[i:i+1], font=("Arial", 24), width = 2, bg = "green")
            spot.grid(row = locX, column = locY)
            continue

        elif d == 5 and (a[locX + i][locY + i] == "-" or a[locX + i][locY + i] == word[i:i+1]) and locX + len(word) < size and locY + len(word) < size:
            spot = Label(canvas, text = word[i:i+1], font=("Arial", 24), width = 2, bg = "green")
            spot.grid(row = locX, column = locY)
            continue

        elif d == 6 and (a[locX - i][locY - i] == "-" or a[locX - i][locY - i] == word[i:i+1]) and locX - len(word) > 0 and locY - len(word) > 0:
            spot = Label(canvas, text = word[i:i+1], font=("Arial", 24), width = 2, bg = "green")
            spot.grid(row = locX, column = locY)
            continue

        elif d == 7 and (a[locX + i][locY - i] == "-" or a[locX + i][locY - i] == word[i:i+1]) and locX + len(word) < size and locY - len(word) > 0:
            spot = Label(canvas, text = word[i:i+1], font=("Arial", 24), width = 2, bg = "green")
            spot.grid(row = locX, column = locY)
            continue

        else:
            return False

    return True

# Puts the word into the array 'a'
def fillWord(word, locX, locY, d, a):
    for i in range(0, len(word)):
        if d == 0:
            a[locX][locY + i] = word[i:i+1]
            spot = Label(canvas, text = a[locX][locY + i], font=("Arial", 24), width = 2, bg = "blue")
            spot.grid(row = locX, column = locY)

        elif d == 1:
            a[locX + i][locY] = word[i:i+1]
            spot = Label(canvas, text = a[locX + i][locY], font=("Arial", 24), width = 2, bg = "blue")
            spot.grid(row = locX, column = locY)

        elif d == 2:
            a[locX][locY - i] = word[i:i+1]
            spot = Label(canvas, text = a[locX][locY - i], font=("Arial", 24), width = 2, bg = "blue")
            spot.grid(row = locX, column = locY)

        elif d == 3:
            a[locX - i][locY] = word[i:i+1]
            spot = Label(canvas, text = a[locX - i][locY], font=("Arial", 24), width = 2, bg = "blue")
            spot.grid(row = locX, column = locY)

        elif d == 4:
            a[locX - i][locY + i] = word[i:i+1]
            spot = Label(canvas, text = a[locX - i][locY + i], font=("Arial", 24), width = 2, bg = "blue")
            spot.grid(row = locX, column = locY)

        elif d == 5:
            a[locX + i][locY + i] = word[i:i+1]
            spot = Label(canvas, text = a[locX + i][locY + i], font=("Arial", 24), width = 2, bg = "blue")
            spot.grid(row = locX, column = locY)

        elif d == 6:
            a[locX - i][locY - i] = word[i:i+1]
            spot = Label(canvas, text = a[locX - i][locY - i], font=("Arial", 24), width = 2, bg = "blue")
            spot.grid(row = locX, column = locY)

        elif d == 7:
            a[locX + i][locY - i] = word[i:i+1]
            spot = Label(canvas, text = a[locX + i][locY - i], font=("Arial", 24), width = 2, bg = "green")
            spot.grid(row = locX, column = locY)

    return a

# Recursive function that will test random
# words with random locations and directions
# until it finds one that fits
# then it puts the word into the array
def addWord(word, x, y, d, a):
    if checkWord(word, x, y, d, a):
        print(word)
        return fillWord(word, x, y, d, a)

    else:
        return addWord(random.choice(words), random.randint(0, size - 1), random.randint(0, size - 1), random.randint(0, 7), a)

# --- Main code starts here --- #

# Just a blank canvas to put the board on
canvas = Canvas(root)
canvas.pack(side = BOTTOM)

# Uses an empty numpy array of strings that will act as the board
a = np.zeros([size,size], dtype = np.str)

# Fills the array with -'s as placeholders for non-words
for row in range(0, size):
    for col in range(0, size):
        a[row][col] = "-"

# Generates all the words you want on the board
for n in range(0, numberOfWords):
    word = random.choice(words)
    locX = random.randint(0, size - 1)
    locY = random.randint(0, size - 1)
    direction = random.randint(0, 7)
    addWord(word, locX, locY, direction, a)

print(a)

# Takes the numpy array and puts it into a grid of labels, with the words highlighted
##for row in range(0, size):
##    for col in range(0, size):
##        if a[row][col] == "-":
##            a[row][col] = random.choice(letters)
##            spot = Label(canvas, text = a[row][col], font=("Arial", 24), width = 2, bg = "white")
##        else:
##            spot = Label(canvas, text = a[row][col], font=("Arial", 24), width = 2, bg = "pink")
##            
##        spot.grid(row = row, column = col)

root.mainloop()
