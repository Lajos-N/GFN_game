def ctf_game():
    print ("Welcome to Chris and Can's CTF")
    print ("You must answer 3 questions correctly to collect the flag!")
# Lvl1
    print("\nLvl1")
a = 0
while a < 3:

    ctf_game()
    while True:
        flag1 = input("Enter the command to display IP addresses: ")
        
        if flag1.lower() == "ipconfig":
            print("Correct! You receive the letter 'I'.")
            letter1 = 'I'
            break  
        else:
            print("Incorrect! Try again. You are still on Level 1.")
            a += 1

    # Lvl2
    print("\nLvl2")

    while True:
        flag2 = input("How can I display output in the console in Python? ")
        
        if flag2 == "print()":
            print("Correct! You receive the letter 'H'.")
            letter2 = 'H'
            break  
        else:
            print("Incorrect! Try again. You are still on Level 2.")
            a += 1

    # Lvl3
    print("\nLvl3")

    while True:
        flag3 = input("Which OS does Peter hate the most? ")
        
        if flag3.lower() == "windows":
            print("Supertoll! You receive your final letter 'K'.")
            letter3 = 'K'
            break
        else:  
            print("Error 404. Try again. You are still on Level 3.")
            a += 1

    print("\nCapture")

    while True:
        CTF = input("Enter the letters you received: ")
        
        if CTF.upper() == f"{letter1}{letter2}{letter3}":
            print("\nWell done, you captured your first flag!")
            print(f"The final flag is: GFN") 
            break
        else:
            print("Incorrect! Try again.")
            a += 1

    #Spiel starten


ctf_game()

 