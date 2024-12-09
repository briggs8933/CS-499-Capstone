# room.py

"""
Contains the Room class, representing a room in the game.
"""

import pygame
import time
from constants import *


class Room:
    """
    Represents a room in the game.

    Attributes:
        name (str): The name of the room.
        x (int): The x-coordinate of the room's position.
        y (int): The y-coordinate of the room's position.
        rect (pygame.Rect): The rectangle representing the room's position and size.
        connections (Dict[str, str]): Possible moves from this room.
        is_clean (bool): Indicates whether the room is clean.
        last_cleaned (float): Timestamp of when the room was last cleaned.
    """

    def __init__(self, name: str, x: int, y: int, connections: dict = None) -> None:
        """
        Initializes the Room with its name, position, and connections.

        Args:
            name (str): The name of the room.
            x (int): The x-coordinate of the room's position.
            y (int): The y-coordinate of the room's position.
            connections (dict): Dictionary of possible moves from this room.
        """
        self.name: str = name
        self.x: int = x
        self.y: int = y
        self.rect: pygame.Rect = pygame.Rect(x, y, ROOM_WIDTH, ROOM_HEIGHT)
        self.connections: dict = connections if connections else {}
        self.is_clean: bool = False
        self.last_cleaned: float = 0.0

    @classmethod
    def load_rooms_from_db(cls, conn):
        """
        Load rooms from the database and return a dictionary of Room instances.
        """
        cursor = conn.cursor()
        cursor.execute('SELECT name, x_coordinate, y_coordinate, is_clean FROM Rooms')
        rooms = {}
        for row in cursor.fetchall():
            name, x, y, is_clean = row
            room = cls(name, x, y)
            room.is_clean = bool(is_clean)
            rooms[name] = room
        return rooms

    def save_to_db(self, conn):
        """
        Save the room's current state to the database.
        """
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO Rooms (name, x_coordinate, y_coordinate, is_clean)
            VALUES (?, ?, ?, ?)
        ''', (self.name, self.x, self.y, int(self.is_clean)))
        conn.commit()

    def dirty(self) -> None:
        """
        Marks the room as dirty.
        """
        self.is_clean = False

    def clean(self) -> None:
        """
        Marks the room as clean and updates the last cleaned timestamp.
        """
        self.is_clean = True
        self.last_cleaned = time.time()

    def draw(self, surface: pygame.Surface, is_current_room: bool, has_agent: bool) -> None:
        """
        Draws the room on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw on.
            is_current_room (bool): True if the player is in this room.
            has_agent (bool): True if the agent is in this room.
        """
        # Set color based on cleanliness
        color = CLEAN_COLOR if self.is_clean else DIRTY_COLOR
        pygame.draw.rect(surface, color, self.rect)

        # Highlight current room
        if is_current_room:
            pygame.draw.rect(surface, WHITE, self.rect, 3)

        # Draw the agent if present
        if has_agent:
            pygame.draw.circle(surface, (0, 0, 255), (self.rect.centerx, self.rect.centery), 10)

        # Display room name
        font = pygame.font.SysFont(None, 24)
        text = font.render(self.name, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)