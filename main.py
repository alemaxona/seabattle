__author__ = 'alemaxona'

''' 
main.py - Game logic
'''


from models import Field, Player, Ship, Storage
from user_input import user_input_coo_ship, user_input_coo_field


print('\n+++SEABATTLE+++')


# Init player 1
player1 = Player(input('\nEnter name player1: '), 1)
print('Welcome player', player1.name)


# Init player 2
player2 = Player(input('\nEnter name player2: '), 2)
if player2.name == player1.name:
    player2.name = player2.name + '.2'
    print('Welcome player', player2.name)
else:
    print('Welcome player', player2.name)


# Select field size
print('\nEnter field size:')
while True:
    field_coo = user_input_coo_field()
    if isinstance(field_coo, list):
        break


# Init field and write field in storage
field = Field(field_coo[0], field_coo[1])
field.init_field()
Storage.field = field.result.copy()


# Show clean field
print('\n FIELD')
for i in field.result:
    print(i)


# Write field in player1 storage
Storage.field_player1 = field.result.copy()


# Enter coordinates ship 1
print('\n', player1.name, ', enter coordinates ship (1 cell)')
while True:
    ship_coo = user_input_coo_ship()
    if isinstance(ship_coo, list):
        break


# Write map with ship(1 cell) in storage
Storage.field_player1[ship_coo[0]][ship_coo[1]] = '[]'


# Write ship(1cell) in storage
ship1_player1 = Ship(ship_coo, 1)


# Show map player1 with ship/s
for i in Storage.field_player1:
    print(i)

# Show Storage
# print('\nName:', Storage.player1,
#       '\nField:', Storage.field_player1,
#       '\nShips', Storage.ship_player1,
#       '\nShots', Storage.shot_player1)


# # Enter coordinates ship 2
# if len(Storage.field_player1) >= 2:
#     print('\n', player1.name, ', enter coordinates ship (2 cell)')
#     while True:
#         print('\n Enter 1 cell ship')
#         ship_coo_x1 = input('X = ')
#         ship_coo_y1 = input('Y = ')
#         ship_coo = user_input_coo_ship(ship_coo_x1, ship_coo_y1)
#         if isinstance(ship_coo, list):
#             print('\n Enter 2 cell ship')
#             ship_coo_x2 = input('X = ')
#             ship_coo_y2 = input('Y = ')
#             ship_coo_2 = user_input_coo_ship(ship_coo_x2, ship_coo_y2)
#             # if
#             if isinstance(ship_coo_2, list):
#                 if ship_coo_2[0]:
#                     # !
#                     break
#
# # Write map with ship(2 cell) in storage
# Storage.field_player1[ship_coo[0]][ship_coo[1]] = '[]'
# Storage.field_player1[ship_coo_2[0]][ship_coo_2[1]] = '[]'
# for i in Storage.field_player1:
#     print(i)