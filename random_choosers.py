import random

def random_chooser():
    options = input("Please enter your list of options (separated by spaces):").split()
    while True:
        computer = random.choice(options)
        print("")
        print(f"Random choice is: {computer}")
        play_again = input("PRESS ENTER TO GO AGAIN").lower()
        if play_again != '':
            break
        
def random_chooser_that_removes_choice():

    options = input("Please enter your list of options (separated by spaces):").split()
    while True:
        computer = random.choice(options)
        print("")
        print(f"Random choice is: {computer}")
        options.remove(computer)
        play_again = input("PRESS ENTER TO GO AGAIN").lower()
        if play_again != '':
            break
        if len(options) == 0:
            print("No more options left to choose from.")
            break

def menu():
    while True:
        print("Please choose an option:")
        print("1. Random Chooser")
        print("2. Random Chooser that removes choice")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            random_chooser()
        elif choice == '2':
            random_chooser_that_removes_choice()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()


