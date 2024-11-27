from ihk_spiel_def import *

# State
game_state = {
    "welcome_massage": "\nWelcome to CTF game! :)\n",
    "game_rules": "You must answer 3 questions correctly to collect the flag, but you have only three lives!",
    "player_life": 3,
    "level": 1,

    "question_answer" : {
        "level1": ["Enter the command to display IP addresses?", "ipconfig", "I"],
        "level2": ["How can I display output in the console in Python?", "print()", "H"],
        "level3": ["Which OS does Peter hate the most?", "windows", "K"],
        "level4": ["Enter the letter you received: ", "ihk", ""],
    },
}


while True:
    welcome_massage(game_state)
    game_rules(game_state)
    
    while game_state["player_life"] > 0 and game_state["level"] < 5:
        print(f"Level {game_state["level"]}") 
        question_printer(game_state, game_state["level"])

        if player_input_and_answer_check(game_state["question_answer"][f"level{game_state['level']}"][1]):
            answer_is_correct(game_state["question_answer"][f"level{game_state['level']}"][2])
            game_state["level"] = level_counter(game_state["level"])
        
        else:
            game_state["player_life"] = minus_life(game_state["player_life"])
            answer_not_correct(game_state["player_life"])
                            
    you_won(game_state["player_life"])
    game_state["player_life"] = want_to_try_again(game_state["player_life"])
    