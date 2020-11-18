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


def changeMode(bgMode, txtMode):
    root.config(bg=bgMode)
    menu.config(bg=bgMode, fg=txtMode)
    dispFrame.config(bg=bgMode)

def getNumbers(tickets, main_low, main_high, main_picks, has_stars, star_low, star_high, star_picks):
    print(tickets, main_low, main_high, main_picks, has_stars, star_low, star_high, star_picks)
    for ticket in range(int(tickets)):
        nums = [i for i in range(main_low, main_high + 1)]
        print(nums)
        picked = []
        for i in range(main_picks):
            pick = random.choice(nums)
            choice = nums.index(pick)
            picked.append(pick)
            nums.pop(choice)
        picked.sort()
        if has_stars == True:
            starNums = [i for i in range(star_low, star_high + 1)]
            print(starNums)
            pickedStars = []
            for i in range(star_picks):
                pickStar = random.choice(starNums)
                starChoice = starNums.index(pickStar)
                pickedStars.append(pickStar)
                starNums.pop(starChoice)
            if len(pickedStars) >= 2:
                pickedStars.sort()
            picked.append('--')
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
    showTickets = tk.Listbox(dispFrame, width=20, height=10)
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
    showTickets = tk.Listbox(dispFrame, width=20, height=10)
    showTickets.pack()


def nationalLotteryHandler():
    if getGame.get() == games[0]:
        getNumbers(getLines.get(), 1, 59, 6, False, 0, 0, 0)
    elif getGame.get() == games[1]:
        getNumbers(getLines.get(), 1, 39, 5, True, 1, 14, 1)
    elif getGame.get() == games[2]:
        getNumbers(getLines.get(), 1, 50, 5, True, 1, 12, 2)


# Setup root window
root = tk.Tk()
# Uncomment this next line if you want to remove the title bar. Then to close app use file menu to exit.
##root.attributes('-type', 'splash')
root.title('Lottery Picker')
root.geometry("600x400")
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
filemenu.add_command(label='Custom Raffle')
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
