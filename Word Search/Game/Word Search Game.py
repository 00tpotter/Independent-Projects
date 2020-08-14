# *************************************************
#                 Word Search Game.py
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
# Author:       Teddy Potter
# *************************************************

import random
import numpy as np
import pygame
import copy
import sys

# Variables for dimensions of board and number of words to find; can be adjusted
size = 17
numberOfWords = 25

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
           "Y", "Z"]
text_file = open("words.txt", "r")
words = text_file.read().splitlines()   # read in all the words from the dictionary

score_file = open("high_score.txt", "r")
score = score_file.read().splitlines()   # read in the best time/high score
score_file.close()
print(score)

used_words = []

# Checks to see if the word fits on the board
def checkWord(word, locX, locY, d, a):
    if word in used_words:
        return False

    for i in range(0, len(word)):
        if d == 0 and (a[locX][locY + i] == "-" or a[locX][locY + i] == word[i:i+1]) and locY + len(word) < size:
            continue

        elif d == 1 and (a[locX + i][locY] == "-" or a[locX + i][locY] == word[i:i+1]) and locX + len(word) < size:
            continue

        elif d == 2 and (a[locX][locY - i] == "-" or a[locX][locY - i] == word[i:i+1]) and locY - len(word) > 0:
            continue

        elif d == 3 and (a[locX - i][locY] == "-" or a[locX - i][locY] == word[i:i+1]) and locX - len(word) > 0:
            continue

        elif d == 4 and (a[locX - i][locY + i] == "-" or a[locX - i][locY + i] == word[i:i+1]) and locX - len(word) > 0 and locY + len(word) < size:
            continue

        elif d == 5 and (a[locX + i][locY + i] == "-" or a[locX + i][locY + i] == word[i:i+1]) and locX + len(word) < size and locY + len(word) < size:
            continue

        elif d == 6 and (a[locX - i][locY - i] == "-" or a[locX - i][locY - i] == word[i:i+1]) and locX - len(word) > 0 and locY - len(word) > 0:
            continue

        elif d == 7 and (a[locX + i][locY - i] == "-" or a[locX + i][locY - i] == word[i:i+1]) and locX + len(word) < size and locY - len(word) > 0:
            continue

        else:
            return False

    return True

# Puts the word into the array 'a'
def fillWord(word, locX, locY, d, a):
    for i in range(0, len(word)):
        if d == 0:
            a[locX][locY + i] = word[i:i+1]

        elif d == 1:
            a[locX + i][locY] = word[i:i+1]

        elif d == 2:
            a[locX][locY - i] = word[i:i+1]

        elif d == 3:
            a[locX - i][locY] = word[i:i+1]

        elif d == 4:
            a[locX - i][locY + i] = word[i:i+1]

        elif d == 5:
            a[locX + i][locY + i] = word[i:i+1]

        elif d == 6:
            a[locX - i][locY - i] = word[i:i+1]

        elif d == 7:
            a[locX + i][locY - i] = word[i:i+1]

    return a

# Recursive function that will test random
# words with random locations and directions
# until it finds one that fits
# then it puts the word into the array
def addWord(word, x, y, d, a):
    if checkWord(word, x, y, d, a):
        print(word)
        used_words.append(word)
        return fillWord(word, x, y, d, a)

    else:
        return addWord(random.choice(words), random.randint(0, size - 1), random.randint(0, size - 1), random.randint(0, 7), a)

def generateGame():
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

    return a

def checkSelection(sel):
    sel.sort()
    temp = ""
    tempBack = ""

    for i in sel:
        row = i[1]
        col = i[0]
        if b[row][col] == "-":
            return False

        temp += (b[row][col])
        print("temp: " + temp)

    for x in range(0, len(temp)):
        tempBack += temp[len(temp)-x-1]
    print("tempBack: " + tempBack)

    if temp in used_words:
        return temp
    elif tempBack in used_words:
        return tempBack
    else:
        return ""

def clearSelection(sel):
    sel.clear()

# Main game board variables
a = generateGame()
print(a)
b = copy.deepcopy(a)

# -------------------- Pygame stuff -------------------- #
pygame.init()
pygame.display.set_caption('Word Search Game')

# Variables for screen and fonts
width = 850
height = 1130

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont("consola", 32)
small_font = pygame.font.SysFont("consola", 28) #pygame.font.Font('C:\WINDOWS\FONTS\CONSOLA.TTF', 28)

# Colors
white = (255, 255, 255)
grey = (200, 200, 200)
dark_grey = (175, 175, 175)
black = (0, 0, 0)

light_red = (255, 175, 175)
dark_red = (230, 150, 150)
light_orange = (255, 200, 145)
light_yellow = (255, 255, 200)
light_green = (200, 255, 200)
light_blue = (200, 200, 255)
dark_blue = (175, 175, 230)
light_purple = (255, 175, 255)
light_pink = (255, 200, 200)
light_brown = (200, 150, 100)

# color_options = [light_red, light_orange, light_yellow, light_green,
#                 light_blue, light_purple, light_pink, light_brown]
# curr_color = random.choice(color_options)

letter_color = white
word_color = white

check_color = grey
clear_color = light_blue
new_color = light_red

# Other miscellaneous variables
selX = -1
selY = -1
selected = []

correct = []
correctLetters = []

running = True
leftDrag = False
rightDrag = False
win = False

frames = 0
minutes = 0
seconds = 0
total_seconds = 0

while running:
    # Variables for calculating time
    if not win:
        total_seconds = frames // 60
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        time = "{0:02}:{1:02}".format(minutes, seconds)

    # Actions/events from input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Events related to left click mouse down
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // 50
            row = (pos[1] - 50) // 50

            # Action for letters being selected
            if (column < size and column >= 0) and (row < size and row >= 0) and not win:
                leftDrag = True

                selX = column
                selY = row
                if (selX, selY) not in selected:
                    selected.append((selX, selY))
                print(b[selY][selX])
                print(selected)
                print("Click ", pos, "Grid coordinates: ", row, column)

            # Action for check word buttton pressed
            if (pos[0] < width // 2 and pos[0] >= 0) and (pos[1] < 40 and pos[1] >= 0) and not win:
                check_color = dark_grey
                if checkSelection(selected):
                    correct.append(checkSelection(selected))
                    for things in selected:
                        correctLetters.append(things)

                clearSelection(selected)
                print("Check word pressed")

            # Action for clear word buttton pressed
            if (pos[0] < width and pos[0] >= width // 2) and (pos[1] < 40 and pos[1] >= 0) and not win:
                clear_color = dark_blue
                clearSelection(selected)
                print("Clear word pressed")

            # Action for new game button; resets all variables, game board, etc.
            if (pos[0] < width // 2 and pos[0] >= 0) and (pos[1] < height and pos[1] >= 1050):
                win = False
                score_file = open("high_score.txt", "r")
                score = score_file.read().splitlines()   # read in the best time/high score
                score_file.close()
                used_words = []
                a = generateGame()
                print(a)
                b = copy.deepcopy(a)
                frames = 0
                minutes = 0
                seconds = 0
                total_seconds = 0
                selected = []
                correct = []
                correctLetters = []
                new_color = dark_red
                
        # Events related to left click mouse up
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            leftDrag = False

        # Events related to mouse drag/motion
        elif event.type == pygame.MOUSEMOTION and leftDrag:
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // 50
            row = (pos[1] - 50) // 50
            if (column, row) not in selected:
                selected.append((column, row))

        # Events related to right click mouse down
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // 50
            row = (pos[1] - 50) // 50

            # Action for letters being selected
            if (column < size and column >= 0) and (row < size and row >= 0):
                rightDrag = True

                selX = column
                selY = row
                if (selX, selY) in selected:
                    selected.remove((selX, selY))
                print(b[selY][selX])
                print(selected)
                print("Click ", pos, "Grid coordinates: ", row, column)
        
        # Events related to right click mouse up
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            rightDrag = False

        # Events related to mouse drag/motion
        elif event.type == pygame.MOUSEMOTION and rightDrag:
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // 50
            row = (pos[1] - 50) // 50
            if (column, row) in selected:
                selected.remove((column, row))

        # Visual change for buttons being clicked
        else:
            check_color = grey
            clear_color = light_blue
            new_color = light_red

    # Displaying everything on the screen
    screen.fill(white)

    # Takes the numpy array and puts it into a grid of labels
    for row in range(0, size):
        for col in range(0, size):
            if (col, row) in selected:
                letter_color = light_yellow
            elif (col, row) in correctLetters:
                letter_color = light_green
            else:
                letter_color = white

            if a[row][col] == "-":
                a[row][col] = random.choice(letters)

            letter = font.render(a[row][col], True, black, letter_color)
            letterRect = letter.get_rect()
            letterRect.center = (col * 50 + 25, row * 50 + 65)
            pygame.draw.rect(screen, letter_color, [50 * col, 50 * row + 40, 50, 50])
            screen.blit(letter, letterRect)

    # Display all the words at the bottom of the screen
    for i in range(0, numberOfWords):
        col = i % 5
        row = i // 5

        if used_words[i] in correct:
            word_color = light_green
        else:
            word_color = white

        word = small_font.render(used_words[i], True, black, word_color)
        wordRect = word.get_rect()
        wordRect.center = (col * 170 + 85, (row * 40 + 20) + 890)
        pygame.draw.rect(screen, word_color, [170 * col, (40 * row) + 890, 170, 40])
        screen.blit(word, wordRect)

    # Check word and clear buttons
    check = font.render("CHECK WORD", True, black, check_color)
    checkRect = check.get_rect()
    checkRect.center = (width // 4, 20)
    pygame.draw.rect(screen, check_color, [0, 0, width // 2, 40])
    screen.blit(check, checkRect)

    clear = font.render("CLEAR", True, black, clear_color)
    clearRect = clear.get_rect()
    clearRect.center = (width - (width // 4), 20)
    pygame.draw.rect(screen, clear_color, [width // 2, 0, width // 2, 40])
    screen.blit(clear, clearRect)

    # New game button and timer
    new = font.render("NEW GAME", True, black, new_color)
    newRect = new.get_rect()
    newRect.center = (width // 4, height - 20)
    pygame.draw.rect(screen, new_color, [0, 1090, width // 2, 40])
    screen.blit(new, newRect)
    
    timer = font.render(time, True, black, light_orange)
    timerRect = timer.get_rect()
    timerRect.center = (width - (width // 4), height - 20)
    pygame.draw.rect(screen, light_orange, [width // 2, 1090, width // 2, 40])
    screen.blit(timer, timerRect)

    # Win condition
    if len(correct) == numberOfWords:
        win = True
        text = "{0:02}:{1:02}".format(int(score[0]), int(score[1]))
        #print(score)
        if int(score[0]) > minutes or (int(score[0]) >= minutes and int(score[1]) > seconds):
            #score_file = open("high_score.txt", "w")
            #score = [str(minutes), str(seconds)]
            with open("high_score.txt", "w") as out:
                out.write("{}\n{}".format(str(minutes), str(seconds)))
            #score_file.writelines(score)
            text = "{0:02}:{1:02}".format(minutes, seconds)
            score_file.close()

        complete = font.render("Puzzle complete! Best time: " + text, True, black, light_orange)
        completeRect = complete.get_rect()
        completeRect.center = (width // 2, 20)
        pygame.draw.rect(screen, light_orange, [0, 0, width, 40])
        screen.blit(complete, completeRect)

    frames += 1
    clock.tick(60)

    pygame.display.update()

text_file.close()
score_file.close()
pygame.quit()