#fuctions
def greet():
    print()
    print("Welcome to Richmond Rowing Club!")
    print()
    print('1. Login')
    print("2. Setup Account")
    print('3. Exit')
    print()
def user_check(name, pin):
    for name in name_lts:
        if name in name_lts and pin == 1875:
            print("Login successful!")
#lists
name_lts = ['Helen', "Jack", "Phin"]
#main program
greet()
choice = int(input("Please select an option: "))
while True: 
    if choice == 1:
        choice2 = int(input())
        print("Please enter your name and pin:")
        user_check(input("Name: "), int(input("Pin: ")))
        print("Welcome to Richmond Rowing Club!")
        print("Please select an option:")
        print("1. Book a boat")
        print("2. Cancel a booking")
        print("3. Exit")
        if choice2 == 1:
            print("Please select a boat type:")
            print("1. Single Scull")
            print("2. Double Scull")
            print("3. Quad Scull")
            print("4. Eight")
            print("5. Exit")
            boat_choice = int(input())
            if boat_choice == 1:
                print("You have selected a Single Scull.")
            elif boat_choice == 2:
                print("You have selected a Double Scull.")
            elif boat_choice == 3:
                print("You have selected a Quad Scull.")
            elif boat_choice == 4:
                print("You have selected an Eight.")
            elif boat_choice == 5:
                exit()
            else:
                print("Invalid choice. Please try again.")
                exit
    if choice == 2:
        print("Please enter your name and pin:")
        name = input("Name: ")
        pin = int(input("Pin: "))
        if pin == 1875:
            name_lts.append(name)
            print("Account created successfully!")
            print("Please login to continue.")
            greet()
        else:
            print("Pin is incorrect. Please try again.")
            exit




    