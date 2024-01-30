import pattern
import playWithPC
import playWithPlayer


try:
    list_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print("""
--------------------------------------------------------------------------
	
                         Welcome to Tic-Tac-Toe Game
                         
--------------------------------------------------------------------------
	""")
    pattern.pattern(list_1)
    print("""


    Rules :-
         -----
         1. MAXIMUM OF 2 PLAYERS & MINIMUM OF 1 PLAYER CAN PLAY THIS GAME.
         2. EACH PLAYER HAVE TO CHOOSE BETWEEN TWO SIGNS : EITHER X OR O
         3. FIRST PLAYER WHO CAN MATCH HIS/HER RESPECTIVE SIGN DIAGONALLY, 
            HORIZONTALLY OR VERTICALLY IS THE WINNER.

         SO, LETS START THE GAME.....
	""")
    while (1):
        list_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        print("""
		PRESS 1 TO PLAY WITH PC.
		PRESS 2 TO PLAY WITH ANOTHER PLAYER.
		PRESS 3 TO QUIT.
		""")
        choice = (input(" CHOICE : "))
        if (choice == "1"):
            playWithPC.play_with_pc(list_1)
        elif (choice == "2"):
            playWithPlayer.play_with_player(list_1)
        elif (choice == "3"):
            break
        else:
            print("Invalid Choice.")


except Exception as e:
    print(type(e).__name__)
