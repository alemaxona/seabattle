__author__ = 'alemaxona'

''' 
main.py - Game logic
'''


from models import Field, Player, Ship, Storage, check_busy, check_build_ship_logic
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


print('\n FIELD')  # Show clean field
for i in field.result:
    print(i)


Storage.field_player1 = field.result.copy()  # Write field in player1 storage


print('\n', player1.name, ', enter coordinates ship (1 cell)')  # Enter coordinates ship 1
while True:
    ship_coo = user_input_coo_ship()
    if isinstance(ship_coo, list):
        break


Storage.field_player1[ship_coo[0]][ship_coo[1]] = '[]'  # Write map with ship(1 cell) in player1 storage
ship1_player1 = Ship(ship_coo, 1)  # Init player1 ship(1cell)
ship1_player1.write_ship()  # Write ship(1cell) in player1 storage


for i in Storage.field_player1:  # Show map player1 with ship/s
    print(i)


# Enter coordinates ship 2
if len(Storage.field) >= 2:
    print('\n', player1.name, ', enter coordinates ship (2 cell)')
    while True:
        print('\nEnter 1 cell ship')
        ship_coo = user_input_coo_ship()
        if isinstance(ship_coo, list):
            if check_busy(ship_coo, 1) == False:  # Check cell for busy
                print('Cell is busy! Enter coo again.')
            else:
                # Write map with ship(1.2 cell) in player1 storage
                Storage.field_player1[ship_coo[0]][ship_coo[1]] = '[]'
                ship2_player1 = Ship(ship_coo, 2)  # Init player1 ship(1cell)
                # ship2_player1.write_ship()  # Write ship(2.1cell) in player1 storage
                flag = 0
                while flag == 0:
                    print('\nEnter 2 cell ship')
                    ship_coo = user_input_coo_ship()
                    if check_busy(ship_coo, 1) == False:  # Check cell for busy
                        print('Cell is busy! Enter coo again.')
                    else:
                        if check_build_ship_logic(ship_coo, 2, 2) == False:
                            print('Ship is not build! Enter again!')
                        else:
                            if isinstance(ship_coo, list):
                                # Add ship(2.2cell) in player1 storage
                                ship2_player1.size[2].append([ship_coo[0], ship_coo[1]])
                                # Write map with ship(2.2 cell) in player1 storage
                                Storage.field_player1[ship_coo[0]][ship_coo[1]] = '[]'
                                break
        else:
            print('Enter again!')


for i in Storage.field_player1:  # Show map player1 with ship/s
    print(i)


# Show player1 Storage
print('\nName:', Storage.players[1],
      '\nField:', Storage.field_player1,
      '\nShips', Storage.ship_player1,
      '\nShots', Storage.shot_player1)


'''All objects:'''

# player1
# player2

# field

# ship1_player1
# ship2_player1