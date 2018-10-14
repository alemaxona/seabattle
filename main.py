__author__ = 'alemaxona'

''' 
main.py - Game logic
'''


from models import Field, Gamer, Ship, Storage
from user_input import user_input_coo_ship, user_input_coo_field


print('\n+++SEABATTLE+++')


# Select field size
print('\nEnter field size:')
while True:
    field_coo_x = input('\nX = ')
    field_coo_y = input('Y = ')
    field_coo = user_input_coo_field(field_coo_x, field_coo_y)
    if isinstance(field_coo, list):
        break


# Init player 1
input_player1 = input('\nEnter name player1: ')
player1 = Gamer(input_player1)
print('Welcome player', player1.name)

# Init player 2
input_player2 = input('\nEnter name player2: ')
if input_player1 == input_player2:
    input_player2 += '.2'
    player2 = Gamer(input_player2)
    print('Welcome player', player2.name)
else:
    player2 = Gamer(input_player2)
    print('Welcome player', player2.name)



# Show field
field = Field(field_coo[0], field_coo[1])
field.init_field()
########## ТУТ!
Storage.field_player1 = field.size.copy()
print('\n FIELD')
for i in field.size:
    print(i)


# Enter coordinates ship
print('\n', player1.name, ', please enter coordinates ship (1 cell)')
while True:
    ship_coo_x = input('\nX = ')
    ship_coo_y = input('Y = ')
    ship_coo = user_input_coo_ship(ship_coo_x, ship_coo_y)
    if isinstance(ship_coo, list):
        break

a = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
if Storage.field_player1 == a:
    print(True)
else:
    False
print(ship_coo)
Storage.field_player1[ship_coo[0]][ship_coo[1]] = '[]'
print(Storage.field_player1)

#
#
# ship_player1_once = Ship(1,[])
#
# print(Storage.field_player1)
# print(len(Storage.field_player1))
# print(field.size)
