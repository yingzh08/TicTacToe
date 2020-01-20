"""
main.py contains the main program that runs the tic tac toe game
"""
import functions
import time

while True:
    #----------------------------- Set up the game ----------------------------------
    
    print('Welcome to Tic Tac Toe!')
    time.sleep(1)
    
    ###*************************************************###
    ### STEP 1: ASSIGN PLAYER 1'S AND PLAYER 2'S MARKERS ###
    ###*************************************************###
    d_plyr_marker = {'Player 1':'', 'Player 2':''} #Create a player to marker dictionary
    
    d_plyr_marker['Player 1'] = functions.choose_marker() #Ask for player 1's marker
    time.sleep(1)
    
    d_plyr_marker['Player 2'] = functions.player2_marker(d_plyr_marker['Player 1']) #Return player 2's marker
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
    
    if input('Are you ready to play? Enter Yes or No:')=='Yes':
        game_on = True
    else:
        game_on = False
        continue
    
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
                break
            
            if functions.full_board_check(gameboard)==True:
                print('Game Over. It is a tie!')
                break
                
            # Player2's turn.
            print (f'{second_plyr} (marker {d_plyr_marker[second_plyr]}):')
            new_position = functions.choose_position(gameboard)
            functions.place_marker(gameboard,d_plyr_marker[second_plyr],new_position)
            functions.display_board(gameboard)
           
            
            #Break out of the loop if player 1 wins
            if functions.win_check(gameboard,d_plyr_marker[second_plyr])==True:
                print(f'Game Over. {second_plyr} (marker:{d_plyr_marker[second_plyr]}) won!')
                break
            
    
        break
    break
    
    #if not replay():
        #break
        
    