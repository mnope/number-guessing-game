import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    
    # write your code inside this function.
    # ACSII banner generated from https://patorjk.com/software/taag/#p=display&h=3&f=Old%20Banner&t=Pick%20%20A%20%20Number
    print("""
        ######                           #          #     #                                    
        #     # #  ####  #    #         # #         ##    # #    # #    # #####  ###### #####  
        #     # # #    # #   #         #   #        # #   # #    # ##  ## #    # #      #    # 
        ######  # #      ####         #     #       #  #  # #    # # ## # #####  #####  #    # 
        #       # #      #  #         #######       #   # # #    # #    # #    # #      #####  
        #       # #    # #   #        #     #       #    ## #    # #    # #    # #      #   #  
        #       #  ####  #    #       #     #       #     #  ####  #    # #####  ###### #    # 
        """)
    print("\nWelcome to the Pick A Number guessing game! Let's get started!\n")
    
    
    the_number = random.randint(1, 10)
    
    keep_playing = True
    high_score = 100
    while keep_playing:
        number_of_guesses = 1
        guess = 44
        while guess != the_number:
            try:
                guess = int(input("Pick a number between 1 and 10:  "))
                if guess < 1 or guess > 10:
                    raise Exception("Please keep guesses between 1 and 10. Try again!\n")
            except ValueError:
                print("Numbers only please, try again!\n")
            except Exception as err:
                print(err)
            else:
                if guess > the_number:
                    print("It's lower")
                elif guess < the_number:
                    print("It's higher")
                else: 
                    continue
                number_of_guesses += 1
            
        print(f"\nYou got it! The mystery number was {the_number}.")
        print(f"The total number of guesses this game was {number_of_guesses}.")
        again = input("\nDo you want to play again? Y/N:  ")
        if again.lower() == "y":
            if number_of_guesses < high_score:
                high_score = number_of_guesses
            print(f"\n\n*********************\nThe HIGH SCORE is {high_score}\n*********************\n\n")
            the_number = random.randint(1, 10)
            continue
        else:
            print("That was fun. See you next time!\n")
            keep_playing = False

# Kick off the program by calling the start_game function.
start_game()
