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


def getNumbers(tickets, main_low, main_high, main_picks, is_star_picks, star_low_range, star_high_range, star_picks):
    for ticket in range(int(tickets)):
        nums = [i for i in range(main_low, main_high)]
        picked = []
        for i in range(main_picks):
            pick = random.choice(nums)
            choice = nums.index(pick)
            picked.append(pick)
            nums.pop(choice)
        picked.sort()
        showTickets.insert('end', picked)


def healthLottery():
    global dispFrame, showTickets
    currBG = menu['bg']
    currFG = menu['fg']
    dispFrame = tk.Frame(root, bg=currBG)
    dispFrame.pack(fill='both', expand=True)
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
filemenu.add_command(label='UK National Lottery')
filemenu.add_separator()
filemenu.add_command(label='Custom Raffle')
filemenu.add_separator()
filemenu.add_command(label='Light Mode', command=lambda: changeMode(light, dark))
filemenu.add_command(label='Dark Mode', command=lambda: changeMode(dark, light))
helpmenu = tk.Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About')


if startupMode == dark: # Depending on the startup mode this will set to light or dark mode.
    changeMode(bgMode=dark, txtMode=light)
else:
    changeMode(bgMode=light, txtMode=dark)
    
root.mainloop()
