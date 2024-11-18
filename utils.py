import pygame
from constants import *

def render_messages(surface, messages):
    # Create a rect for the text box
    text_box_rect = pygame.Rect(TEXT_BOX_X, TEXT_BOX_Y, TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT)

    # Fill the text box with a background color
    pygame.draw.rect(surface, BLACK, text_box_rect)

    # Set up the font
    font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

    # Render each message
    line_height = FONT_SIZE + 5
    for i, message in enumerate(messages[-5:]):  # Show the last 5 messages
        text_surface = font.render(message, True, FONT_COLOR)
        text_position = (TEXT_BOX_X + 10, TEXT_BOX_Y + 10 + i * line_height)
        surface.blit(text_surface, text_position)