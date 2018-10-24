__author__ = 'alemaxona'

''' 
main.py - Game logic
'''

from random import randint
from models import Field, Player, Ship, Storage, \
    check_busy, \
    check_max_ships_for_field, \
    ship_connection_check
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
print('\nMaximum ships for this field size: '
      '\nSingle deck ship -', max_ships[0])
if max_ships[1] != 0:
    print('Two deck ship -', max_ships[1])
if max_ships[2] != 0:
    print('Three deck ship -', max_ships[2])
if max_ships[3] != 0:
    print('Four deck ship -', max_ships[3])


# Random chose queue players!
QUEUE = randint(player1.queue, player2.queue)


# Create lists objects ships players / ЗАЧЕМ?
objects_ship1_player1 = [Ship(player1) for i in range(max_ships[0])]
objects_ship1_player2 = [Ship(player2) for i in range(max_ships[0])]
objects_ship2_player1 = [Ship(player1) for i in range(max_ships[1])]
objects_ship2_player2 = [Ship(player2) for i in range(max_ships[1])]
objects_ship3_player1 = [Ship(player1) for i in range(max_ships[2])]
objects_ship3_player2 = [Ship(player2) for i in range(max_ships[2])]
objects_ship4_player1 = [Ship(player1) for i in range(max_ships[3])]
objects_ship4_player2 = [Ship(player2) for i in range(max_ships[3])]


# Enter coordinates all single deck ships - []
i = 1
n = 1.0
while i <= max_ships[0]:
    print('\n', player1.name, ', enter coordinates single deck ship (1 cell)')
    ship_coo = user_input_coo_ship()
    if isinstance(ship_coo, list):
        if check_busy(ship_coo, player1) == 0:  # Check cell for busy
            print('Place is busy! Enter coordinates again.')
        else:
            # Write map with single ships to player1 storage
            Storage.field_players[player1.queue][ship_coo[0]][ship_coo[1]] = '[1]'
            objects_ship1_player1[i - 1].write_ship(n, ship_coo)  # Add ships in storage
            print('\n', end='')
            for row in Storage.field_players[player1.queue]:  # Show map player1 with ship/s
                print(row)
            n += 0.1
            n = round(n, 1)  # Округление
            i += 1


# Enter coordinates all two deck ships - [][]
i = 1
n = 2.0
while i <= max_ships[1]:
    print('\n', player1.name, ', enter coordinates two deck ships (2 cell))')
    print('Enter coordinates 1/2 ship')
    ship_coo = user_input_coo_ship()
    ship_coo2 = user_input_coo_ship()
    if isinstance(ship_coo, list) and isinstance(ship_coo2, list):
        if check_busy(ship_coo, player1) == 0 and check_busy(ship_coo2, player1) == 0:  # Check cell for busy
            print('Cell is busy! Enter coo again.')
            print('\n', end='')
            for row in Storage.field_players[player1.queue]:  # Show map player1 with ship/s
                print(row)
        else:
            if ship_connection_check([ship_coo, ship_coo2]) == 1:
                print([ship_coo, ship_coo2])
                # Write map with two ships to player1 storage
                Storage.field_players[player1.queue][ship_coo[0]][ship_coo[1]] = '[2]'
                Storage.field_players[player1.queue][ship_coo2[0]][ship_coo2[1]] = '[2]'
                objects_ship2_player1[i - 1].write_ship(n, [ship_coo, ship_coo2])  # Add ships in storage
                print('\n', end='')
                for row in Storage.field_players[player1.queue]:  # Show map player1 with ship/s
                    print(row)
                n += 0.1
                n = round(n, 1)  # Округление
                i += 1
            else:
                print('Build ship error!')
                print('\n', end='')
                for row in Storage.field_players[player1.queue]:  # Show map player1 with ship/s
                    print(row)

# Show player1 Storage
print('\nNames:', Storage.players,
      '\nFields player1:', Storage.field_players[player1.queue],
      '\nFields player2:', Storage.field_players[player2.queue],
      '\nShips player1', Storage.ships_player1,
      '\nShots', Storage.shots_players, '\n')


'''All objects:'''

# player1
# player2

# field

# objects_ship1_player1
# objects_ship1_player2
# objects_ship2_player1
# objects_ship2_player2
# objects_ship3_player1
# objects_ship3_player2
# objects_ship4_player1
# objects_ship4_player2
