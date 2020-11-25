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
textFont = ('Verdana', 10)
startupMode = dark
numbers = [i for i in range(1, 1000001)] # Custom stars / raffle number range.


def changeMode(bgMode, txtMode):
    root.config(bg=bgMode)
    menu.config(bg=bgMode, fg=txtMode)
    filemenu.config(bg=bgMode, fg=txtMode)
    helpmenu.config(bg=bgMode, fg=txtMode)
    dispFrame.config(bg=bgMode)
    ticketFrame.config(bg=bgMode)
    getTickets.config(bg=bgMode, fg=txtMode)
    try: # healthLottery
        game.config(bg=bgMode, fg=txtMode)
    except:
        pass
    try: # nationalLottery
        linesLabel.config(bg=bgMode, fg=txtMode)
    except:
        pass
    try: # customLottery main
        customFrame.config(bg=bgMode)
        game.config(bg=bgMode, fg=txtMode)
        starsNeededLabel.config(bg=bgMode, fg=txtMode)
        mainNumbersLabel.config(bg=bgMode, fg=txtMode)
        mainNumbersLowLabel.config(bg=bgMode, fg=txtMode)
        mainNumbersHighLabel.config(bg=bgMode, fg=txtMode)
        starsNeeded.config(bg=bgMode, fg=txtMode, highlightbackground=bgMode)
        linesLabel.config(bg=bgMode, fg=txtMode)
    except:
        pass
    try: # customLottery stars
        starNumbersLabel.config(bg=bgMode, fg=txtMode)
        starNumbersLowLabel.config(bg=bgMode, fg=txtMode)
        starNumbersHighLabel.config(bg=bgMode, fg=txtMode)
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


def healthLottery(bgMode, txtMode):
    global dispFrame, ticketFrame, showTickets, game, linesLabel, getLines, getTickets
    dispFrame.destroy()
    ticketFrame.destroy()
    dispFrame = tk.Frame(root, bg=bgMode)
    dispFrame.pack()
    ticketFrame = tk.Frame(root, bg=bgMode)
    ticketFrame.pack()
    game = tk.Label(dispFrame, text='Health Lottery', bg=bgMode, fg=txtMode, font=textFont)
    game.pack(pady=10)
    lines = [str(i).zfill(2) for i in range(1, 11)]
    linesLabel = tk.Label(dispFrame, text='How many lines:', bg=bgMode, fg=txtMode, font=textFont)
    linesLabel.pack()
    getLines = ttk.Combobox(dispFrame, width=3, values=lines)
    getLines.set('01')
    getLines.pack()
    getLines.bind('<<ComboboxSelected>>', healthLotteryHandler)
    getTickets = tk.Button(dispFrame, text='Generate Ticket(s)', bg=bgMode, fg=txtMode, font=textFont, command=lambda: getNumbers(getLines.get(), 1, 50, 5, False, 0, 0, 0))
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
    ticketFrame.pack()
    showTickets = ttk.Treeview(ticketFrame, columns=[i for i in range(1, 6)], show='headings', height=getLines.get())
    showTickets.pack(padx=20, pady=20)
    for i in range(1, 6):
        showTickets.column(i, width=30)
        showTickets.heading(i, text=str(i))


def nationalLottery(bgMode, txtMode):
    global dispFrame, ticketFrame, showTickets, getGame, games, linesLabel, getLines, bonus, getTickets
    dispFrame.destroy()
    ticketFrame.destroy()
    dispFrame = tk.Frame(root, bg=bgMode)
    dispFrame.pack()
    games = ['Lotto', 'Thunderball', 'Euromillions']
    getGame = ttk.Combobox(dispFrame, values=games, font=textFont)
    getGame.set('Lotto')
    getGame.pack(pady=20)
    getGame.bind('<<ComboboxSelected>>', setNationalLayout)
    lines = [str(i).zfill(2) for i in range(1, 11)]
    linesLabel = tk.Label(dispFrame, text='How many lines:', bg=bgMode, fg=txtMode, font=textFont)
    linesLabel.pack()
    getLines = ttk.Combobox(dispFrame, width=3, values=lines, font=textFont)
    getLines.set('01')
    getLines.pack()
    getLines.bind('<<ComboboxSelected>>', setNationalLayout)
    getTickets = tk.Button(dispFrame, text='Generate Ticket(s)', bg=bgMode, fg=txtMode, font=textFont, command=nationalLotteryHandler)
    getTickets.pack(pady=10)
    ticketFrame = tk.Frame(root, bg=bgMode, height=200)
    ticketFrame.pack()
    showTickets = ttk.Treeview(ticketFrame, columns=[1, 2, 3, 4, 5, 6], show='headings', height='1')
    showTickets.pack(pady=20)
    for i in range(1, 7):
        showTickets.column(i, width=30)
        showTickets.heading(i, text=str(i))


def setNationalLayout(event=None):
    global ticketFrame, showTickets, bonus
    ticketFrame.destroy()
    bgMode = menu['bg']
    ticketFrame = tk.Frame(root, bg=bgMode)
    ticketFrame.pack()
    if getGame.get() == games[0]:
        showTickets = ttk.Treeview(ticketFrame, columns=[1, 2, 3, 4, 5, 6], show='headings', height=getLines.get()) 
        showTickets.pack(pady=20)
        for i in range(1, 7):
            showTickets.column(str(i), width=50)
            showTickets.heading(i, text=str(i))
    elif getGame.get() == games[1]:
        showTickets = ttk.Treeview(ticketFrame, columns=[1, 2, 3, 4, 5], show='headings', height=getLines.get()) 
        showTickets.pack(side='left', pady=20)
        for i in range(1, 6):
            showTickets.column(str(i), width=50)
            showTickets.heading(i, text=str(i))
        bonus = ttk.Treeview(ticketFrame, columns=[1], show='headings', height=getLines.get())
        bonus.pack(side='left', padx=5)
        bonus.column('1', width=100)
        bonus.heading(1, text='Thunderball')
    elif getGame.get() == games[2]:
        showTickets = ttk.Treeview(ticketFrame, columns=[1, 2, 3, 4, 5], show='headings', height=getLines.get()) 
        showTickets.pack(side='left', pady=20)
        for i in range(1, 6):
            showTickets.column(str(i), width=50)
            showTickets.heading(i, text=str(i))
        bonus = ttk.Treeview(ticketFrame, columns=[1, 2], show='headings', height=getLines.get())
        bonus.pack(side='left', padx=5)
        for i in range(1, 3):
            bonus.column(str(i), width=70)
            bonus.heading(i, text='Star {}'.format(i))


def nationalLotteryHandler():
    if getGame.get() == games[0]:
        getNumbers(getLines.get(), 1, 59, 6, False, 0, 0, 0)
    elif getGame.get() == games[1]:
        getNumbers(getLines.get(), 1, 39, 5, True, 1, 14, 1)
    elif getGame.get() == games[2]:
        getNumbers(getLines.get(), 1, 50, 5, True, 1, 12, 2)


def customRaffle(bgMode, txtMode):
    global dispFrame, ticketFrame, showTickets, customFrame, starsNeededVar, starsNeeded, starsNeededLabel, getTickets, getLines, game
    global mainNumbers, mainNumbersLabel, mainNumbersLow, mainNumbersLowLabel, mainNumbersHigh, mainNumbersHighLabel, linesLabel
    dispFrame.destroy()
    ticketFrame.destroy()
    dispFrame = tk.Frame(root, bg=bgMode)
    dispFrame.pack()#side='top')
    game = tk.Label(dispFrame, text='Custom Lottery / Raffle', bg=bgMode, fg=txtMode, font=textFont)
    game.pack(pady=10)
    customFrame = tk.Frame(dispFrame, bg=bgMode)
    customFrame.pack()
    mainNumbersLabel = tk.Label(customFrame, text='How many main numbers per draw do you require: ', bg=bgMode, fg=txtMode, font=textFont)
    mainNumbersLabel.grid(row=0, column=0, sticky='e')
    mainNumbers = ttk.Combobox(customFrame, value=numbers[:100], width=4, font=textFont)
    mainNumbers.set('1')
    mainNumbers.grid(row=0, column=1, sticky='w')
    mainNumbers.bind('<<ComboboxSelected>>', customLayout)
    mainNumbersLowLabel = tk.Label(customFrame, text='Set the main lowest number: ', bg=bgMode, fg=txtMode, font=textFont)
    mainNumbersLowLabel.grid(row=1, column=0, sticky='e')
    mainNumbersLow = ttk.Combobox(customFrame, value=numbers[:10000], width=6, font=textFont)
    mainNumbersLow.set('1')
    mainNumbersLow.grid(row=1, column=1, pady=10, sticky='w')
    mainNumbersHighLabel = tk.Label(customFrame, text='Set the main highest number: ', bg=bgMode, fg=txtMode, font=textFont)
    mainNumbersHighLabel.grid(row=2, column=0, sticky='e')
    mainNumbersHigh = ttk.Combobox(customFrame, value=numbers, width=8, font=textFont)
    mainNumbersHigh.set('2')
    mainNumbersHigh.grid(row=2, column=1, sticky='w')
    mainNumbersHigh.bind('<<ComboboxSelected>>', customLayout)
    starsNeededLabel = tk.Label(customFrame, text='Do you require any stars / bonus numbers? ', bg=bgMode, fg=txtMode, font=textFont)
    starsNeededLabel.grid(row=3, column=0, pady=10, sticky='e')
    starsNeededVar = tk.BooleanVar()
    starsNeeded = tk.Checkbutton(customFrame, bg=bgMode, variable=starsNeededVar, onvalue=True, offvalue=False, bd=0, highlightbackground=bgMode, command=customStars)
    starsNeeded.grid(row=3, column=1, sticky='w')
    lines = [str(i).zfill(2) for i in range(1, 11)]
    linesLabel = tk.Label(customFrame, text='How many tickets:', bg=bgMode, fg=txtMode, font=textFont)
    linesLabel.grid(row=7, column=0, pady=10, sticky='e')
    getLines = ttk.Combobox(customFrame, width=3, values=lines, font=textFont)
    getLines.set('01')
    getLines.grid(row=7, column=1, sticky='w')
    getLines.bind('<<ComboboxSelected>>', customLayout)
    getTickets = tk.Button(dispFrame, text='Generate Ticket(s)', bg=bgMode, fg=txtMode, font=textFont, command=preCustomHandler)
    getTickets.pack(pady=10)
    ticketFrame = tk.Frame(root, bg=bgMode)
    ticketFrame.pack()
    showTickets = ttk.Treeview(ticketFrame, columns=[str(i) for i in range(1, int(mainNumbers.get()) + 1)], show='headings', height=str(getLines.get())) 
    showTickets.pack(side='left', pady=20)
    showTickets.column('1', width=15)
    showTickets.heading(1, text='1')


def preCustomHandler():
    customLayout()
    customHandler()


def customLayout(event=None):
    global ticketFrame, showTickets, bonus, stars
    ticketFrame.destroy()
    currBG = menu['bg']
    ticketFrame = tk.Frame(root, bg=currBG)
    ticketFrame.pack()
    showTickets = ttk.Treeview(ticketFrame, columns=[str(i) for i in range(1, int(mainNumbers.get()) + 1)], show='headings', height=getLines.get()) 
    showTickets.pack(side='left')
    mainDigits = len(mainNumbersHigh.get()) + 1
    for i in range(1, int(mainNumbers.get()) + 1):
        showTickets.column(str(i), width=int(mainDigits * 15 / 1.5))
        showTickets.heading(i, text=str(i))
    try:
        if stars:
            starDigits = len(starNumbersHigh.get()) + 1
            bonus = ttk.Treeview(ticketFrame, columns=[str(i) for i in range(1, int(starNumbers.get()) + 1)], show='headings', height=getLines.get())
            bonus.pack(side='left', padx=5)
            for i in range(1, int(starNumbers.get()) + 1):
                bonus.column(str(i), width=int(starDigits * 15 / 1.5))
                bonus.heading(i, text=str(i))
    except NameError:
        pass


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


def customStars():
    global starNumbersLabel, starNumbers, starNumbersLowLabel, starNumbersLow, starNumbersHighLabel, starNumbersHigh, stars, bonus
    bgMode = menu['bg']
    txtMode = menu['fg']
    stars = starsNeededVar.get()
    if stars:
        starNumbersLabel = tk.Label(customFrame, text='How many stars / bonus numbers do you require: ', bg=bgMode, fg=txtMode, font=textFont)
        starNumbersLabel.grid(row=4, column=0, sticky='e')
        starNumbers = ttk.Combobox(customFrame, value=numbers[:20], width=3, font=textFont)
        starNumbers.set('1')
        starNumbers.grid(row=4, column=1, sticky='w')
        starNumbers.bind('<<ComboboxSelected>>', customLayout)
        starNumbersLowLabel = tk.Label(customFrame, text='Set the stars / bonus lowest number: ', bg=bgMode, fg=txtMode, font=textFont)
        starNumbersLowLabel.grid(row=5, column=0, pady=10, sticky='e')
        starNumbersLow = ttk.Combobox(customFrame, value=numbers[:10000], width=6, font=textFont)
        starNumbersLow.set('1')
        starNumbersLow.grid(row=5, column=1, sticky='w')
        starNumbersHighLabel = tk.Label(customFrame, text='Set the stars / bonus highest number: ', bg=bgMode, fg=txtMode, font=textFont)
        starNumbersHighLabel.grid(row=6, column=0, sticky='e')
        starNumbersHigh = ttk.Combobox(customFrame, value=numbers, width=8, font=textFont)
        starNumbersHigh.set('2')
        starNumbersHigh.grid(row=6, column=1, sticky='w')
        starNumbersHigh.bind('<<ComboboxSelected>>', customLayout)
        bonus = ttk.Treeview(ticketFrame, columns=(1), show='headings', height=getLines.get())
        bonus.pack(side='left', padx=5)
        bonus.column('1', width=15)
        bonus.heading(1, text='1')
    else:
        starNumbersLabel.grid_forget()
        starNumbers.grid_forget()
        starNumbersLowLabel.grid_forget()
        starNumbersLow.grid_forget()
        starNumbersHighLabel.grid_forget()
        starNumbersHigh.grid_forget()
        bonus.destroy()


def aboutMode(bgMode, txtMode):
    root.config(bg=bgMode)
    dispFrame.config(bg=bgMode)
    menu.config(bg=bgMode, fg=txtMode)
    filemenu.config(bg=bgMode, fg=txtMode)
    helpmenu.config(bg=bgMode, fg=txtMode)
    title.config(bg=bgMode, fg=txtMode)
    line.config(bg=bgMode, fg=txtMode)
    line2.config(bg=bgMode, fg=txtMode)



def about(bgMode, txtMode):
    global dispFrame, ticketFrame, menu, filemenu, helpmenu, title, line, line2
    menu = tk.Menu(root, bg=bgMode, fg=txtMode)
    root.config(menu=menu) 
    filemenu = tk.Menu(menu, bg=bgMode, fg=txtMode, font=textFont, tearoff=0) 
    menu.add_cascade(label='File', menu=filemenu) 
    filemenu.add_command(label='Exit', command=root.destroy)
    filemenu.add_separator()
    filemenu.add_command(label='UK Health Lottery', command=lambda: healthLottery(bgMode, txtMode))
    filemenu.add_command(label='UK National Lottery', command=lambda: nationalLottery(bgMode, txtMode))
    filemenu.add_separator()
    filemenu.add_command(label='Custom Raffle', command=lambda: customRaffle(bgMode, txtMode))
    filemenu.add_separator()
    filemenu.add_command(label='Light Mode', command=lambda: aboutMode(light, dark))
    filemenu.add_command(label='Dark Mode', command=lambda: aboutMode(dark, light))
    helpmenu = tk.Menu(menu, bg=bgMode, fg=txtMode, font=textFont, tearoff=0) 
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About', command=lambda: about(bgMode, txtMode))
    dispFrame.destroy()
    ticketFrame.destroy()
    dispFrame = tk.Frame(root, bg=bgMode)
    dispFrame.pack(fill='both', expand=True)
    title = tk.Label(dispFrame, text='Thank you for downloading the Worldwide Lottery / Raffle Number Generator', bg=bgMode, fg=txtMode, font=textFont)
    title.pack(pady=30)
    line = tk.Label(dispFrame, text='This project was initially started by Martin Parker in the UK,', bg=bgMode, fg=txtMode, font=textFont)
    line.pack(pady=10)
    line2 = tk.Label(dispFrame, text='in order that people could contribute all around the world.', bg=bgMode, fg=txtMode, font=textFont)
    line2.pack(pady=10)
    ticketFrame = tk.Frame(root, bg=bgMode)
    ticketFrame.pack()


def main(bgMode, txtMode):
    global dispFrame, ticketFrame, menu, filemenu, helpmenu 
    # Menu Tabs
    menu = tk.Menu(root, bg=bgMode, fg=txtMode)
    root.config(menu=menu, bg=bgMode) 
    filemenu = tk.Menu(menu, bg=bgMode, fg=txtMode, font=textFont, tearoff=0) 
    menu.add_cascade(label='File', menu=filemenu) 
    filemenu.add_command(label='Exit', command=root.destroy)
    filemenu.add_separator()
    filemenu.add_command(label='UK Health Lottery', command=lambda: healthLottery(bgMode, txtMode))
    filemenu.add_command(label='UK National Lottery', command=lambda: nationalLottery(bgMode, txtMode))
    filemenu.add_separator()
    filemenu.add_command(label='Custom Raffle', command=lambda: customRaffle(bgMode, txtMode))
    filemenu.add_separator()
    filemenu.add_command(label='Light Mode', command=lambda: changeMode(light, dark))
    filemenu.add_command(label='Dark Mode', command=lambda: changeMode(dark, light))
    helpmenu = tk.Menu(menu, bg=bgMode, fg=txtMode, font=textFont, tearoff=0) 
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About', command=lambda: about(bgMode, txtMode))
    # Startup screen
    dispFrame = tk.Frame(root, bg=bgMode)
    dispFrame.pack(fill='both', expand=True)
    ticketFrame = tk.Frame(root, bg=bgMode)
    ticketFrame.pack()
    

# Setup root window
root = tk.Tk()
# Uncomment this next line if you want to remove the title bar. Then to close app use file menu to exit.
##root.attributes('-type', 'splash')
root.title('Lottery / Raffle Number Generator')
root.geometry("600x600")


if startupMode == dark:
    main(dark, light)
else:
    main(light, dark)
    
root.mainloop()
