# State
life = 3


def welcome_massage(): # print the welcome massage
    if not hasattr(welcome_massage, "has_run"): # check if the function has already run
        welcome_massage.has_run = True

        massage = "\nWelcome to Chris and Can's CTF \n\nYou must answer 3 questions correctly to collect the flag!\n"
        
        return print(massage)


def game_rules(): # print the game rules
    if not hasattr(game_rules, "has_run"): # check if the function has already run
        game_rules.has_run = True

        massage = "You must answer 3 questions correctly to collect the flag, but you have only three lives!"  

        return print(massage)

    massage = "You already know the rules of the game I won't tell you again"
    return print(massage)    


def answer_not_correct(): # answer is not correct minus 1 life and print massage
    global life
    life -= 1
    massage = f"Incorrect! Try again. You lost a life.\nYou have {life} lives left." if life > 0 else "You lost a life.\nYou have no more lives left."
    return print(massage)


def you_are_dead_massage(): # dead massage
    massage = "You are dead! Game over!"
    return print(massage)


def you_won(): # you won massage and exit
    if life > 0:
        massage = "Well done!"
        return print(massage), exit()


def want_to_try_again(): # ask if the player want to try again and reset the life
    if input("Do you want to try again? (yes/no): ").lower() == "yes":
        global life
        life = 3
    else: # if the player don't want to try again print goodbye and exit
        print("Goodbye!")
        exit()


while True:
    welcome_massage()
    game_rules()
    
    while life > 0:
        print("\nLvl1")
        flag1 = input("Enter the command to display IP addresses: ")
        
        if flag1.lower() == "ipconfig":
            print("Correct! You receive the letter 'I'.")
            letter1 = 'I'
            break
        else:
            answer_not_correct()
            if life == 0:
                you_are_dead_massage()
                break

    while life > 0:
        print("\nLvl2")
        flag2 = input("How can I display output in the console in Python? ")
        
        if flag2 == "print()":
            print("Correct! You receive the letter 'H'.")
            letter2 = 'H'
            break  
        else:
            answer_not_correct()
            if life == 0:
                you_are_dead_massage()
                break

    while life > 0:
        print("\nLvl3")
        flag3 = input("Which OS does Peter hate the most? ")
        
        if flag3.lower() == "windows":
            print("Supertoll! You receive your final letter 'K'.")
            letter3 = 'K'
            break
        else:  
            answer_not_correct()
            if life == 0:
                you_are_dead_massage()
                break


    #TODO: CTF ist noch nicht implementiert


    you_won()
    want_to_try_again()
    