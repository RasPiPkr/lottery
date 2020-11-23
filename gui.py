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
    filemenu.config(bg=bgMode, fg=txtMode)
    helpmenu.config(bg=bgMode, fg=txtMode)
    dispFrame.config(bg=bgMode)
    ticketFrame.config(bg=bgMode)
    try:
        customFrame.config(bg=currBG)
        mainNumbersLabel.config(bg=bgMode, fg=txtMode)
        mainNumbersLowLabel.config(bg=bgMode, fg=txtMode)
        mainNumbersHighLabel.config(bg=bgMode, fg=fgMode)
    except:
        pass


def getNumbers(tickets, main_low, main_high, main_picks, has_stars, star_low, star_high, star_picks):
    try:
        for ticket in range(int(tickets)):
            nums = [i for i in range(int(main_low), int(main_high) + 1)]
            picked = []
            for i in range(int(main_picks)):
                pick = random.choice(nums)
                choice = nums.index(pick)
                picked.append(pick)
                nums.pop(choice)
            picked.sort()
            showTickets.insert('', 'end', values=picked)
            if has_stars == True:
                starNums = [i for i in range(int(star_low), int(star_high) + 1)]
                pickedStars = []
                for i in range(int(star_picks)):
                    pickStar = random.choice(starNums)
                    starChoice = starNums.index(pickStar)
                    pickedStars.append(pickStar)
                    starNums.pop(starChoice)
                if len(pickedStars) >= 2:
                    pickedStars.sort()
                bonus.insert('', 'end', values=pickedStars)
    except IndexError:
        pass


def setTicketLayout(event=None):
    global ticketFrame, showTickets, bonus, stars
    ticketFrame.destroy()
    currBG = dispFrame['bg']
    ticketFrame = tk.Frame(root, bg=currBG)
    ticketFrame.pack(side='top')
    showTickets = ttk.Treeview(ticketFrame, columns=[str(i) for i in range(1, int(mainNumbers.get()) + 1)], show='headings', height=getLines.get()) 
    showTickets.pack(side='left')
    mainDigits = len(mainNumbersHigh.get())
    for i in range(1, int(mainNumbers.get()) + 1):
        showTickets.column(str(i), width=mainDigits * 10)
        showTickets.heading(i, text=str(i))
    try:
        if stars:
            starDigits = len(starNumbersHigh.get())
            bonus = ttk.Treeview(ticketFrame, columns=[str(i) for i in range(1, int(starNumbers.get()) + 1)], show='headings', height=getLines.get())
            bonus.pack(side='left', padx=5)
            for i in range(1, int(starNumbers.get()) + 1):
                bonus.column(str(i), width=starDigits * 10)
                bonus.heading(i, text=str(i))
    except NameError:
        pass


def healthLottery():
    global dispFrame, ticketFrame, showTickets, getLines
    dispFrame.destroy()
    ticketFrame.destroy()
    currBG = menu['bg']
    currFG = menu['fg']
    dispFrame = tk.Frame(root, bg=currBG)
    dispFrame.pack(fill='both', expand=True)
    ticketFrame = tk.Frame(root, bg=currBG)
    ticketFrame.pack(side='bottom', fill='x')
    game = tk.Label(dispFrame, text='Health Lottery', bg=currBG, fg=currFG)
    game.pack()
    lines = [str(i).zfill(2) for i in range(1, 51)]
    linesLabel = tk.Label(dispFrame, text='How many lines:', bg=currBG, fg=currFG)
    linesLabel.pack(pady=10)
    getLines = ttk.Combobox(dispFrame, width=3, values=lines)
    getLines.set('01')
    getLines.pack()
    getLines.bind('<<ComboboxSelected>>', healthLotteryHandler)
    getTickets = tk.Button(dispFrame, text='Generate Ticket(s)', bg=currBG, fg=currFG, command=lambda: getNumbers(getLines.get(), 1, 50, 5, False, 0, 0, 0))
    getTickets.pack(pady=10)
    showTickets = ttk.Treeview(ticketFrame, columns=[i for i in range(1, 6)], show='headings', height=getLines.get())
    showTickets.pack(padx=20, pady=20)
    for i in range(1, 6):
        showTickets.column(i, width=30)
        showTickets.heading(i, text=str(i))


def healthLotteryHandler(event=None):
    global ticketFrame, showTickets
    ticketFrame.destroy()
    currBG = menu['bg']
    ticketFrame = tk.Frame(root, bg=currBG)
    ticketFrame.pack(side='bottom', fill='x')
    showTickets = ttk.Treeview(ticketFrame, columns=[i for i in range(1, 6)], show='headings', height=getLines.get())
    showTickets.pack(padx=20, pady=20)
    for i in range(1, 6):
        showTickets.column(i, width=30)
        showTickets.heading(i, text=str(i))


def nationalLottery():
    global dispFrame, tiicketFrame, showTickets, getGame, games, getLines, bonus
    dispFrame.destroy()
    currBG = menu['bg']
    currFG = menu['fg']
    dispFrame = tk.Frame(root, bg=currBG)
    dispFrame.pack(fill='both', expand=True)
    ticketFrame = tk.Frame(root, bg=currBG, height=200)
    ticketFrame.pack(side='bottom', fill='x')
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
    getTickets = tk.Button(dispFrame, text='Generate Ticket(s)', bg=currBG, fg=currFG, command=nationalLotteryHandler)
    getTickets.pack(pady=10)
    showTickets = ttk.Treeview(ticketFrame, columns=(1, 2, 3, 4, 5, 6), show='headings', height='5')
    showTickets.pack(side='left')
    bonus = ttk.Treeview(ticketFrame, columns=(1, 2), show='headings', height='5')
    bonus.pack(side='left')
    showTickets.column('1', width=50)
    showTickets.column('2', width=50)
    showTickets.column('3', width=50)
    showTickets.column('4', width=50)
    showTickets.column('5', width=50)
    showTickets.column('6', width=50)
    showTickets.heading(1, text='1')
    showTickets.heading(2, text='2')
    showTickets.heading(3, text='3')
    showTickets.heading(4, text='4')
    showTickets.heading(5, text='5')
    showTickets.heading(6, text='6')
    bonus.column('1', width=50)
    bonus.column('2', width=50)
    bonus.heading(1, text='Bonus')
    bonus.heading(2, text='Bonus')


def nationalLotteryHandler():
    if getGame.get() == games[0]:
        getNumbers(getLines.get(), 1, 59, 6, False, 0, 0, 0)
    elif getGame.get() == games[1]:
        getNumbers(getLines.get(), 1, 39, 5, True, 1, 14, 1)
    elif getGame.get() == games[2]:
        getNumbers(getLines.get(), 1, 50, 5, True, 1, 12, 2)


def customRaffle():
    global dispFrame, ticketFrame, showTickets, customFrame, starsNeededVar, getTickets, getLines
    global mainNumbers, mainNumbersLabel, mainNumbersLow, mainNumbersLowLabel, mainNumbersHigh, mainNumbersHighLabel
    dispFrame.destroy()
    currBG = menu['bg']
    currFG = menu['fg']
    dispFrame = tk.Frame(root, bg=currBG)
    dispFrame.pack(side='top', fill='both', expand=True)
    game = tk.Label(dispFrame, text='Custom Lottery / Raffle', bg=currBG, fg=currFG)
    game.pack(pady=10)
    customFrame = tk.Frame(dispFrame, bg=currBG)
    customFrame.pack()
    mainNumbersLabel = tk.Label(customFrame, text='How many main numbers per draw do you require: ', bg=currBG, fg=currFG)
    mainNumbersLabel.grid(row=0, column=0, sticky='e')
    mainNumbers = ttk.Combobox(customFrame, value=numbers[:100], width=4)
    mainNumbers.set('1')
    mainNumbers.grid(row=0, column=1, sticky='w')
    mainNumbers.bind('<<ComboboxSelected>>', setTicketLayout)
    mainNumbersLowLabel = tk.Label(customFrame, text='Set the main lowest number: ', bg=currBG, fg=currFG)
    mainNumbersLowLabel.grid(row=1, column=0, sticky='e')
    mainNumbersLow = ttk.Combobox(customFrame, value=numbers[:10000], width=6)
    mainNumbersLow.set('1')
    mainNumbersLow.grid(row=1, column=1, pady=10, sticky='w')
    mainNumbersHighLabel = tk.Label(customFrame, text='Set the main highest number: ', bg=currBG, fg=currFG)
    mainNumbersHighLabel.grid(row=2, column=0, sticky='e')
    mainNumbersHigh = ttk.Combobox(customFrame, value=numbers, width=8)
    mainNumbersHigh.set('2')
    mainNumbersHigh.grid(row=2, column=1, sticky='w')
    mainNumbersHigh.bind('<<ComboboxSelected>>', setTicketLayout)
    starsNeededLabel = tk.Label(customFrame, text='Do you require any stars / bonus numbers? ', bg=currBG, fg=currFG)
    starsNeededLabel.grid(row=3, column=0, pady=10, sticky='e')
    starsNeededVar = tk.BooleanVar()
    starsNeeded = tk.Checkbutton(customFrame, bg=currBG, variable=starsNeededVar, onvalue=True, offvalue=False, bd=0, highlightbackground=currBG, command=showStars)
    starsNeeded.grid(row=3, column=1, sticky='w')
    lines = [str(i).zfill(2) for i in range(1, 51)]
    linesLabel = tk.Label(customFrame, text='How many tickets:', bg=currBG, fg=currFG)
    linesLabel.grid(row=7, column=0, pady=10, sticky='e')
    getLines = ttk.Combobox(customFrame, width=3, values=lines)
    getLines.set('01')
    getLines.grid(row=7, column=1, sticky='w')
    getLines.bind('<<ComboboxSelected>>', setTicketLayout)
    getTickets = tk.Button(dispFrame, text='Generate Ticket(s)', bg=currBG, fg=currFG, command=customHandler)
    getTickets.pack(pady=10)
    ticketFrame = tk.Frame(root, bg=currBG)
    ticketFrame.pack()
    showTickets = ttk.Treeview(ticketFrame, columns=[str(i) for i in range(1, int(mainNumbers.get()) + 1)], show='headings', height=str(getLines.get())) 
    showTickets.pack(side='left')
    showTickets.column('1', width=15)
    showTickets.heading(1, text='1')


def customHandler():
    try:
        if mainNumbersHigh.get() <= mainNumbersLow.get():
            getTickets.config(text='Please check main numbers!')
            root.update()
            root.after(3000, getTickets.config(text='Generate Ticket(s)'))
        elif (int(mainNumbersHigh.get()) - int(mainNumbersLow.get())) < int(mainNumbers.get()):
            getTickets.config(text='Too many numbers for the set number range!')
            root.update()
            root.after(3000, getTickets.config(text='Generate Ticket(s)'))
        stars = starsNeededVar.get()
        if stars:
            if starNumbersHigh.get() <= starNumbersLow.get():
                getTickets.config(text='Please check star / bonus numbers!')
                root.update()
                root.after(3000, getTickets.config(text='Generate Ticket(s)'))
            elif (int(starNumbersHigh.get()) - int(starNumbersLow.get())) < int(starNumbers.get()):
                getTickets.config(text='Too many numbers for the set number range!')
                root.update()
                root.after(3000, getTickets.config(text='Generate Ticket(s)'))
            else:
                getNumbers(getLines.get(), mainNumbersLow.get(), mainNumbersHigh.get(), mainNumbers.get(), True, starNumbersLow.get(), starNumbersHigh.get(), starNumbers.get())
        else:
            getNumbers(getLines.get(), mainNumbersLow.get(), mainNumbersHigh.get(), mainNumbers.get(), False, 0, 0, 0)
    except ValueError:
        getTickets.config(text='Sorry, numerical digits required!')
        root.update()
        root.after(3000, getTickets.config(text='Generate Ticket(s)'))


def showStars():
    global starNumbersLabel, starNumbers, starNumbersLowLabel, starNumbersLow, starNumbersHighLabel, starNumbersHigh, stars, bonus
    currBG = menu['bg']
    currFG = menu['fg']
    stars = starsNeededVar.get()
    if stars:
        starNumbersLabel = tk.Label(customFrame, text='How many stars / bonus numbers do you require: ', bg=currBG, fg=currFG)
        starNumbersLabel.grid(row=4, column=0, sticky='e')
        starNumbers = ttk.Combobox(customFrame, value=numbers[:20], width=3)
        starNumbers.set('1')
        starNumbers.grid(row=4, column=1, sticky='w')
        starNumbers.bind('<<ComboboxSelected>>', setTicketLayout)
        starNumbersLowLabel = tk.Label(customFrame, text='Set the stars / bonus lowest number: ', bg=currBG, fg=currFG)
        starNumbersLowLabel.grid(row=5, column=0, pady=10, sticky='e')
        starNumbersLow = ttk.Combobox(customFrame, value=numbers[:10000], width=6)
        starNumbersLow.set('1')
        starNumbersLow.grid(row=5, column=1, sticky='w')
        starNumbersHighLabel = tk.Label(customFrame, text='Set the stars / bonus highest number: ', bg=currBG, fg=currFG)
        starNumbersHighLabel.grid(row=6, column=0, sticky='e')
        starNumbersHigh = ttk.Combobox(customFrame, value=numbers, width=8)
        starNumbersHigh.set('2')
        starNumbersHigh.grid(row=6, column=1, sticky='w')
        starNumbersHigh.bind('<<ComboboxSelected>>', setTicketLayout)
        bonus = ttk.Treeview(ticketFrame, columns=(1), show='headings', height=getLines.get())
        bonus.pack(side='left', padx=5)
        bonus.column('1', width=10)
        bonus.heading(1, text='1')
    else:
        starNumbersLabel.grid_forget()
        starNumbers.grid_forget()
        starNumbersLowLabel.grid_forget()
        starNumbersLow.grid_forget()
        starNumbersHighLabel.grid_forget()
        starNumbersHigh.grid_forget()
        bonus.destroy()


def about():
    global dispFrame
    dispFrame.destroy()
    currBG = menu['bg']
    currFG = menu['fg']
    dispFrame = tk.Frame(root, bg=currBG)
    dispFrame.pack(fill='both', expand=True)
    title = tk.Label(dispFrame, text='Thank you for downloading the Worldwide Lottery / Raffle Number Generator', bg=currBG, fg=currFG)
    title.pack(pady=30)
    line = tk.Label(dispFrame, text='This project was initially started by Martin Parker in the UK,', bg=currBG, fg=currFG)
    line.pack(pady=10)
    line2 = tk.Label(dispFrame, text='in order that people could contribute all around the world.', bg=currBG, fg=currFG)
    line2.pack(pady=10)
    

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
filemenu = tk.Menu(menu, tearoff=0) 
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
helpmenu = tk.Menu(menu, tearoff=0) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About', command=about)
# Startup screen
dispFrame = tk.Frame(root)
dispFrame.pack(fill='both', expand=True)
ticketFrame = tk.Frame(root)
ticketFrame.pack(side='bottom', fill='x')


if startupMode == dark: # Depending on the startup mode this will set to light or dark mode.
    changeMode(bgMode=dark, txtMode=light)
else:
    changeMode(bgMode=light, txtMode=dark)
    
root.mainloop()
