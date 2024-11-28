from ihk_spiel_def import *
import tkinter as tk

# Spielstatus
game_state = {
    "welcome_massage": "\nWelcome to CTF game! :)\n",
    "game_rules": "You must answer 3 questions correctly to collect the flag, but you have only three lives!",
    "player_life": 3,
    "level": 1,
    "question_answer": {
        "level1": ["Enter the command to display IP addresses?", "ipconfig", "I"],
        "level2": ["How can I display output in the console in Python?", "print()", "H"],
        "level3": ["Which OS does Peter hate the most?", "windows", "K"],
        "level4": ["Enter the letter you received: ", "ihk", "Well done, you captured your first flag!\nThe final flag is: GFN"],
    },
}

# GUI erstellen
root = tk.Tk()
root.title("CTF Game")
root.geometry("600x500")  # Fenstergröße setzen
root.configure(bg="black")  # Hintergrundfarbe auf Schwarz

# Labels und Buttons
welcome_label = tk.Label(root, text="", font=("Arial", 20, "bold"), wraplength=550, bg="black", fg="white")
rules_label = tk.Label(root, text=game_state["game_rules"], font=("Arial", 10), wraplength=550, bg="black", fg="white")
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=550, bg="black", fg="white")
answer_entry = tk.Entry(root, font=("Arial", 14), bg="black", fg="white", insertbackground="white")
answer_entry.bind("<Return>", lambda event: check_answer())
submit_button = tk.Button(root, text="Submit", command=lambda: check_answer(), bg="black", fg="white")
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=550, bg="black", fg="white")

# Platzhalter für Bilder
game_over_image = None
game_over_image_label = tk.Label(root, bg="black")

win_image = None
win_image_label = tk.Label(root, bg="black")

# Spielsteuerung
def start_game():
    welcome_label.pack(pady=10)
    question_label.pack(pady=(50, 10))
    answer_entry.pack()
    submit_button.pack(pady=(10, 20))
    result_label.pack()
    rules_label.pack(side=tk.BOTTOM, fill=tk.X)
    start_button.place_forget()
    welcome_label.config(text=game_state["welcome_massage"])
    update_question()

def update_question():
    if game_state["player_life"] > 0 and game_state["level"] < 5:
        question_label.config(text=game_state["question_answer"][f"level{game_state['level']}"][0])
        answer_entry.delete(0, tk.END)
    else:
        end_game()

def check_answer():
    player_answer = answer_entry.get().strip().lower()
    correct_answer = game_state["question_answer"][f"level{game_state['level']}"][1]
    if player_answer == correct_answer:
        result_label.config(text=f"Correct! You receive the letter {game_state['question_answer'][f'level{game_state['level']}'][2]}.",fg="green")
    
        game_state["level"] += 1
    else:
        game_state["player_life"] -= 1
        result_label.config(text=f"Incorrect! You lost a life. Lives left: {game_state['player_life']}",fg="red")
       
    if game_state["player_life"] == 0 or game_state["level"] >= 5:
        end_game()
    else:
        update_question()

def end_game():
    if game_state["player_life"] > 0:
        # Alles ausblenden
        welcome_label.pack_forget()
        question_label.pack_forget()
        answer_entry.pack_forget()
        submit_button.pack_forget()
        result_label.pack_forget()
        rules_label.pack_forget()

        # Gewinn-Bild anzeigen
        global win_image
        win_image = tk.PhotoImage(file="Flag.png")  # Pfad zum Gewinn-Bild
        win_image_label.config(image=win_image)
        win_image_label.pack(expand=True, fill=tk.BOTH)  # Bild anzeigen
    else:
        # Alles ausblenden
        welcome_label.pack_forget()
        question_label.pack_forget()
        answer_entry.pack_forget()
        submit_button.pack_forget()
        result_label.pack_forget()
        rules_label.pack_forget()

        # Game Over Bild anzeigen
        global game_over_image
        game_over_image = tk.PhotoImage(file="scull.png")  # Pfad zum Game Over Bild
        game_over_image_label.config(image=game_over_image)
        game_over_image_label.pack(expand=True, fill=tk.BOTH)  # Bild anzeigen

# Start-Button
start_button = tk.Button(root, text="Start Game", command=start_game, bg="black", fg="white")
start_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
