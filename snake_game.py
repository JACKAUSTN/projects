
import sys
import pygame # type: ignore
from pygame.locals import * # type: ignore
from random import randint
from os import path

# Initialize the game
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Snake Game")

# Try to load music
try:
    pygame.mixer.music.load("background_music.mp3")
    pygame.mixer.music.play(-1)
except Exception:
    pass  # Ignore if music file is missing

# Set up the display
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 15

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up fonts
FONT = pygame.font.SysFont("Arial", 30)
SCORE_FONT = pygame.font.SysFont("Arial", 20)

# Set up the snake
SNAKE_SIZE = 20
SNAKE_COLOR = GREEN

# Set up the food
FOOD_SIZE = 20
FOOD_COLOR = RED

# Set up the game clock
CLOCK = pygame.time.Clock()

# Load high score from file
def load_high_score():
    if path.exists("high_score.txt"):
        with open("high_score.txt", "r") as file:
            return int(file.read())
    return 0

# Save high score to file
def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))

# Draw the snake
def draw_snake(snake_pos):
    for pos in snake_pos:
        pygame.draw.rect(WINDOW, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

# Draw the food
def draw_food(food_pos):
    pygame.draw.rect(WINDOW, FOOD_COLOR, pygame.Rect(food_pos[0], food_pos[1], FOOD_SIZE, FOOD_SIZE))

# Draw the score
def draw_score(score):
    score_text = SCORE_FONT.render(f"Score: {score}", True, WHITE)
    WINDOW.blit(score_text, (10, 10))

# Draw the high score
def draw_high_score(high_score):
    high_score_text = SCORE_FONT.render(f"High Score: {high_score}", True, WHITE)
    WINDOW.blit(high_score_text, (WIDTH - 200, 10))

# Draw the game over message
def draw_game_over():
    game_over_text = FONT.render("Game Over! Press R to Restart or Q to Quit", True, WHITE)
    WINDOW.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

def reset_game():
    snake_pos = [(100, 50), (90, 50), (80, 50)]
    snake_direction = "RIGHT"
    food_pos = (randint(0, (WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE,
                randint(0, (HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE)
    score = 0
    game_over = False
    return snake_pos, snake_direction, food_pos, score, game_over

def main():
    high_score = load_high_score()
    while True:
        snake_pos, snake_direction, food_pos, score, game_over = reset_game()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT: # type: ignore
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN: # type: ignore
                    if event.key == K_UP and snake_direction != "DOWN": # type: ignore
                        snake_direction = "UP"
                    elif event.key == K_DOWN and snake_direction != "UP": # type: ignore
                        snake_direction = "DOWN"
                    elif event.key == K_LEFT and snake_direction != "RIGHT": # type: ignore
                        snake_direction = "LEFT"
                    elif event.key == K_RIGHT and snake_direction != "LEFT": # type: ignore
                        snake_direction = "RIGHT"
                    elif event.key == K_r and game_over: # type: ignore
                        break  # Break inner loop to restart
                    elif event.key == K_q and game_over: # type: ignore
                        pygame.quit()
                        sys.exit()

            if not game_over:
                # Move the snake
                if snake_direction == "UP":
                    new_head = (snake_pos[0][0], snake_pos[0][1] - SNAKE_SIZE)
                elif snake_direction == "DOWN":
                    new_head = (snake_pos[0][0], snake_pos[0][1] + SNAKE_SIZE)
                elif snake_direction == "LEFT":
                    new_head = (snake_pos[0][0] - SNAKE_SIZE, snake_pos[0][1])
                elif snake_direction == "RIGHT":
                    new_head = (snake_pos[0][0] + SNAKE_SIZE, snake_pos[0][1])

                # Check for collision with food
                if new_head == food_pos:
                    score += 1
                    food_pos = (randint(0, (WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE,
                                randint(0, (HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE)
                else:
                    snake_pos.pop()

                # Check for collision with walls or self
                if (new_head[0] < 0 or new_head[0] >= WIDTH or
                    new_head[1] < 0 or new_head[1] >= HEIGHT or
                    new_head in snake_pos):
                    game_over = True

                snake_pos.insert(0, new_head)

                WINDOW.fill(BLACK)
                draw_snake(snake_pos)
                draw_food(food_pos)
                draw_score(score)
                draw_high_score(high_score)
                pygame.display.update()
                CLOCK.tick(FPS)
            else:
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)
                draw_game_over()
                pygame.display.update()
                # Wait for user input to restart or quit
                break  # Break inner loop to restart or quit

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
