__author__ = 'alemaxona'

"""
user_input.py - Functions inputs users 
"""

from models import Storage


def user_input_coo_field():
    while True:
        try:
            x = input('X = ')
            y = input('Y = ')
            coo_x = int(x)
            coo_y = int(y)
            if int(coo_x) < 3:
                print('Enter number X > 3')
                break
            elif int(coo_x) > 10:
                print('Max field size - 10x10.')
                break
            elif int(coo_y) <= 0:
                print('Enter number Y > 0')
                break
            elif int(coo_y) > 10:
                print('Max field size - 10x10.')
                break
            else:
                value3 = [coo_x, coo_y]
                return value3
        except ValueError:
            print('Enter only numbers')
            break


def user_input_coo_ship():
    while True:
        try:
            x = input('\nX = ')
            y = input('Y = ')
            coo_x = int(x)
            coo_y = int(y)
            if int(coo_x) <= 0:
                print('Enter number X > 0')
                break
            elif int(coo_y) <= 0:
                print('Enter number Y > 0')
                break
            elif int(coo_x - 1) >= len(Storage.field):
                print('Enter number X < or =', len(Storage.field))
                break
            elif int(coo_y) > len(Storage.field[0]):
                print('Enter number Y < or =', len(Storage.field[0]))
                break
            else:
                value3 = [(coo_x - 1), (coo_y - 1)]
                return value3
        except ValueError:
            print('Enter only numbers')
            break