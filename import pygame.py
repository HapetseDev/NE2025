import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Mainloop Example")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw everything

    # Flip the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()