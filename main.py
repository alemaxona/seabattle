__author__ = 'alemaxona'

''' 
main.py - Game logic
'''

from random import randint
from models import Field, Player, Ship, Storage, \
    check_busy, \
    check_build_ship_logic, \
    check_max_ships_for_field
from user_input import user_input_coo_ship, user_input_coo_field


print('\n+++SEABATTLE+++')


# Init player1
player1 = Player(input('\nEnter name player1: '), 0)
print('Welcome player', player1.name)


# Init player2
player2 = Player(input('\nEnter name player2: '), 1)
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
field = Field(field_coo)
field.init_field()
field.write_field_to_storage()


# Write fields in players storage
field.write_field_to_storage_players(player1)
field.write_field_to_storage_players(player2)


# Show clean field
print('\nFIELD')
for i in field.result:
    print(i)


# Show max number of ships for this field
max_ships = check_max_ships_for_field()
print('\nMaximum ships: '
      '\nSingle deck ship -', max_ships[0],
      '\nTwo deck ship -', max_ships[1],
      '\nThree deck ship -', max_ships[2],
      '\nFour deck ship -', max_ships[3])


# Random chose queue players!
# QUEUE = randint(player1.queue, player2.queue)
# print('QUEUE -', QUEUE)


# Create lists objects ships1 players
objects_ship1_player1 = [Ship(player1) for i in range(max_ships[0])]
objects_ship1_player2 = [Ship(player1) for i in range(max_ships[0])]


# Enter coordinates all ships - []
print('\n', player1.name, ', enter coordinates ships (1 cell)')
i = 1
n = 1.0
while i <= max_ships[0]:
        ship_coo = user_input_coo_ship()
        if isinstance(ship_coo, list):
            if check_busy(ship_coo, player1) == False:  # Check cell for busy
                print('Cell is busy! Enter coo again.')
            else:
              # -->  Storage.field_players[player1.queue][ship_coo[0]][ship_coo[1]] = '[]'  # Write map with ship(1 cell) in player1 storage
                objects_ship1_player1[i - 1].write_ship(n, ship_coo)  # Add ships in storage
                n += 0.1
                n = round(n, 1)  # Округление
                i += 1


# Show player1 Storage
print('\nNames:', Storage.players,
      '\nFields player1:', Storage.field_players[player1.queue],
      '\nFields player2:', Storage.field_players[player2.queue],
      '\nShips player1', Storage.ships_player1,
      '\nShots', Storage.shots_players, '\n')


for i in Storage.field_players[player1.queue]:  # Show map player1 with ship/s
    print(i)


# Enter coordinates all ship - [][]
i = 1
while i <= max_ships[1]:
    print('\n\n', player1.name, ', enter coordinates ship (2 cell)')
    while True:
        print('\nEnter 1 cell ship')
        ship_coo = user_input_coo_ship()
        if isinstance(ship_coo, list):
            if check_busy(ship_coo, 1) == False:  # Check cell for busy
                print('Cell is busy! Enter coo again.')
            else:
                # Write map with ship(1.2 cell) in player1 storage
                Storage.field_player1[ship_coo[0]][ship_coo[1]] = '[]'
                n = 2.0
                ship2_player1 = Ship(ship_coo, n)  # Init player1 ship(1cell)
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
                            if isinstance(ship_coo, list):
                                # Add ship(2.2cell) in player1 storage
                                ship2_player1.size[2].append([ship_coo[0], ship_coo[1]])
                                # Write map with ship(2.2 cell) in player1 storage
                                Storage.field_player1[ship_coo[0]][ship_coo[1]] = '[]'
                                n += 0.1
                                n = round(n, 1)  # Округление дробного числа
                                i += 1
                        else:
                            pass
        else:
            print('Enter again!')


for i in Storage.field_players[player1.queue]:  # Show map player1 with ship/s
    print(i)


'''All objects:'''

# player1
# player2

# field

# ships1_player1
# ship2_player1
