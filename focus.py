import pygame
import time
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sighting Device")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up fonts
FONT = pygame.font.SysFont('Arial', 30)

# Load sight image
sight_image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'sight.png'))
sight_rect = sight_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Set up timer
start_time = pygame.time.get_ticks()

# Main loop
running = True
while running:
    # Check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    window.fill(BLACK)

    # Draw sight image
    window.blit(sight_image, sight_rect.topleft)

    # Calculate remaining time
    seconds = 120 - (pygame.time.get_ticks() - start_time) // 1000
    seconds = max(0, seconds)

    # Draw timer
    timer_text = FONT.render(f'Time: {seconds}', True, WHITE)
    window.blit(timer_text, (10, 10))

    # Refresh display
    pygame.display.flip()

    # If time is up, break the loop
    if seconds == 0:
        time.sleep(3)
        running = False

# Clean up
pygame.quit()