import random
import re

argent = 0
utilisateur = None


def enregistrer_joueur():
    nom_prenom = input("Enter the name and surname in the format (nameSurname): ")
    while True:
        email = input(f"Enter the email address in the format 'nameSurname@gmail.com': ")

        if email == f"{nom_prenom}@gmail.com":
            print("Valid email address.")
            break
        else:
            print("Email address is not in the expected format ('nameSurname@gmail.com'). Please try again.")

    while True:
        password = input(
            "Enter a password (8 to 12 characters, at least one lowercase, one uppercase, one digit, and one special character): ")
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,12}$", password):
            break
        else:
            print("The password does not meet the criteria. Please try again.")

    with open("Registration.txt", "a") as file:
        file.write(f"{nom_prenom}:{email}:{password}\n")
    print(f"Registration for {nom_prenom} successful.")


def authenticate():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    with open("Registration.txt", "r") as file:
        credentials = [line.strip().split(':') for line in file]

    for user_data in credentials:
        if len(user_data) == 3:
            user, saved_email, saved_pwd = user_data
            if email == saved_email and password == saved_pwd:
                return user
    return None


def display_main_menu():
    if utilisateur is not None:
        print(f"Hello, {utilisateur}!")
        print("Menu:")
        print("A- Play Roulette")
        print("B- Caesar Cipher Shift")
    else:
        print("User not authenticated. Please register.")
    print("0- Quit")


def roulette_menu():
    while True:
        print("Roulette Menu:")
        print("a- Start playing")
        print("b- Return to the main menu")
        roulette_choice = input("Select an option (a, b): ").lower()

        if roulette_choice == "a":
            play_roulette()
        elif roulette_choice == "b":
            break
        else:
            print("Invalid option.")


def play_roulette():
    global argent
    argent = int(input("Enter your balance: "))
    while argent > 0:
        bet = 0
        player_number = -1
        winning_number = random.randint(0, 36)

        print(f"Remaining money: {argent}")

        while True:
            try:
                bet = int(input("How much do you want to bet (0 to quit)? "))
                if bet == 0:
                    return argent
                elif bet > argent:
                    print("You cannot bet more than you have.")
                else:
                    break
            except ValueError:
                print("Please enter an integer.")

        while player_number < 0 or player_number > 36:
            try:
                player_number = int(input("Choose a number between 0 and 36: "))
            except ValueError:
                print("Please enter an integer.")

        print(f"Player number: {player_number}")
        print(f"Winning number: {winning_number}")

        if player_number == winning_number:
            winnings = 36 * bet
        else:
            winnings = -bet

        argent += winnings

        if winnings > 0:
            print(f"You won {winnings} chips!")
        else:
            print(f"You lost {abs(winnings)} chips.")

    print("You are out of money. End of the game.")
    return argent


def caesar_menu():
    while True:
        print("Caesar Menu:")
        print("A- Start playing")
        print("B- Return to the main menu")
        caesar_choice = input("Select an option (A, B): ").upper()

        if caesar_choice == "A":
            text = str(input("Enter the text to encrypt: "))
            shift = int(input("Enter the shift (integer): "))
            caesar_cipher_menu(text, shift)
        elif caesar_choice == "B":
            break
        else:
            print("Invalid option.")


def caesar_cipher_menu(text, shift):
    while True:
        print("Caesar Cipher Menu:")
        print("1- Caesar with ASCII code")
        print("2- Caesar with 26 letters")
        print("W- Return to Caesar Menu")
        cipher_choice = input("Select an option (1, 2, W): ")

        if cipher_choice == "1":
            caesar_ascii_code(text, shift)
        elif cipher_choice == "2":
            caesar_26_letters(text, shift)
        elif cipher_choice == "W":
            break
        else:
            print("Invalid option.")


def caesar_ascii_code(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += char
    print("Encrypted text:", result)


def caesar