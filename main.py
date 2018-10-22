__author__ = 'alemaxona'

''' 
main.py - Game logic
'''


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
player1.write_field_to_storage_players()
player2.write_field_to_storage_players()


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


# Show player1 Storage
print('\nNames:', Storage.players,
      '\nFields:', Storage.field_players,
      '\nShips', Storage.ship_player1,
      '\nShots', Storage.shots_players)


# ship1_player1 = Ship(ship_coo, n, player1)  # Сначала определить, потом добавлять!
# Enter coordinates all ships - []
print('\n', player1.name, ', enter coordinates ships (1 cell)')
i = 1
while i <= max_ships[0]:
        ship_coo = user_input_coo_ship()
        if isinstance(ship_coo, list):
            if check_busy(ship_coo, player1) == False:  # Check cell for busy
                print('Cell is busy! Enter coo again.')
            else:
                n = 1.0
                Storage.field_players[player1.queue][ship_coo[0]][ship_coo[1]] = '[]'  # Write map with ship(1 cell) in player1 storage
                ship1_player1 = Ship(ship_coo, n, player1)  # Init player1 ship(1cell)
                ship1_player1.write_ship()  # Write ship(1cell) in player1 storage
                n += 0.1
                i += 1

# Show player1 Storage
print('\nName:', Storage.players,
      '\nField:', Storage.field_players,
      '\nShips', Storage.ship_player1,
      '\nShots', Storage.shots_players)


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
                                i += 1
                        else:
                            pass
        else:
            print('Enter again!')


for i in Storage.field_players[player1.queue]:  # Show map player1 with ship/s
    print(i)


# Show player1 Storage
print('\nName:', Storage.players,
      '\nField:', Storage.field_players,
      '\nShips', Storage.ship_player1,
      '\nShots', Storage.shots_players)


'''All objects:'''

# player1
# player2

# field

# ship1_player1
# ship2_player1
