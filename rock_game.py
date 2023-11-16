import re
import sys
import time
import random

"""Command line Python game - Rock, Paper, Scissors, Lizard, Spock
"""


def computer_choice():
    """Function to select a random choice from array of string values

    Returns:
        str: String representation of number value (1, 2, 3, 4, 5)
    """
    
    options = ['1', '2', '3', '4', '5']
    computer = random.choice(options)
    return computer


def option_graphic(choice):
    """Function to return ASCII art image based on user/computer choice

    Args:
        choice (str): String representation of number value (1, 2, 3, 4, 5) selected by user/computer
    """
    
    if choice == '1':
        rock = "         _____    ____    _____  _  __\n\
        |  __ \  / __ \  / ____|| |/ /\n\
        | |__) || |  | || |     | ' / \n\
        |  _  / | |  | || |     |  <  \n\
        | | \ \ | |__| || |____ | . \ \n\
        |_|  \_\ \____/  \_____||_|\_\ "
        print(rock)
    elif choice == '2':
        paper = "         _____          _____   ______  _____ \n\
        |  __ \  /\    |  __ \ |  ____||  __ \ \n\
        | |__) |/  \   | |__) || |__   | |__) | \n\
        |  ___// /\ \  |  ___/ |  __|  |  _  / \n\
        | |   / ____ \ | |     | |____ | | \ \ \n\
        |_|  /_/    \_\|_|     |______||_|  \_\ "
        print(paper)
    elif choice == '3':
        scissors = "         _____   _____  _____   _____  _____   ____   _____    _____ \n\
        / ____| / ____||_   _| / ____|/ ____| / __ \ |  __ \  / ____| \n\
        | (___  | |       | |  | (___ | (___  | |  | || |__) || (___  \n\
        \___ \ | |       | |   \___ \ \___ \ | |  | ||  _  /  \___ \ \n\
        ____) || |____  _| |_  ____) |____) || |__| || | \ \  ____) | \n\
        |_____/  \_____||_____||_____/|_____/  \____/ |_|  \_\|_____/  "
        print(scissors)
    elif choice == '4':
        lizard = "         _       _____  ______           _____   _____\n\
        | |     |_   _||___  /    /\    |  __ \ |  __ \ \n\
        | |       | |     / /    /  \   | |__) || |  | | \n\
        | |       | |    / /    / /\ \  |  _  / | |  | | \n\
        | |____  _| |_  / /__  / ____ \ | | \ \ | |__| | \n\
        |______||_____|/_____|/_/    \_\|_|  \_\|_____/ "
        print(lizard)
    elif choice == '5':
        spock = "          _____  _____    ____    _____  _  __ \n\
         / ____||  __ \  / __ \  / ____|| |/ / \n\
        | (___  | |__) || |  | || |     | ' / \n\
         \___ \ |  ___/ | |  | || |     |  <  \n\
         ____) || |     | |__| || |____ | . \ \n\
        |_____/ |_|      \____/  \_____||_|\_\ "
        print(spock)


def game_winner(selection, computer):
    """Function to determine game winner based on user and computer selected options

    Args:
        selection (str): String representation of number value (1, 2, 3, 4, 5) selected by user
        computer (str): String representation of number value (1, 2, 3, 4, 5) randomly
            selected for computer by computer_choice function

    Returns:
        str: String of 'user' or 'computer' winner based on array of winning choice combinations
    """
    
    if selection == computer:
        return 'draw'
    else:
        user_wins = ['13', '14', '21', '25', '32', '34', '42', '45', '52', '53']
        combo = selection + computer

        if combo in user_wins:
            return 'user'
        else:
            return 'computer'


def return_to_menu():
    """Function to return to main menu
    """

    input('Press "Enter" key to return to the game menu.')
    game_menu()


def exit_game():
    """Function to exit program
    """
    print('Exiting...')
    time.sleep(1)
    sys.exit()


def game_menu():
    """Main menu function to initiate game play and display winner
    """
    
    print("Let's Play a Game: \n1: Rock \n2: Paper \n3: Scissors \n4: Lizard \n5: Spock \n6: Exit")
    selection = input('Enter selection number: ')

    pattern = r'[1-6]'
    check_input = re.findall(pattern, selection)

    while not check_input:
        selection = input('Enter valid selection number: ')
        check_input = re.findall(pattern, selection)

    if selection == '6':
        exit_game()
    else:
        option_graphic(selection)

        vs = "        __      __ _____ \n\
        \ \    / // ____| \n\
         \ \  / /| (___  \n\
          \ \/ /  \___ \ \n\
           \  /   ____) | \n\
            \/   |_____/  "
        print(vs)

        computer = computer_choice()
        option_graphic(computer)

        winner = game_winner(selection, computer)
        if winner == 'user':
            print('\nYou are the winner!\n')
        elif winner == 'computer':
            print('\nSorry, you lost. Please try again.\n')
        elif winner == 'draw':
            print('\nMatch is a draw. Please try again.\n')

        return_to_menu()


if __name__ == "__main__":
    game_menu()
