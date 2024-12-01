# agent.py

"""
Contains the Agent class, representing an AI agent (e.g., a child) that moves around the house
and dirties rooms after a certain number of rooms have been cleaned by the player.
"""

from typing import List, Optional, Dict
from utils import astar
import random

from room import Room


class Agent:
    """
    Represents an AI agent that moves around the house and dirties rooms.

    Attributes:
        current_room (Room): The room where the agent is currently located.
        path (List[str]): The current path the agent is following.
        target_room_name (Optional[str]): The name of the room the agent is targeting.
        wait_counter (int): Counts the number of rooms cleaned since the agent last acted.
        wait_threshold (int): Number of rooms to wait before the agent acts.
    """

    def __init__(self, current_room: Room) -> None:
        """
        Initializes the Agent with a starting room.

        Args:
            current_room (Room): The room where the agent starts.
        """
        self.current_room: Room = current_room
        self.path: List[str] = []
        self.target_room_name: Optional[str] = None
        self.wait_counter: int = 0
        self.wait_threshold: int = 2

    def increment_wait_counter(self) -> None:
        """
        Increments the agent's wait counter when the player cleans a room.
        """
        self.wait_counter += 1

    def should_act(self) -> bool:
        """
        Determines whether the agent should act based on the wait counter.

        Returns:
            bool: True if the agent should act, False otherwise.
        """
        return self.wait_counter >= self.wait_threshold

    def reset_wait_counter(self) -> None:
        """
        Resets the agent's wait counter after acting.
        """
        self.wait_counter = 0

    def set_target(self, rooms: Dict[str, Room]) -> None:
        """
        Sets the agent's target room to a clean room to dirty.

        Args:
            rooms (Dict[str, Room]): Dictionary of all room objects.
        """
        # Choose a clean room to dirty
        clean_rooms = [
            room for room in rooms.values()
            if room.is_clean and room != self.current_room
        ]
        if clean_rooms:
            target_room = random.choice(clean_rooms)
            self.target_room_name = target_room.name
        else:
            self.target_room_name = None

    def move(self, rooms: Dict[str, Room], graph: Dict[str, List[str]]) -> None:
        """
        Moves the agent along the path towards the target room if it's time to act.

        Args:
            rooms (Dict[str, Room]): Dictionary of all rooms.
            graph (Dict[str, List[str]]): Graph representation of the house.
        """
        if not self.should_act():
            return  # Agent waits until the threshold is reached

        if not self.path or self.current_room.name == self.target_room_name:
            # Recalculate path if we reached the target or there is no path
            self.set_target(rooms)
            if self.target_room_name:
                self.path = astar(
                    graph,
                    self.current_room.name,
                    self.target_room_name,
                    rooms
                )
                if self.path and len(self.path) > 1:
                    # Remove the current room from the path
                    self.path.pop(0)
                else:
                    self.path = []
            else:
                self.path = []

        if self.path:
            next_room_name = self.path.pop(0)
            self.current_room = rooms[next_room_name]

    def dirty_room(self, messages: List[str]) -> None:
        """
        Dirties the current room if it's clean and adds a message to the game.

        Args:
            messages (List[str]): List of messages to display to the player.
        """
        if not self.should_act():
            return  # Agent waits until the threshold is reached

        if self.current_room.is_clean:
            self.current_room.dirty()
            # Add a message to inform the player
            messages.append(
                f"Oh no! The child messed up the {self.current_room.name} again!"
            )

        # After acting, reset the wait counter
        self.reset_wait_counter()