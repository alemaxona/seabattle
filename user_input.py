__author__ = 'alemaxona'

'''
user_input.py - Functions inputs users
'''

from models import Storage


def user_input_coo_field(value1, value2):
    while True:
        try:
            coo_x = int(value1)
            coo_y = int(value2)
            if int(coo_x) < 3:
                print('Enter number X > 3')
                break
            elif int(coo_y) <= 0:
                print('Enter number Y > 0')
                break
            else:
                value3 = [coo_x, coo_y]
                return value3
        except ValueError:
            print('Enter only numbers')
            break


def user_input_coo_ship(value1, value2):
    while True:
        try:
            coo_x = int(value1)
            coo_y = int(value2)
            if int(coo_x) <= 0:
                print('Enter number X > 0')
                break
            elif int(coo_y) <= 0:
                print('Enter number Y > 0')
                break
            elif int(coo_x) > len(Storage.field_player1[0]):
                print('Enter number X <', len(Storage.field_player1[0]))
                break
            elif int(coo_y) > len(Storage.field_player1):
                print('Enter number Y <', len(Storage.field_player1))
                break
            else:
                value3 = [(coo_x - 1), (coo_y - 1)]
                return value3
        except ValueError:
            print('Enter only numbers')
            break