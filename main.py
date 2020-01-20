"""
main.py contains the main program that runs the tic tac toe game
"""
import functions
import time

print('Welcome to Tic Tac Toe!')
time.sleep(1)

keep_play = True
while keep_play==True:
    #----------------------------- Set up the game ----------------------------------
    
    ###*************************************************###
    ### STEP 1: ASSIGN PLAYER 1'S AND PLAYER 2'S MARKERS ###
    ###*************************************************###
    d_plyr_marker = {'Player 1':'', 'Player 2':''} #Create a player to marker dictionary
    
    player1_marker, player2_marker = functions.choose_marker() #tuple unpacking

    d_plyr_marker['Player 1'] = player1_marker #assign player 1's marker
    time.sleep(1)
    
    d_plyr_marker['Player 2'] = player2_marker #assign player 2's marker
    time.sleep(1)
    
    #**Checker**#
    #print('This is a checker: Player-Marker dictionary looks like ' + str(d_plyr_marker))
    
    ###**********************************###
    ### STEP 2: DETERMINE WHO GOES FIRST ###
    ###**********************************###
    selected_marker= functions.choose_first() #Random draw of the first marker
    for plyr,marker in d_plyr_marker.items():
        if marker==selected_marker:
            first_plyr = plyr
            print(f'{first_plyr} will go first')
            time.sleep(1)
        else:
            second_plyr = plyr
            
            #**Checker**#
            #print('This is a checker: Marker of the player that goes first is ' + marker)
            #print('This is a checker: The second player is ' + second_plyr)
    
    ###***************************###
    ### STEP 3: PRINT BOARD GUIDE ###
    ###***************************###       
    print('\n')
    functions.display_guide()
    print('\nPlease remember the board guide') 
    functions.count_down(1)
    
    ###************************###
    ### STEP 4: READY TO PLAY? ###
    ###************************###
    game_on = False
    while game_on == False:
        ready = input('Are you ready to play? Enter Yes or No:')
        if ready =='Yes':
            game_on = True
            break

        
    
    #**Checker**#
    #print (game_on)
    
      
    #---------------------------------- Game On ------------------------------------
    while game_on==True:
        
        
        ###***************************###
        ### STEP 2: PRINT EMPTY BOARD ###
        ###***************************###
        
        gameboard = ['#']+[' ']*9 #Create empty board
        print('GAME STARTS!\n')
        functions.display_board(gameboard) #Print empty board
        print('\n')
        
        ###**************************###
        ### STEP 3: GAME PLAY STARTS ###
        ###**************************###

        while functions.full_board_check(gameboard) == False:
            
            #Player 1 Turn
            
            #Ask for next position
            print(f'{first_plyr} (marker {d_plyr_marker[first_plyr]}):')
            new_position = functions.choose_position(gameboard)
            functions.place_marker(gameboard,d_plyr_marker[first_plyr],new_position)
            functions.display_board(gameboard)
            
            
            #Break out of the loop if player 1 wins
            if functions.win_check(gameboard,d_plyr_marker[first_plyr])==True:
                print(f'Game Over. {first_plyr} (marker:{d_plyr_marker[first_plyr]}) won!')
                game_on=False
                break

                
            # Chec
            if functions.full_board_check(gameboard)==True:
                print('Game Over. It is a tie!')
                game_on=False
                break

                
            # Player2's turn.
            print (f'{second_plyr} (marker {d_plyr_marker[second_plyr]}):')
            new_position = functions.choose_position(gameboard)
            functions.place_marker(gameboard,d_plyr_marker[second_plyr],new_position)
            functions.display_board(gameboard)
           
            
            #Break out of the loop if player 2 wins
            if functions.win_check(gameboard,d_plyr_marker[second_plyr])==True:
                print(f'Game Over. {second_plyr} (marker:{d_plyr_marker[second_plyr]}) won!')
                game_on=False
                break

        break

    keep_play = functions.replay()   #Break the loop if the user choose not to keep playing
    
    
print('Thank you for playing! Hope to see you again!')
        
    