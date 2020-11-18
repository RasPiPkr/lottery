#!/usr/bin/python3
from tkinter import ttk
import tkinter as tk
import random
import time
import sys
import os


# Assign the light, dark mode colours and startup mode.
light = '#bcbcbc'
dark = '#23272a'
startupMode = dark
numbers = [i for i in range(1, 1000001)] # Custom stars / raffle number range.
ticketFont = ('verdana', 20)


def changeMode(bgMode, txtMode):
    root.config(bg=bgMode)
    menu.config(bg=bgMode, fg=txtMode)
    dispFrame.config(bg=bgMode)

def getNumbers(tickets, main_low, main_high, main_picks, has_stars, star_low, star_high, star_picks):
    for ticket in range(int(tickets)):
        nums = [i for i in range(main_low, main_high + 1)]
        picked = []
        for i in range(main_picks):
            pick = random.choice(nums)
            choice = nums.index(pick)
            picked.append(pick)
            nums.pop(choice)
        picked.sort()
        if has_stars == True:
            starNums = [i for i in range(star_low, star_high + 1)]
            pickedStars = []
            for i in range(star_picks):
                pickStar = random.choice(starNums)
                starChoice = starNums.index(pickStar)
                pickedStars.append(pickStar)
                starNums.pop(starChoice)
            if len(pickedStars) >= 2:
                pickedStars.sort()
            picked.append('-')
            for star in range(len(pickedStars)):
                picked.append(pickedStars[star])
        showTickets.insert('end', picked)
        


def healthLottery():
    global dispFrame, showTickets
    dispFrame.destroy()
    currBG = menu['bg']
    currFG = menu['fg']
    dispFrame = tk.Frame(root, bg=currBG)
    dispFrame.pack(fill='both', expand=True)
    game = tk.Label(dispFrame, text='Health Lottery', bg=currBG, fg=currFG)
    game.pack()
    lines = [str(i).zfill(2) for i in range(1, 51)]
    linesLabel = tk.Label(dispFrame, text='How many lines:', bg=currBG, fg=currFG)
    linesLabel.pack(pady=10)
    getLines = ttk.Combobox(dispFrame, width=3, values=lines)
    getLines.set('01')
    getLines.pack()
    getTickets = tk.Button(dispFrame, text='Generate Ticket(s)', bg=currBG, fg=currFG, command=lambda: getNumbers(getLines.get(), 1, 50, 5, False, 0, 0, 0))
    getTickets.pack(pady=10)
    showTickets = tk.Listbox(dispFrame, width=30, height=10, font=ticketFont)
    showTickets.pack()


def nationalLottery():
    global dispFrame, showTickets, getGame, games, getLines
    dispFrame.destroy()
    currBG = menu['bg']
    currFG = menu['fg']
    dispFrame = tk.Frame(root, bg=currBG)
    dispFrame.pack(fill='both', expand=True)
    games = ['Lotto', 'Thunderball', 'Euromillions']
    getGame = ttk.Combobox(dispFrame, values=games)
    getGame.set('Lotto')
    getGame.pack()
    lines = [str(i).zfill(2) for i in range(1, 51)]
    linesLabel = tk.Label(dispFrame, text='How many lines:', bg=currBG, fg=currFG)
    linesLabel.pack(pady=10)
    getLines = ttk.Combobox(dispFrame, width=3, values=lines)
    getLines.set('01')
    getLines.pack()
    if getGame.get() == 'Lotto':
        getTickets = tk.Button(dispFrame, text='Generate Ticket(s)', bg=currBG, fg=currFG, command=nationalLotteryHandler)
    elif getGame.get() == 'Thunderball':
        getTickets = tk.Button(dispFrame, text='Generate Ticket(s)', bg=currBG, fg=currFG, command=nationalLotteryHandler)
    elif getGame.get() == 'Euromillions':
        getTickets = tk.Button(dispFrame, text='Generate Ticket(s)', bg=currBG, fg=currFG, command=nationalLotteryHandler)
    getTickets.pack(pady=10)
    showTickets = tk.Listbox(dispFrame, width=30, height=10, font=ticketFont)
    showTickets.pack()


def nationalLotteryHandler():
    if getGame.get() == games[0]:
        getNumbers(getLines.get(), 1, 59, 6, False, 0, 0, 0)
    elif getGame.get() == games[1]:
        getNumbers(getLines.get(), 1, 39, 5, True, 1, 14, 1)
    elif getGame.get() == games[2]:
        getNumbers(getLines.get(), 1, 50, 5, True, 1, 12, 2)


def customRaffle():
    global dispFrame, customFrame, starsNeededVar
    dispFrame.destroy()
    currBG = menu['bg']
    currFG = menu['fg']
    dispFrame = tk.Frame(root, bg=currBG)
    dispFrame.pack(fill='both', expand=True)
    game = tk.Label(dispFrame, text='Custom Lottery / Raffle', bg=currBG, fg=currFG)
    game.pack(pady=10)
    customFrame = tk.Frame(dispFrame, bg=currBG)
    customFrame.pack()
    mainNumbersLabel = tk.Label(customFrame, text='How many main numbers per draw do you require: ', bg=currBG, fg=currFG)
    mainNumbersLabel.grid(row=0, column=0, sticky='e')
    mainNumbers = ttk.Combobox(customFrame, value=numbers[:100], width=4)
    mainNumbers.set('1')
    mainNumbers.grid(row=0, column=1, sticky='w')
    mainNumbersLowLabel = tk.Label(customFrame, text='Set the main lowest number: ', bg=currBG, fg=currFG)
    mainNumbersLowLabel.grid(row=1, column=0, sticky='e')
    mainNumbersLow = ttk.Combobox(customFrame, value=numbers[:10000], width=6)
    mainNumbersLow.set('1')
    mainNumbersLow.grid(row=1, column=1, pady=10, sticky='w')
    mainNumbersHighLabel = tk.Label(customFrame, text='Set the main highest number: ', bg=currBG, fg=currFG)
    mainNumbersHighLabel.grid(row=2, column=0, sticky='e')
    mainNumbersHigh = ttk.Combobox(customFrame, value=numbers, width=8)
    mainNumbersHigh.set('1')
    mainNumbersHigh.grid(row=2, column=1, sticky='w')
    starsNeededLabel = tk.Label(customFrame, text='Do you require any stars / bonus numbers? ', bg=currBG, fg=currFG)
    starsNeededLabel.grid(row=3, column=0, pady=10, sticky='e')
    starsNeededVar = tk.BooleanVar()
    starsNeeded = tk.Checkbutton(customFrame, bg=currBG, variable=starsNeededVar, onvalue=True, offvalue=False, command=showStars)
    starsNeeded.grid(row=3, column=1, sticky='w')
    spacer = tk.Label(customFrame, text='', bg=currBG, width=49)
    spacer.grid(row=4, column=0)
    showTickets = tk.Listbox(dispFrame, width=30, height=10, font=ticketFont)
    showTickets.pack(pady=10)


def showStars():
    global starNumbersLabel, starNumbers, starNumbersLowLabel, starNumbersLow, starNumbersHighLabel, starNumbersHigh
    currBG = menu['bg']
    currFG = menu['fg']
    stars = starsNeededVar.get()
    if stars:
        starNumbersLabel = tk.Label(customFrame, text='How many stars / bonus numbers per draw do you require: ', bg=currBG, fg=currFG)
        starNumbersLabel.grid(row=4, column=0, sticky='e')
        starNumbers = ttk.Combobox(customFrame, value=numbers[:20], width=3)
        starNumbers.set('1')
        starNumbers.grid(row=4, column=1, sticky='w')
        starNumbersLowLabel = tk.Label(customFrame, text='Set the stars / bonus lowest number: ', bg=currBG, fg=currFG)
        starNumbersLowLabel.grid(row=5, column=0, pady=10, sticky='e')
        starNumbersLow = ttk.Combobox(customFrame, value=numbers[:10000], width=6)
        starNumbersLow.set('1')
        starNumbersLow.grid(row=5, column=1, sticky='w')
        starNumbersHighLabel = tk.Label(customFrame, text='Set the stars / bonus highest number: ', bg=currBG, fg=currFG)
        starNumbersHighLabel.grid(row=6, column=0, sticky='e')
        starNumbersHigh = ttk.Combobox(customFrame, value=numbers, width=8)
        starNumbersHigh.set('1')
        starNumbersHigh.grid(row=6, column=1, sticky='w')
    else:
        starNumbersLabel.grid_forget()
        starNumbers.grid_forget()
        starNumbersLowLabel.grid_forget()
        starNumbersLow.grid_forget()
        starNumbersHighLabel.grid_forget()
        starNumbersHigh.grid_forget()


# Setup root window
root = tk.Tk()
# Uncomment this next line if you want to remove the title bar. Then to close app use file menu to exit.
##root.attributes('-type', 'splash')
root.title('Lottery / Raffle Number Generator')
root.geometry("600x500")
nums = [i for i in range(1, 50)]

# Menu Tabs
menu = tk.Menu(root)
root.config(menu=menu) 
filemenu = tk.Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='Exit', command=root.destroy)
filemenu.add_separator()
filemenu.add_command(label='UK Health Lottery', command=healthLottery)
filemenu.add_command(label='UK National Lottery', command=nationalLottery)
filemenu.add_separator()
filemenu.add_command(label='Custom Raffle', command=customRaffle)
filemenu.add_separator()
filemenu.add_command(label='Light Mode', command=lambda: changeMode(light, dark))
filemenu.add_command(label='Dark Mode', command=lambda: changeMode(dark, light))
helpmenu = tk.Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About')

dispFrame = tk.Frame(root)
dispFrame.pack(fill='both', expand=True)


if startupMode == dark: # Depending on the startup mode this will set to light or dark mode.
    changeMode(bgMode=dark, txtMode=light)
else:
    changeMode(bgMode=light, txtMode=dark)
    
root.mainloop()
