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


print('\n+++SEABATTLE+++\n\n')
game = 1
while game == 1:
    answer = input('\nStart game? (Y/N): ')
    if answer.upper() != 'Y' and answer.upper() != 'N':
        print('What?')
        continue
    elif answer.upper() == 'N':
        print('\nGoodbye...')
        break
    elif answer.upper() == 'Y':
        while True:
            print('\n************')
            print('* New game *')
            print('************')


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


# Show clean field
            num_x = 1
            print('\nFIELD')
            for i in field.result:
                print(num_x, i)
                num_x += 1

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


# Write fields in players storage
            field.write_field_to_storage_players(player1)
            field.write_field_to_storage_players(player2)


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
            if QUEUE == player1.queue:
                print('\nThe computer chose the player who will start first. It\'s -', player1.name)
            else:
                print('\nThe computer chose the player who will start first. It\'s -', player2.name)

# Create lists objects ships players / ЗАЧЕМ?
#             objects_ship1_player1 = [Ship(player1) for i in range(max_ships[0])]
#             objects_ship1_player2 = [Ship(player2) for i in range(max_ships[0])]
#             objects_ship2_player1 = [Ship(player1) for i in range(max_ships[1])]
#             objects_ship2_player2 = [Ship(player2) for i in range(max_ships[1])]
#             objects_ship3_player1 = [Ship(player1) for i in range(max_ships[2])]
#             objects_ship3_player2 = [Ship(player2) for i in range(max_ships[2])]
#             objects_ship4_player1 = [Ship(player1) for i in range(max_ships[3])]
#             objects_ship4_player2 = [Ship(player2) for i in range(max_ships[3])]


# Enter coordinates all single deck ships - []
            flag = 0
            while flag != 2:
                if QUEUE == 0:
                    player_obj = player1
                else:
                    player_obj = player2
                i = 1
                n = 1.0
                while i <= max_ships[0]:
                    print('\n', player_obj.name, ', enter coordinates single deck ship (1 cell)\n')
                    num_x = 1
                    for row in Storage.field_players[player_obj.queue]:  # Show map player1 with ship/s
                        print(num_x, row)
                        num_x += 1
                    ship_coo = user_input_coo_ship()
                    if isinstance(ship_coo, list):
                        if check_busy(ship_coo, player_obj) == 0:  # Check cell for busy
                            print('Place is busy! Enter coordinates again.')
                        else:
                            # Write map with single ships to player1 storage
                            Storage.field_players[player_obj.queue][ship_coo[0]][ship_coo[1]] = '[1]'
                            # objects_ship1_player1[i - 1].write_ship(n, ship_coo)  # Add ships in storage
                            print('\n', end='')
                            # num_y = [' * ' for i in range(len(Storage.field[0]))]
                            # print(' ', num_y)
                            num_x = 1
                            for row in Storage.field_players[player_obj.queue]:  # Show map player1 with ship/s
                                print(num_x, row)
                                num_x += 1
                            n += 0.1
                            n = round(n, 1)  # Округление
                            i += 1


# Enter coordinates all two deck ships - [][]
                i = 1
                n = 2.0
                while i <= max_ships[1]:
                    print('\n', player_obj.name, ', enter coordinates two deck ships (2 cell))')
                    print('Enter coordinates 1/2 ship')
                    ship_coo = user_input_coo_ship()
                    print('Enter coordinates 1/2 ship')
                    ship_coo2 = user_input_coo_ship()
                    if isinstance(ship_coo, list) and isinstance(ship_coo2, list):
                        if check_busy(ship_coo, player_obj) == 0 or\
                                check_busy(ship_coo2, player_obj) == 0:  # Check cell for busy
                            print('Cell is busy! Enter coo again.')
                            print('\n', end='')
                            for row in Storage.field_players[player_obj.queue]:  # Show map player1 with ship/s
                                print(row)
                        else:
                            if ship_connection_check([ship_coo, ship_coo2]) == 1:
                                print([ship_coo, ship_coo2])
                                # Write map with two ships to player1 storage
                                Storage.field_players[player_obj.queue][ship_coo[0]][ship_coo[1]] = '[2]'
                                Storage.field_players[player_obj.queue][ship_coo2[0]][ship_coo2[1]] = '[2]'
                                # objects_ship2_player1[i - 1].write_ship(n, [ship_coo, ship_coo2])  # Add ships in storage
                                print('\n', end='')
                                num_x = 1
                                for row in Storage.field_players[player_obj.queue]:  # Show map player1 with ship/s
                                    print(num_x, row)
                                    num_x += 1
                                n += 0.1
                                n = round(n, 1)  # Округление
                                i += 1
                            else:
                                print('Build ship error!')
                                print('\n', end='')
                                num_x = 1
                                for row in Storage.field_players[player_obj.queue]:  # Show map player1 with ship/s
                                    print(num_x, row)
                                    num_x += 1


# Enter coordinates all three deck ships - [][][]
                i = 1
                n = 3.0
                while i <= max_ships[2]:
                    print('\n', player_obj.name, ', enter coordinates three deck ships (3 cell))')
                    print('Enter coordinates 1/3 ship')
                    ship_coo = user_input_coo_ship()
                    print('Enter coordinates 1/3 ship')
                    ship_coo2 = user_input_coo_ship()
                    print('Enter coordinates 1/3 ship')
                    ship_coo3 = user_input_coo_ship()
                    if isinstance(ship_coo, list) and isinstance(ship_coo2, list) and isinstance(ship_coo3, list):
                        if check_busy(ship_coo, player_obj) == 0 or\
                                check_busy(ship_coo2, player_obj) == 0 or\
                                check_busy(ship_coo3, player_obj) == 0:  # Check cell for busy
                            print('Cell is busy! Enter coo again.')
                            print('\n', end='')
                            num_x = 1
                            for row in Storage.field_players[player_obj.queue]:  # Show map player1 with ship/s
                                print(num_x, row)
                                num_x += 1
                        else:
                            if ship_connection_check([ship_coo, ship_coo2, ship_coo3]) == 1:
                                print([ship_coo, ship_coo2, ship_coo3])
                                # Write map with two ships to player1 storage
                                Storage.field_players[player_obj.queue][ship_coo[0]][ship_coo[1]] = '[3]'
                                Storage.field_players[player_obj.queue][ship_coo2[0]][ship_coo2[1]] = '[3]'
                                Storage.field_players[player_obj.queue][ship_coo3[0]][ship_coo3[1]] = '[3]'
                                # Add ships in storage
                                # objects_ship2_player1[i - 1].write_ship(n, [ship_coo, ship_coo2, ship_coo3])
                                print('\n', end='')
                                num_x = 1
                                for row in Storage.field_players[player_obj.queue]:  # Show map player1 with ship/s
                                    print(num_x, row)
                                    num_x += 1
                                n += 0.1
                                n = round(n, 1)  # Округление
                                i += 1
                            else:
                                print('Build ship error!')
                                print('\n', end='')
                                num_x = 1
                                for row in Storage.field_players[player_obj.queue]:  # Show map player1 with ship/s
                                    print(num_x, row)
                                    num_x += 1


# Enter coordinates all four deck ships - [][][][]
                i = 1
                n = 4.0
                while i <= max_ships[3]:
                    print('\n', player_obj.name, ', enter coordinates four deck ships (3 cell))')
                    print('Enter coordinates 1/4 ship')
                    ship_coo = user_input_coo_ship()
                    print('Enter coordinates 1/4 ship')
                    ship_coo2 = user_input_coo_ship()
                    print('Enter coordinates 1/4 ship')
                    ship_coo3 = user_input_coo_ship()
                    print('Enter coordinates 1/4 ship')
                    ship_coo4 = user_input_coo_ship()
                    if isinstance(ship_coo, list) and\
                            isinstance(ship_coo2, list) and\
                            isinstance(ship_coo3, list) and\
                            isinstance(ship_coo4, list):
                        if check_busy(ship_coo, player_obj) == 0 or\
                                check_busy(ship_coo2, player_obj) == 0 or\
                                check_busy(ship_coo3, player_obj) == 0 or \
                                check_busy(ship_coo4, player_obj) == 0:  # Check cell for busy:  # Check cell for busy
                            print('Cell is busy! Enter coo again.')
                            print('\n', end='')
                            num_x = 1
                            for row in Storage.field_players[player_obj.queue]:  # Show map player1 with ship/s
                                print(num_x, row)
                                num_x += 1
                        else:
                            if ship_connection_check([ship_coo, ship_coo2, ship_coo3, ship_coo4]) == 1:
                                print([ship_coo, ship_coo2, ship_coo3, ship_coo4])
                                # Write map with two ships to player1 storage
                                Storage.field_players[player_obj.queue][ship_coo[0]][ship_coo[1]] = '[4]'
                                Storage.field_players[player_obj.queue][ship_coo2[0]][ship_coo2[1]] = '[4]'
                                Storage.field_players[player_obj.queue][ship_coo3[0]][ship_coo3[1]] = '[4]'
                                Storage.field_players[player_obj.queue][ship_coo4[0]][ship_coo3[1]] = '[4]'
                                # Add ships in storage
                                # objects_ship2_player1[i - 1].write_ship(n, [ship_coo, ship_coo2, ship_coo3, ship_coo4])
                                print('\n', end='')
                                num_x = 1
                                for row in Storage.field_players[player_obj.queue]:  # Show map player1 with ship/s
                                    print(num_x, row)
                                    num_x += 1
                                n += 0.1
                                n = round(n, 1)  # Округление
                                i += 1
                            else:
                                print('Build ship error!')
                                print('\n', end='')
                                num_x = 1
                                for row in Storage.field_players[player_obj.queue]:  # Show map player1 with ship/s
                                    print(num_x, row)
                                    num_x += 1
                                    # Второй проход цикла.
                                    flag += 1
                if QUEUE == 1:
                    QUEUE = 0
                elif QUEUE == 0:
                    QUEUE = 1


# Show player1 Storage
            print('\nNames:', Storage.players,
                  '\nFields player1:', Storage.field_players[player1.queue],
                  '\nFields player2:', Storage.field_players[player2.queue],
                  '\nShips player1', Storage.ships_player1,
                  '\nShots', Storage.shots_players, '\n')

            answer = input('Do you want start new game? (Y/N) ')
            if answer.upper() == 'Y':
                continue
            else:
                print('\nOk, goodbye...')
                game = 0
                break


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
