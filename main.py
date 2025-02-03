import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mainloop Follows Mouse")

# Set up the font
font = pygame.font.SysFont(None, 48)

# Main loop
clock = pygame.time.Clock()
angle = 0

def print_text(screen, font, text, position, angle):
    rendered_text = font.render(text, True, (255, 255, 255))
    rotated_text = pygame.transform.rotate(rendered_text, angle)
    rotated_rect = rotated_text.get_rect(center=position)
    screen.blit(rotated_text, rotated_rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render the text
    text = font.render("mainloop", True, (255, 255, 255))
    text_rect = text.get_rect(center=(mouse_x, mouse_y))

    # Rotate the text
    angle += 1
    rotated_text = pygame.transform.rotate(text, angle)
    rotated_rect = rotated_text.get_rect(center=text_rect.center)

    # Draw the text
    screen.blit(rotated_text, rotated_rect.topleft)

    # Check for mouse button click
    if pygame.mouse.get_pressed()[0]:  # Left mouse button
        print_text(screen, font, "mainloop", (mouse_x, mouse_y), angle)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)