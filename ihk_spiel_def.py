def welcome_massage(game_state): # print the welcome massage
    if not hasattr(welcome_massage, "has_run"): # check if the function has already run
        welcome_massage.has_run = True

        massage = game_state["welcome_massage"]
        
        return print(massage)


def game_rules(game_state): # print the game rules
    if not hasattr(game_rules, "has_run"): # check if the function has already run
        game_rules.has_run = True

        massage = game_state["game_rules"]

        return print(massage)

    massage = "You already know the rules of the game I won't tell you again"
    return print(massage)    


def answer_not_correct(life): # answer is not correct print massage
    # massage= "TESZT"
    massage = f"Incorrect! Try again. You lost a life.\nYou have {life} lives left." if life > 0 else "You lost a life.\nYou have no more lives left."
    return print(massage)

def minus_life(life): # minus 1 life
    
    life -= 1
    return life


def you_are_dead_massage(): # dead massage
    massage = "You are dead! Game over!"
    return print(massage)


def you_won(life): # you won massage and exit
    if life > 0:
        massage = "Well done!"
        return print(massage), exit()


def want_to_try_again(life): # ask if the player want to try again and reset the life
    if input("Do you want to try again? (yes/no): ").lower() == "yes":
        life = 3
        return life
    else: # if the player don't want to try again print goodbye and exit
        print("Goodbye!")
        exit()

