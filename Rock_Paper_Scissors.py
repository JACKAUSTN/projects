import random
def play_game():
    options = ('rock', 'paper', 'scissors')
    player_score = 0
    computer_score = 0
    while True: 
        player = None
        computer = random.choice(options)
   
        print("Welcome to Rock, Paper, Scissors!")
        player = input("Ready? Rock, paper, scissors! ").lower()

        print("Player: ", player)
        print("Computer: ", computer)
        if player == computer:
            print("It's a tie!")
        elif player == 'rock':
            if computer == 'scissors':
                print("Rock crushes scissors! You win!")
                player_score += 1
            else:
                print("Paper covers rock! You lose!")
                computer_score += 1
        elif player == 'paper':
            if computer == 'rock':
                print("Paper covers rock! You win!")
                player_score += 1
            else:
                print("Scissors cuts paper! You lose!")
                computer_score += 1
        elif player == 'scissors':  
            if computer == 'paper':
                print("Scissors cuts paper! You win!")
                player_score += 1
            else:
                print("Rock crushes scissors! You lose!")
                computer_score += 1
        else:
            print("Invalid input. Please try again.")
            continue
        print("Player score: ", player_score)
        print("Computer score: ", computer_score)
        play_again = input("PRESS ENTER TO PLAY AGAIN").lower()
        if play_again != '':
            break
play_game()

