""" 
test.py contains various tests for the functions in functions.py
"""

import functions    #import functions modules

print('Test display_board()')
test_board = ['#','O','O','O','X','O','X','O','X','O']
functions.display_board(test_board)

print('Test display_guide()')
functions.display_guide()

print('Test choose_marker()')
functions.choose_marker()

print('Test player2_marker()')
functions.player2_marker('X')

print('Test place_marker()')
functions.place_marker(test_board, 'X',1)
functions.display_board(test_board)

print('Test choose_first()')
functions.choose_first()

print('Test space_check()')
functions.space_check(test_board, 2)

print('Test full_board_check()')
functions.full_board_check(test_board)

print('Test choose_position()')
functions.choose_position(test_board)

print('Test win_check()')
functions.win_check(test_board, 'X')

print('Test replay()')
functions.replay()

print('Test count_down()')
functions.count_down(10)
