from ihk_spiel_def import *
import tkinter as tk

# Spielstatus
game_state = {
    "welcome_massage": "Welcome to the CTF Challenge!",
    "game_rules": "Answer 3 questions correctly to collect the flag, but you have only three lives!",
    "player_life": 3,
    "level": 1,
    "question_answer": {
        "level1": ["", "", "I"],
        "level2": ["", "", "H"],
        "level3": ["", "", "K"],
        "level4": ["Enter the letter you received: ", "ihk", "Well done, you captured your first flag!\nThe final flag is: GFN"],
    },
    "collected_letters": [],  # Neue Liste für gesammelte Buchstaben
}

# GUI erstellen
root = tk.Tk()
root.title("CTF Game")
root.geometry("600x500")
root.configure(bg="black")

# Labels und Buttons
welcome_label = tk.Label(
    root,
    text=game_state["welcome_massage"],
    font=("Arial", 20, "bold"),
    wraplength=550,
    bg="black",
    fg="white",
)
rules_label = tk.Label(
    root,
    text=game_state["game_rules"],
    font=("Arial", 12),
    wraplength=550,
    bg="black",
    fg="white",
)
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=550, bg="black", fg="white")
answer_entry = tk.Entry(root, font=("Arial", 14), bg="black", fg="white", insertbackground="white")
answer_entry.bind("<Return>", lambda event: check_answer())
submit_button = tk.Button(root, text="Submit", command=lambda: check_answer(), bg="black", fg="white")
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=550, bg="black", fg="white")
collected_letters_label = tk.Label(
    root, 
    text="Collected letters: ", 
    font=("Arial", 22, "bold"),
    bg="black", 
    fg="white"
)

collected_letters_value_label = tk.Label(
    root, 
    text="", 
    font=("Arial", 22, "bold"),
    bg="black", 
    fg="green"
)

# Nach den anderen Label-Definitionen einen neuen Label für den Level-Counter hinzufügen
level_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="black",
    fg="white"
)

# Spielfunktionen
def start_game():
    question_uploader(question_lottery(), game_state["question_answer"])
    # Welcome-Nachricht und Regeln ausblenden
    welcome_label.pack_forget()
    rules_label.pack_forget()
    quit_button.place_forget()  # Quit-Button ausblenden beim Spielstart

    # Spielfenster-Elemente mittig platzieren
    question_label.place(relx=0.5, rely=0.3, anchor="center")
    answer_entry.place(relx=0.5, rely=0.4, anchor="center", width=300)
    submit_button.place(relx=0.5, rely=0.5, anchor="center")
    result_label.place(relx=0.5, rely=0.6, anchor="center")
    
    # Level-Label anzeigen
    level_label.place(relx=0.5, rely=0.1, anchor="center")
    level_label.config(text=f"Level: {game_state['level']}")

    start_button.place_forget()
    update_question()

def update_question():
    if game_state["player_life"] > 0 and game_state["level"] < 5:
        # Level-Anzeige nur aktualisieren, wenn nicht im letzten Level (Level 4)
        if game_state["level"] != 4:
            level_label.config(text=f"Level: {game_state['level']}")
            level_label.place(relx=0.5, rely=0.1, anchor="center")
        else:
            level_label.place_forget()  # Level-Anzeige ausblenden im letzten Level
            
        question_label.config(text=game_state["question_answer"][f"level{game_state['level']}"][0])
        answer_entry.delete(0, tk.END)
    else:
        end_game()

def check_answer():
    player_answer = answer_entry.get().strip().lower()
    correct_answer = game_state["question_answer"][f"level{game_state['level']}"][1]
    if player_answer == correct_answer:
        # Buchstaben sammeln
        current_letter = game_state["question_answer"][f"level{game_state['level']}"][2]
        game_state["collected_letters"].append(current_letter)
        
        # Erfolgstext anzeigen
        result_label.config(
            text=f"Correct! You receive the letter {current_letter}",
            fg="green",
        )
        
        # Gesammelte Buchstaben anzeigen
        collected_letters_text = "".join(game_state["collected_letters"])
        collected_letters_label.config(
            text="Collected letters: ",
            font=("Arial", 22, "bold"),
            fg="white"
        )
        collected_letters_value_label.config(
            text=collected_letters_text,
            font=("Arial", 22, "bold"),
            fg="green"
        )
        
        # Labels weiter rechts platzieren (von 0.60/0.62 zu 0.65/0.67)
        if game_state["collected_letters"]:
            collected_letters_label.place(relx=0.70, rely=0.85, anchor="e")
            collected_letters_value_label.place(relx=0.70, rely=0.85, anchor="w")
        
        game_state["level"] += 1
    else:
        game_state["player_life"] -= 1
        result_label.config(
            text=f"Incorrect! You lost a life. Lives left: {game_state['player_life']}",
            fg="red",
        )
    if game_state["player_life"] == 0 or game_state["level"] >= 5:
        end_game()
    else:
        update_question()

def end_game():
    question_label.place_forget()
    answer_entry.place_forget()
    submit_button.place_forget()
    result_label.place_forget()
    collected_letters_label.place_forget()
    collected_letters_value_label.place_forget()
    level_label.place_forget()

    if game_state["player_life"] > 0:
        global win_image
        win_image = tk.PhotoImage(file="Flag.png")
        win_image_label = tk.Label(root, image=win_image, bg="black")
        win_image_label.pack(expand=True, fill=tk.BOTH)
        
        # Restart Button bei Sieg hinzufügen
        restart_button = tk.Button(
            root, 
            text="Play again", 
            command=reset_game,
            bg="black", 
            fg="white",
            font=("Arial", 12)
        )
        restart_button.place(relx=0.5, rely=0.8, anchor="center")
        
        # Quit Button wieder anzeigen
        quit_button.place(relx=0.5, rely=0.9, anchor="center")
    else:
        global game_over_image
        game_over_image = tk.PhotoImage(file="scull.png")
        game_over_image_label = tk.Label(root, image=game_over_image, bg="black")
        game_over_image_label.pack(expand=True, fill=tk.BOTH)
        
        # Try Again Button bei Niederlage
        try_again_button = tk.Button(
            root, 
            text="Try Again", 
            command=reset_game,
            bg="black", 
            fg="white",
            font=("Arial", 12)
        )
        try_again_button.place(relx=0.5, rely=0.85, anchor="center")
        
        # Quit Button wieder anzeigen
        quit_button.place(relx=0.5, rely=0.95, anchor="center")

def reset_game():
    # Alle existierenden Widgets entfernen
    for widget in root.winfo_children():
        widget.destroy()
        
    # Spielstatus zurücksetzen
    game_state["player_life"] = 3
    game_state["level"] = 1
    game_state["collected_letters"] = []  # Buchstaben zurücksetzen
    
    # GUI-Elemente neu erstellen und global machen
    global welcome_label, rules_label, question_label, answer_entry, submit_button, result_label, start_button, collected_letters_label, collected_letters_value_label, level_label, quit_button
    
    welcome_label = tk.Label(root, text=game_state["welcome_massage"], font=("Arial", 20, "bold"), 
                           wraplength=550, bg="black", fg="white")
    rules_label = tk.Label(root, text=game_state["game_rules"], font=("Arial", 12), 
                         wraplength=550, bg="black", fg="white")
    question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=550, bg="black", fg="white")
    answer_entry = tk.Entry(root, font=("Arial", 14), bg="black", fg="white", insertbackground="white")
    answer_entry.bind("<Return>", lambda event: check_answer())
    submit_button = tk.Button(root, text="Submit", command=lambda: check_answer(), bg="black", fg="white")
    result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=550, bg="black", fg="white")
    start_button = tk.Button(
        root, 
        text="Start Game", 
        command=start_game, 
        bg="black", 
        fg="white",
        font=("Arial", 14, "bold"),  # Schriftgröße von 12 auf 14 erhöht
        width=12,  # Breite hinzugefügt
        height=2   # Höhe hinzugefügt
    )
    collected_letters_label = tk.Label(
        root, 
        text="Collected letters: ", 
        font=("Arial", 22, "bold"),
        bg="black", 
        fg="white"
    )
    
    collected_letters_value_label = tk.Label(
        root, 
        text="", 
        font=("Arial", 22, "bold"),
        bg="black", 
        fg="green"
    )
    
    level_label = tk.Label(
        root,
        text="",
        font=("Arial", 16, "bold"),
        bg="black",
        fg="white"
    )
    
    quit_button = tk.Button(
        root, 
        text="Quit Game", 
        command=quit_game,
        bg="black", 
        fg="white",
        font=("Arial", 14, "bold"),
        width=12,
        height=2
    )
    
    # Anfangs-Layout wiederherstellen
    welcome_label.pack(pady=10)
    rules_label.pack(side=tk.BOTTOM, fill=tk.X, pady=15)
    start_button.place(relx=0.5, rely=0.5, anchor="center")
    quit_button.place(relx=0.5, rely=0.65, anchor="center")

# Nach den Label-Definitionen und vor den Button-Definitionen
def quit_game():
    root.destroy()

# Dann erst die Button-Definitionen
start_button = tk.Button(
    root, 
    text="Start Game", 
    command=start_game, 
    bg="black", 
    fg="white",
    font=("Arial", 14, "bold"),
    width=12,
    height=2
)
start_button.place(relx=0.5, rely=0.5, anchor="center")

quit_button = tk.Button(
    root, 
    text="Quit Game", 
    command=quit_game,  #  quit_game 
    bg="black", 
    fg="white",
    font=("Arial", 14, "bold"),
    width=12,
    height=2
)
quit_button.place(relx=0.5, rely=0.65, anchor="center")

# Welcome-Nachricht und Regeln anzeigen
welcome_label.pack(pady=10)
rules_label.pack(side=tk.BOTTOM, fill=tk.X, pady=15)

root.mainloop()
