#1
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = players[0]

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter row (1-3) and column (1-3) separated by space: ").split())
        if board[row - 1][col - 1] == ' ':
            board[row - 1][col - 1] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif all(cell != ' ' for row in board for cell in row):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = players[1] if current_player == players[0] else players[0]
        else:
            print("This cell is already occupied, please choose another.")

tic_tac_toe()

#2
def add_word(dictionary, english_word, french_translation):
    if english_word.strip() == "":
        print("Error: English word cannot be empty.")
        return
    if english_word in dictionary:
        print(f"Error: The word '{english_word}' already exists in the dictionary.")
        return
    dictionary[english_word] = french_translation
    print(f"The word '{english_word}' with translation '{french_translation}' has been added to the dictionary.")

def delete_word(dictionary, english_word):
    if english_word.strip() == "":
        print("Error: English word cannot be empty.")
        return
    if english_word in dictionary:
        del dictionary[english_word]
        print(f"The word '{english_word}' has been deleted from the dictionary.")
    else:
        print(f"Error: The word '{english_word}' is not found in the dictionary.")

def find_translation(dictionary, english_word):
    if english_word.strip() == "":
        print("Error: English word cannot be empty.")
        return
    if english_word in dictionary:
        return dictionary[english_word]
    else:
        return f"Error: The translation for '{english_word}' is not found in the dictionary."

def update_translation(dictionary, english_word, new_french_translation):
    if english_word.strip() == "":
        print("Error: English word cannot be empty.")
        return
    if english_word in dictionary:
        dictionary[english_word] = new_french_translation
        print(f"The translation for the word '{english_word}' has been updated to '{new_french_translation}'.")
    else:
        print(f"Error: The word '{english_word}' is not found in the dictionary.")

def main():
    english_french_dictionary = {}

    while True:
        print("\nMenu:")
        print("1. Add a word")
        print("2. Delete a word")
        print("3. Find translation")
        print("4. Update translation")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            english_word = input("Enter the English word: ")
            french_translation = input("Enter the French translation: ")
            add_word(english_french_dictionary, english_word, french_translation)
        elif choice == '2':
            english_word = input("Enter the English word to delete: ")
            delete_word(english_french_dictionary, english_word)
        elif choice == '3':
            english_word = input("Enter the English word to find translation: ")
            print(find_translation(english_french_dictionary, english_word))
        elif choice == '4':
            english_word = input("Enter the English word to update translation: ")
            new_french_translation = input("Enter the new French translation: ")
            update_translation(english_french_dictionary, english_word, new_french_translation)
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

#3
def add_employee(company, name, phone, email, position, office_number, skype):
    if name in company:
        print("Error: Employee with this name already exists.")
        return
    company[name] = {'Phone': phone, 'Email': email, 'Position': position, 'Office Number': office_number, 'Skype': skype}
    print(f"Employee '{name}' has been added to the company.")

def delete_employee(company, name):
    if name in company:
        del company[name]
        print(f"Employee '{name}' has been deleted from the company.")
    else:
        print(f"Error: Employee '{name}' is not found in the company.")

def find_employee(company, name):
    if name in company:
        print(f"Employee '{name}': {company[name]}")
    else:
        print(f"Error: Employee '{name}' is not found in the company.")

def update_employee(company, name, field, new_value):
    if name in company:
        if field in company[name]:
            company[name][field] = new_value
            print(f"The {field} of employee '{name}' has been updated to '{new_value}'.")
        else:
            print(f"Error: '{field}' is not a valid field.")
    else:
        print(f"Error: Employee '{name}' is not found in the company.")

def main():
    company_info = {}

    while True:
        print("\nMenu:")
        print("1. Add an employee")
        print("2. Delete an employee")
        print("3. Find an employee")
        print("4. Update employee information")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee's name: ")
            phone = input("Enter employee's phone: ")
            email = input("Enter employee's email: ")
            position = input("Enter employee's position: ")
            office_number = input("Enter employee's office number: ")
            skype = input("Enter employee's Skype: ")
            add_employee(company_info, name, phone, email, position, office_number, skype)
        elif choice == '2':
            name = input("Enter employee's name to delete: ")
            delete_employee(company_info, name)
        elif choice == '3':
            name = input("Enter employee's name to find: ")
            find_employee(company_info, name)
        elif choice == '4':
            name = input("Enter employee's name to update: ")
            field = input("Enter the field to update: ")
            new_value = input("Enter the new value: ")
            update_employee(company_info, name, field, new_value)
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
