from test_def import *

# State
life = 3

game_state = {
    "welcome_massage": "\nWelcome to CTF game! :)\n",
    "game_rules": "You must answer 3 questions correctly to collect the flag, but you have only three lives!",

    "question_answer" : {
        "level1": ["Enter the command to display IP addresses: ", "ipconfig", "I"],
        "level2": ["How can I display output in the console in Python? ", "print()", "H"],
        "level3": ["Which OS does Peter hate the most? ", "windows", "K"],
        "level4": ["Enter the letter you received: ", "IHK"], #TODO: késöbb átírni az IHK-t, hogy ne legyen fix        
    },
}


while True:
    welcome_massage(game_state)
    game_rules(game_state)
    
    while life > 0:
        print("\nLvl1") #TODO: kell egy szint kiírató függvény
        flag1 = input("Enter the command to display IP addresses: ")
        
        if flag1.lower() == "ipconfig":
            print("Correct! You receive the letter 'I'.")
            letter1 = 'I'
            break
        else:
            life = minus_life(life)
            answer_not_correct(life)
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
            life = minus_life(life)
            answer_not_correct(life)
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
            life = minus_life(life)
            answer_not_correct(life)
            if life == 0:
                you_are_dead_massage()
                break


    while life > 0:
        CTF = input("\nEnter the letter you received: ")

        if CTF.upper() == f"{letter1}{letter2}{letter3}":
            print("\nWell done, you captured your first flag!")
            print(f"The final flag is: GFN") 
            break
        else:
            life = minus_life(life)
            answer_not_correct(life)
            if life == 0:
                you_are_dead_massage()
                break

    you_won(life)
    want_to_try_again()
    