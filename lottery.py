#!/usr/bin/python3
import random, time, sys, re, os

''' THIS SCRIPT WAS INTENDED FOR LEARNING PURPOSES ONLY!!!
I (Martin Parker) will not be held responsible for any debt caused or
dissappointment in losing your money.

I made this script to get used to using classes.
This script is based on the United Kingdom lottery current as of 01/07/2018.

The custom option is so you can create a raffle or for your lottery in your area.
'''

# Works in python3 idle, or run sudo python3 ./lottery.py in terminal.

goes = 0

class Lottery:
    
    def __init__(self, main_low_range, main_high_range, main_picks, is_star_picks, star_low_range, star_high_range, star_picks):
        self.main_low_range = main_low_range
        self.main_high_range = main_high_range + 1
        self.main_picks = main_picks
        self.is_star_picks = is_star_picks
        self.star_low_range = star_low_range
        self.star_high_range = star_high_range + 1
        self.star_picks = star_picks
        for i in range(self.main_low_range, self.main_high_range):
            main_numbers.append(i)
        if is_star_picks == True:
            for i in range(self.star_low_range, self.star_high_range):
                star_numbers.append(i)

    def get_numbers(self, ticket):
        for i in range(self.main_picks):
            pick = random.choice(main_numbers)
            choice = main_numbers.index(pick)
            picked_numbers.append(pick)
            main_numbers.pop(choice)
        picked_numbers.sort()
        print('Ticket', ticket, 'numbers:', self.tidy_display(picked_numbers))

    def get_star_picks(self, info = 'bonus:'):
        for i in range(self.star_picks):
            star_pick = random.choice(star_numbers)
            choice = star_numbers.index(star_pick)
            picked_star_picks.append(star_pick)
            star_numbers.pop(choice)
        picked_star_picks.sort()
        self.tidy_display(picked_star_picks)
        print('and your', info, self.tidy_display(picked_star_picks))

    def tidy_display(self, tidy_up):
        self.tidy_up = tidy_up
        temp = str(tidy_up)
        temp = temp.replace('[', '')
        temp = temp.replace("'", '')
        temp = temp.replace(']', '')
        return temp

os.system('clear')
print('**************************************************')
print('   Press Ctrl + c, to exit program at any time.')
print('\n    Welcome to Martin Parker\'s lottery picker.\n')

while True:
    picked_numbers = []
    picked_star_picks = []
    global main_numbers
    main_numbers = []
    global star_numbers
    star_numbers = []
    try:
        os.system('clear')
        print('**************************************************')
        if goes >= 1:
            print('**************************************************')
            print('    SCROLL UP FOR NUMBERS IF YOU MISSED THEM')
            print('**************************************************')
        print('   Press Ctrl + c, to exit program at any time.')
        print('\n    Welcome to Martin Parker\'s lottery picker.\n')
        print('**************************************************')
        print('Please choose: 1= Health Lottery, 2= National Lottery, 3= Custom Raffle/Lottery.')
        get_lottery = int(input('\nSelect lottery?'))
        if get_lottery == 1:
            tickets = int(input('\nHow many tickets would you like? '))
            print('Generating your Health Lottery numbers...\n')
            for i in range(tickets):
                health = Lottery(1, 50, 5, False, 0, 0, 0)
                health.get_numbers(ticket = i + 1)
                if (i + 1) % 5 == 0:
                    print('')
                picked_numbers.clear()
        elif get_lottery == 2:
            print('\nPlease choose: 1=Lotto, 2=Thunderball, 3=Euromillions.')
            get_nl = int(input('Select ticket?'))
            if get_nl == 1:
                tickets = int(input('\nHow many tickets would you like? '))
                print('Generating your Lotto numbers...\n')
                for i in range(tickets):
                    lotto = Lottery(1, 59, 6, False, 0, 0, 0)
                    lotto.get_numbers(ticket = i + 1)
                    if (i + 1) % 5 == 0:
                        print('')
                    picked_numbers.clear()
            elif get_nl == 2:
                tickets = int(input('\nHow many tickets would you like? '))
                print('Generating your Thunderball numbers...\n')
                for i in range(tickets):
                    thunderball = Lottery(1, 39, 5, True, 1, 14, 1)
                    thunderball.get_numbers(ticket = i + 1)
                    thunderball.get_star_picks(info = 'Thunderball:')
                    if (i + 1) % 5 == 0:
                        print('')
                    picked_numbers.clear()
                    picked_star_picks.clear()
            elif get_nl == 3:
                tickets = int(input('\nHow many tickets would you like? '))
                print('Generating your Euromillions numbers...\n')
                for i in range(tickets):
                    euromillions = Lottery(1, 50, 5, True, 1, 12, 2)
                    euromillions.get_numbers(ticket = i + 1)
                    euromillions.get_star_picks(info = 'Lucky Stars:')
                    if (i + 1) % 5 == 0:
                        print('')
                    picked_numbers.clear()
                    picked_star_picks.clear()
        elif get_lottery == 3:
            custom_main_low = int(input('Please enter the main lowest number: '))
            custom_main_high = int(input('Please enter the main highest number: '))
            custom_main_picks = int(input('Please enter the amount of main numbers per draw: '))
            custom_stars_numbers = int(input('Please enter the amount of bonus numbers per draw (0=none): '))
            if custom_stars_numbers == 0:
                custom_stars = False
                custom_stars_low = 0
                custom_stars_high = 0
                pass
            else:
                custom_stars_low = int(input('Please enter the bonus lowest number: '))
                custom_stars_high = int(input('Please enter the bonus highest number: '))
                custom_stars = True
            tickets = int(input('\nHow many tickets would you like? '))
            print('Generating your numbers...\n')
            for i in range(tickets):
                custom = Lottery(custom_main_low, custom_main_high, custom_main_picks,
                                 custom_stars, custom_stars_low, custom_stars_high,
                                 custom_stars_numbers)
                custom.get_numbers(ticket = i + 1)
                if custom_stars == True:
                    custom.get_star_picks()
                    picked_star_picks.clear()
                    picked_numbers.clear()
                if (i + 1) % 5 == 0:
                    print('')
                picked_numbers.clear()
                picked_star_picks.clear()
        else:
            print('Invalid choice.')
            continue
    except ValueError:
        print('Invalid choice.')
    except KeyboardInterrupt:
        print('\nExiting script')
        sys.exit()
    print('\nGOOD LUCK!!!\n')
    goes += 1
    time.sleep(2)
