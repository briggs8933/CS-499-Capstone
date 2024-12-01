# player.py

"""
Contains the Player class, representing the player character in the game.
"""

from typing import Dict, List
from room import Room


class Player:
    """
    Represents the player in the game.

    Attributes:
        current_room (Room): The room where the player is currently located.
    """

    def __init__(self, current_room: Room) -> None:
        """
        Initializes the player with a starting room.

        Args:
            current_room (Room): The room where the player starts.
        """
        self.current_room: Room = current_room

    def move(self, direction: str, rooms: Dict[str, Room], messages: List[str]) -> None:
        """
        Moves the player in the specified direction if possible.

        Args:
            direction (str): The direction to move ('North', 'South', 'East', 'West').
            rooms (Dict[str, Room]): Dictionary of all rooms.
            messages (List[str]): List of messages to display to the player.
        """
        if direction in self.current_room.connections:
            prev_room = self.current_room.name
            next_room_name = self.current_room.connections[direction]
            self.current_room = rooms[next_room_name]
            message = f"You moved from {prev_room} to the {self.current_room.name}."
            print(message)
            messages.append(message)

            # Specific messages for certain rooms
            if self.current_room.name == 'Master Bedroom':
                messages.append("You have entered the Master Bedroom.")
        else:
            message = "Trying to escape?! There is no escape! Please try your move again."
            print(message)
            messages.append(message)

    def clean_room(self, messages: List[str]) -> bool:
        """
        Cleans the current room if it's dirty and adds a message.

        Args:
            messages (List[str]): List of messages to display to the player.

        Returns:
            bool: True if the room was cleaned, False if it was already clean.
        """
        if not self.current_room.is_clean:
            self.current_room.clean()
            messages.append(f"You cleaned the {self.current_room.name} and took a picture.")
            return True  # Room was cleaned
        else:
            messages.append(f"The {self.current_room.name} is already clean.")
            return False  # Room was already clean