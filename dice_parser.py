from random import randint
import argparse

def dice_roller(num_dice, num_sides, verbosity):
    dice_results = []
    for number_of_rolls in range(num_dice):
        dice_results.append(randint(1, num_sides))
    if verbosity == True:
        print(f'Individual Rolls: {dice_results}')
        print(f'Occurences in the dice rolls: {dict((key, dice_results.count(key)) for key in set(dice_results))}')
    print(f'Sum of all dice rolls: {sum(dice_results)}')

def get_dice_format():
    while True:
        user_input = input('Enter dice format <number of dice>d<how many sides>: ')

        if user_input in ['q', 'quit']:
            print('Afraid of some dice are ye?')
            exit()

        try:
            num_dice = int(user_input.split('d')[0])
            num_sides = int(user_input.split('d')[1])

            if num_sides > 0 and num_dice > 0:
                return num_dice, num_sides
            else:
                print('Please use positive and whole numbers only. \n')

        except IndexError:
            print('Follow the example: <number of dice>d<how many sides> \n')
        except ValueError:
            print('Please use positive and whole numbers only. \n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", help="increase output to show individual dice rolls and occurences", action="store_true")
    args = parser.parse_args()
    if args.verbosity:
        verbosity = True
    else:
        verbosity = False
    while True:
        num_dice, num_sides = get_dice_format()
        dice_roller(num_dice, num_sides, verbosity)

main()