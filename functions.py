"""
functions.py stores all functions used in the main.py program. 
"""

def display_board(board):
    '''Takes in board's content (list) and prints the board in a 3 by 3 grid.
    

    Parameters
    --------
    board: list len()=10
        Current game board. Length of the board must be 10

        Example:
        test_board = ['#','O','O','O','X','O','X','O','X','O']

    '''
    print('\n'*100)             #scrolls the previous board up out of view
    print(f' {board[1]} | {board[2]} | {board[3]} \
          \n---|---|---\
          \n {board[4]} | {board[5]} | {board[6]}\
          \n---|---|---\
          \n {board[7]} | {board[8]} | {board[9]}')
    
    #use \ as line breaks for python code

def display_guide():
    '''Print board position in 3x3 grid
    
    '''
    print('Board Guide:\n')
    print(' 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ')

def choose_marker():    #player_input()
    '''Asks player 1 to input a marker (X or O)

    If the user provided neither, continue asking. 


    Returns
    --------
    string
        Player 1's marker
    '''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Please choose marker: X or O?')
    else:
        print(f'Player 1: Your marker is {marker}')
        return marker

def player2_marker(marker):
    '''Takes in player 1's marker and automatically returns
    marker for player 2


    Parameters
    --------
    marker: str
        Player 1's marker
    

    Returns
    --------
    string
        Player 2's marker
    '''
    markerset = {'X','O'}
    marker2 = markerset - set(marker)
    marker2 = ''.join(marker2)
    print('Player 2: Your marker is '+ marker2)
    return (marker2)

def place_marker(board, marker, position):
    '''Takes board, player's marker, and a desire position and returns
    a board list with the player's marker placed at the user-defined position.


    Parameters
    ---------
    board: list
        Current game board. Length of the board must be 10.
    marker: str
        Player's marker (either 'X' or 'O')
    position: int
        Player's desired position
    

    Returns
    ---------
    list
        Updated game board list
    '''
    board[position] = marker

def choose_first():
    ''' randomly select a marker to go first
    

    Returns
    --------
    string
        marker that goes first ('X' or 'O')
    '''
    import random
    marker_list=['X','O']
    random_index=random.randint(0,1)
    return marker_list[random_index]

def space_check(board, position):
    '''Return TRUE if the position(parameter) is available on the board(parameter)


    Parameters
    --------
    board: list
        Current game board. Length must be 10
    position: int
        Position under inquiry
    

    Returns
    --------
    boolean
        TRUE if position is available.
        FALSE if position is filled.
    '''
    return board[position]==' '

def full_board_check(board):
    '''Returns TRUE if the board(parameter) is full. Returns FALSE otherwise.


    Parameters
    --------
    board: list
        Current game board. Length must be 10.
    

    Returns
    --------
    boolean
        TRUE if board is filled. FALSE otherwise
    '''
    return ' ' not in board[1:]

def choose_position(board):
    '''Asks user for next position. If position is empty, return that position.

    If user provided invalid position, such as letters or numbers outside 
    of the range of the board, print error message and continue to prompt 
    for user input.


    Parameters
    --------
    position: int
        input() from user
    

    Returns
    --------
    integer
        next position
    '''
    while True:
        try: 
            nextposition = int(input("ENTER position: (1-9)"))
            while space_check(board,nextposition) == False\
            or nextposition == 0:
                print(f'Position {nextposition} is not empty. Please choose again')
                nextposition = int(input("ENTER position: (1-9)"))
            else:
                return nextposition
        except ValueError:
            print('Please check your input and try again.')
        except IndexError:
            print(f'Please enter a number between 1 and {len(board)-1}')

def win_check(board, marker):
    '''Return TRUE if marker(parameter) in the current game board(parameter) has won.


    Parameters
    -------
    board: list
        Current game board. Length must be 10
    marker: str
        Marker being checked for winning

    
    Returns
    --------
    boolean
        TRUE if Marker has won. False otherwise
    '''
    # Get the index when given marker first appeared on the board
    first_marker_index = board.index(marker)

    # Marker at position 1; three ways to win
    if first_marker_index == 1:
        if board[1:4] == [marker]*3\
            or board[1] == board[4] == board[7] == marker\
                or board[1] == board[5] == board[9] == marker:
                return True
        else:
            return False
    
    # Marker at position 2; one way to win 
    elif first_marker_index == 2:
        if board[2] == board[5] == board[8] == marker:
            return True
        else:
            return False
    
    # Marker at position 3; two ways to win
    elif first_marker_index == 3:
        if board[3] == board[6] == board[9] == marker\
            or board[3] == board[5] == board[7] == marker:
            return True
        else:
            return False
    
    # Marker at position 4; one way to win
    elif first_marker_index == 4:
        if board[4] == board[5] == board[6] == marker:
            return True
        else:
            return False
    
    # Marker at position 7; one way to win
    elif first_marker_index == 7:
        if board[7] == board[8] == board[9] == marker:
            return True
        else:
            return False

    # Marker first appeared at any other positions. No chance of winning.

def replay():
    ''' Ask whether to replay the game. Return TRUE if yes, FALSE if no. 


    Parameters
    --------
    input(): str
        yes or no

    
    Returns
    --------
    boolean
        TRUE if yes, FALSE if no
    '''
    choice = input('Replay? (Yes or No)')
    while choice != 'Yes' and choice != 'No':
        print('Please choose between Yes or No only')
        choice = input('Replay? (Yes or No)')
    else:
        return choice == 'Yes'

def count_down(seconds):
    '''Prints a single-line count-down timer that counts down from () seconds.


    Parameters
    --------
    seconds: int
        time (in seconds) to count down from
    '''
    import sys
    import time

    cnt = seconds + 1
    while 1 <= cnt:
        cnt -= 1
        sys.stdout.write('\r' + 'Timer: ' + str(cnt) + ' seconds' + ' '*10) 
        # ' '*10 is used to wipe out text of various length
        time.sleep(1)
        if cnt < 1:
            break
    sys.stdout.write('\r' + ' '*20)     #Once count down complete, wipe out all text