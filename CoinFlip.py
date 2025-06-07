import random
def play_game():
    options = ("Heads", "Tails")
    heads_score = 0
    tails_score = 0
    while True: 
        computer = random.choice(options)
        print("")
        print("Head or Tails?...")
        print(computer)
        if computer == "Heads":
            heads_score += 1
        elif computer == "Tails":
            tails_score += 1
        print(f"Heads: {heads_score}")
        print(f"Tails: {tails_score}")
        play_again = input("PRESS ENTER TO PLAY AGAIN").lower()
        if play_again != '':
            pass
play_game()
