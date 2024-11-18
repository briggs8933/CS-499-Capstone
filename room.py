# room.py

import pygame
from constants import *

class Room:
    def __init__(self, name, x, y, connections):
        self.name = name
        self.rect = pygame.Rect(x, y, ROOM_WIDTH, ROOM_HEIGHT)
        self.connections = connections  # Dictionary of possible moves
        self.is_clean = False

    def draw(self, surface, is_current_room):
        # Set color based on cleanliness
        color = CLEAN_COLOR if self.is_clean else DIRTY_COLOR
        pygame.draw.rect(surface, color, self.rect)

        # Highlight current room
        if is_current_room:
            pygame.draw.rect(surface, WHITE, self.rect, 3)

        # Display room name
        font = pygame.font.SysFont(None, 24)
        text = font.render(self.name, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)