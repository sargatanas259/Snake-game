import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
SNAKE_SIZE = 20
SPEED = 15

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Game Over. Score: {score}", True, RED)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds
    reset_game()

def reset_game():
    global snake, snake_direction, score, food
    snake = [(100, 50), (90, 50), (80, 50)]
    snake_direction = "RIGHT"
    score = 0
    food = [random.randrange(1, (WIDTH // 20)) * 20,
            random.randrange(1, (HEIGHT // 20)) * 20]

# Initialize the snake
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = "RIGHT"

# Initialize the food
food = [random.randrange(1, (WIDTH // 20)) * 20,
        random.randrange(1, (HEIGHT // 20)) * 20]

# Initialize score
score = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction!= "DOWN":
                snake_direction = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Move the snake
    new_head = ()
    if snake_direction == "UP":
        new_head = (snake[0][0], snake[0][1] - SNAKE_SIZE)
    if snake_direction == "DOWN":
        new_head = (snake[0][0], snake[0][1] + SNAKE_SIZE)
    if snake_direction == "LEFT":
        new_head = (snake[0][0] - SNAKE_SIZE, snake[0][1])
    if snake_direction == "RIGHT":
        new_head = (snake[0][0] + SNAKE_SIZE, snake[0][1])

    snake.insert(0, new_head)

    # Check for collisions with the wall
    if (
        snake[0][0] < 0
        or snake[0][0] >= WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= HEIGHT
    ):
        game_over()
        continue

    # Check for collisions with itself
    if len(snake) > 1 and new_head in snake[1:]:
        game_over()
        continue

    # Check for collisions with food
    if snake[0] == food:
        score += 1
        food = [random.randrange(1, (WIDTH // 20)) * 20,
                random.randrange(1, (HEIGHT // 20)) * 20]
    else:
        snake.pop()

    # Draw everything on the screen
    screen.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control game speed
    pygame.time.Clock().tick(SPEED)