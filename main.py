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


# Show clean field
field = Field(field_coo[0], field_coo[1])
field.init_field()
Storage.field_player1 = field.result.copy()
print('\n FIELD')
for i in field.result:
    print(i)


# Enter coordinates ship 1
print('\n', player1.name, ', enter coordinates ship (1 cell)')
while True:
    ship_coo_x = input('\nX = ')
    ship_coo_y = input('Y = ')
    ship_coo = user_input_coo_ship(ship_coo_x, ship_coo_y)
    if isinstance(ship_coo, list):
        break


# Write map with ship(1 cell) in storage
print(ship_coo)
print(Storage.field_player1)
print('rows len',len(Storage.field_player1))
print('col len',len(Storage.field_player1[0]))
Storage.field_player1[ship_coo[0]][ship_coo[1]] = '[]'
for i in Storage.field_player1:
    print(i)


# Enter coordinates ship 2
if len(Storage.field_player1) >= 2:
    print('\n', player1.name, ', enter coordinates ship (2 cell)')
    while True:
        print('\n Enter 1 cell ship')
        ship_coo_x1 = input('X = ')
        ship_coo_y1 = input('Y = ')
        ship_coo = user_input_coo_ship(ship_coo_x1, ship_coo_y1)
        if isinstance(ship_coo, list):
            print('\n Enter 2 cell ship')
            ship_coo_x2 = input('X = ')
            ship_coo_y2 = input('Y = ')
            ship_coo_2 = user_input_coo_ship(ship_coo_x2, ship_coo_y2)
            if isinstance(ship_coo_2, list):
                if ship_coo_2[0]:
                    # !
                    break

# Write map with ship(2 cell) in storage
Storage.field_player1[ship_coo[0]][ship_coo[1]] = '[]'
Storage.field_player1[ship_coo_2[0]][ship_coo_2[1]] = '[]'
for i in Storage.field_player1:
    print(i)