from random import randint


"""This is my funtions section"""

def battleship_small():

    player_wins = []
    computer_wins = []


    def scores(p,c):
        player_wins.append(p)
        computer_wins.append(c)

    def print_board(board):
        for row in board:
            print " ".join(row)

    while True:
        board = []
        for x in range(5):
            board.append(["O"] * 5)

        print
        print "Okay, let's play Battleship!"
        print
        print_board(board)
        print
        print "You get 5 turns to sink my battleship. Good luck."
        print

        def random_row(board):
            return randint(0, len(board) - 1)

        def random_col(board):
            return randint(0, len(board) - 1)

        ship_row = random_row(board)
        ship_col = random_col(board)
        turn = 0

        while turn in range(6):
            if turn == 5:
                scores(0,1)
                print "Game Over."
                break

            print "Turn", turn + 1

            guess_row = int(raw_input("Guess Row: (0-4)"))
            guess_col = int(raw_input("Guess Col: (0-4)"))

            if guess_row == ship_row and guess_col == ship_col:
                print "\n" + "Congratulations! You sunk my battleship!"
                scores(1,0)
                break

            elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print
                print "Oops, that's not even in the ocean."
                print "Guess again."


            elif(board[guess_row][guess_col] == "X"):
                print
                print "You guessed that one already."

            else:
                print
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                turn += 1

            print
            print print_board(board)
            print


        while True:
            play = raw_input("Do you want to play again? (Y/N)")

            if play.lower() == "y" or play.lower() == "yes":
                break
            elif play.lower() == "n" or play.lower() == "no":
                print "Player - " + str(sum(player_wins))
                print "Computer - " + str(sum(computer_wins))
                if sum(player_wins) > sum(computer_wins):
                    print "You Win!" + "\n"

                elif sum(player_wins) == sum(computer_wins):
                    print "Draw"+ "\n"

                else:
                    print "You Lose"+ "\n"
                return gameover_screen()

def battleship_medium():

    player_wins = []
    computer_wins = []


    def scores(p,c):
        player_wins.append(p)
        computer_wins.append(c)

    def print_board(board):
        for row in board:
            print " ".join(row)

    while True:
        board = []
        for x in range(7):
            board.append(["O"] * 7)

        print
        print "Okay, let's play Battleship!"
        print
        print_board(board)
        print
        print "You get 7 turns to sink my battleship. Good luck."
        print

        def random_row(board):
            return randint(0, len(board) - 1)

        def random_col(board):
            return randint(0, len(board) - 1)

        ship_row = random_row(board)
        ship_col = random_col(board)
        turn = 0

        while turn in range(8):
            if turn == 7:
                scores(0,1)
                print "Game Over."
                break

            print "Turn", turn + 1

            guess_row = int(raw_input("Guess Row: (0-6)"))
            guess_col = int(raw_input("Guess Col: (0-6)"))

            if guess_row == ship_row and guess_col == ship_col:
                print "\n" + "Congratulations! You sunk my battleship!"
                scores(1,0)
                break

            elif (guess_row < 0 or guess_row > 6) or (guess_col < 0 or guess_col > 6):
                print
                print "Oops, that's not even in the ocean."
                print "Guess again."


            elif(board[guess_row][guess_col] == "X"):
                print
                print "You guessed that one already."

            else:
                print
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                turn += 1

            print
            print print_board(board)
            print


        while True:
            play = raw_input("Do you want to play again? (Y/N)")

            if play.lower() == "y" or play.lower() == "yes":
                break
            elif play.lower() == "n" or play.lower() == "no":
                print "Player - " + str(sum(player_wins))
                print "Computer - " + str(sum(computer_wins))
                if sum(player_wins) > sum(computer_wins):
                    print "You Win!" + "\n"

                elif sum(player_wins) == sum(computer_wins):
                    print "Draw"+ "\n"

                else:
                    print "You Lose"+ "\n"
                return gameover_screen()

def battleship_large():

    player_wins = []
    computer_wins = []


    def scores(p,c):
        player_wins.append(p)
        computer_wins.append(c)

    def print_board(board):
        for row in board:
            print " ".join(row)

    while True:
        board = []
        for x in range(10):
            board.append(["O"] * 10)

        print
        print "Okay, let's play Battleship!"
        print
        print_board(board)
        print
        print "You get 10 turns to sink my battleship. Good luck."
        print

        def random_row(board):
            return randint(0, len(board) - 1)

        def random_col(board):
            return randint(0, len(board) - 1)

        ship_row = random_row(board)
        ship_col = random_col(board)
        turn = 0

        while turn in range(11):
            if turn == 10:
                scores(0,1)
                print "Game Over."
                break

            print "Turn", turn + 1

            guess_row = int(raw_input("Guess Row: (0-9)"))
            guess_col = int(raw_input("Guess Col: (0-9)"))

            if guess_row == ship_row and guess_col == ship_col:
                print "\n" + "Congratulations! You sunk my battleship!"
                scores(1,0)
                break

            elif (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
                print
                print "Oops, that's not even in the ocean."
                print "Guess again."


            elif(board[guess_row][guess_col] == "X"):
                print
                print "You guessed that one already."

            else:
                print
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                turn += 1

            print
            print print_board(board)
            print


        while True:
            play = raw_input("Do you want to play again? (Y/N)")

            if play.lower() == "y" or play.lower() == "yes":
                break
            elif play.lower() == "n" or play.lower() == "no":
                print "Player - " + str(sum(player_wins))
                print "Computer - " + str(sum(computer_wins))
                if sum(player_wins) > sum(computer_wins):
                    print "You Win!" + "\n"

                elif sum(player_wins) == sum(computer_wins):
                    print "Draw"+ "\n"

                else:
                    print "You Lose"+ "\n"
                return gameover_screen()

def title_screen():
    print("   ######                                                            ")
    print("   #     #   ##   ##### ##### #      ######  ####  #    # # #####    ")
    print("   #     #  #  #    #     #   #      #      #      #    # # #    #   ")
    print("   ######  #    #   #     #   #      #####   ####  ###### # #    #   ")
    print("   #     # ######   #     #   #      #           # #    # # #####    ")
    print("   #     # #    #   #     #   #      #      #    # #    # # #        ")
    print("   ######  #    #   #     #   ###### ######  ####  #    # # #        ")
    print
    print("Small board: 5 X 5      Medium board: 7 X 7     Large board: 10 X 10 ")
    print

def gameover_screen():
    print(" #####     #    #     # #######    ####### #     # ####### ######  ")
    print("#     #   # #   ##   ## #          #     # #     # #       #     # ")
    print("#        #   #  # # # # #          #     # #     # #       #     # ")
    print("#  #### #     # #  #  # #####      #     # #     # #####   ######  ")
    print("#     # ####### #     # #          #     #  #   #  #       #   #   ")
    print("#     # #     # #     # #          #     #   # #   #       #    #  ")
    print(" #####  #     # #     # #######    #######    #    ####### #     # ")

def start_game():
    board_size = raw_input("What size board do you want (S/M/L)?")
    if board_size.lower() == "s":
       return battleship_small()
    elif board_size.lower() == "m":
       return battleship_medium()
    elif board_size.lower() == "l":
       return battleship_large()
    elif board_size.lower() == "q" or board_size.lower() == "quit":
       return gameover_screen()
    else:
        return start_game()



title_screen()
start_game()