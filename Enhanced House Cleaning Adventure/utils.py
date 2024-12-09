# utils.py

"""
Utility functions used in the game, including rendering messages and the A* pathfinding algorithm.
"""

import pygame
import heapq
from typing import List, Dict, Optional
from constants import *
from room import Room


def render_messages(surface: pygame.Surface, messages: List[str]) -> None:
    """
    Renders messages onto the game surface.

    Args:
        surface (pygame.Surface): The surface to draw on.
        messages (List[str]): List of messages to display.
    """
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


def heuristic(a: str, b: str, rooms: Dict[str, Room]) -> float:
    """
    Estimate the cost from room a to room b using the Manhattan distance.

    Args:
        a (str): Name of the start room.
        b (str): Name of the goal room.
        rooms (Dict[str, Room]): Dictionary of Room objects.

    Returns:
        float: Estimated cost between room a and room b.
    """
    ax, ay = rooms[a].x, rooms[a].y
    bx, by = rooms[b].x, rooms[b].y
    return abs(ax - bx) + abs(ay - by)


def astar(
    graph: Dict[str, List[str]],
    start: str,
    goal: str,
    rooms: Dict[str, Room]
) -> Optional[List[str]]:
    """
    Perform A* search to find the shortest path from start to goal.

    Args:
        graph (Dict[str, List[str]]): The graph representation of the house.
        start (str): The starting room name.
        goal (str): The goal room name.
        rooms (Dict[str, Room]): Dictionary of Room objects.

    Returns:
        Optional[List[str]]: A list of room names representing the shortest path, or None if no path exists.
    """
    queue: List = []
    heapq.heappush(queue, (0, start))
    came_from: Dict[str, Optional[str]] = {start: None}
    cost_so_far: Dict[str, float] = {start: 0}

    while queue:
        current_priority, current = heapq.heappop(queue)

        if current == goal:
            # Reconstruct the path
            path: List[str] = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbor in graph[current]:
            # Assume the cost between rooms is 1
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal, rooms)
                heapq.heappush(queue, (priority, neighbor))
                came_from[neighbor] = current

    return None  # No path found