# main.py

import pygame
import sys
from constants import *
from room import Room
from player import Player
from utils import render_messages

def check_win_condition(player, rooms):
    rooms_to_clean = [room for room in rooms.values() if room.name != 'Master Bedroom']
    all_clean = all(room.is_clean for room in rooms_to_clean)

    if all_clean and player.current_room.name == 'Master Bedroom':
        return 'win'
    elif player.current_room.name == 'Master Bedroom' and not all_clean:
        return 'lose'
    else:
        return None

def main():
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("House Cleaning Adventure")

    # Initialize message queue
    messages = []
    messages.append("Welcome to the House Cleaning Adventure")
    messages.append("Your goal is to clean all 6 rooms and show proof to your Wife in the Master Bedroom!")
    messages.append("Move using Arrow keys. Clean a room with the Spacebar.")

    # Define the rooms and their positions
    rooms = {
        'The Foyer': Room('The Foyer', 325, 250, {'South': 'Kitchen', 'North': 'Bathroom', 'East': 'Living Room', 'West': 'Backyard'}),
        'Kitchen': Room('Kitchen', 325, 375, {'North': 'The Foyer', 'East': 'Bedroom'}),
        'Bedroom': Room('Bedroom', 500, 375, {'West': 'Kitchen'}),
        'Bathroom': Room('Bathroom', 325, 0, {'South': 'The Foyer', 'East': 'Garage'}),
        'Living Room': Room('Living Room', 500, 250, {'West': 'The Foyer', 'North': 'Master Bedroom'}),
        'Master Bedroom': Room('Master Bedroom', 500, 125, {'South': 'Living Room'}),
        'Backyard': Room('Backyard', 150, 250, {'East': 'The Foyer'}),
        'Garage': Room('Garage', 500, 0, {'West': 'Bathroom'}),
    }

    # Initialize the player in The Foyer
    player = Player(rooms['The Foyer'])

    # Main game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP):
                    player.move('North', rooms, messages)
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    player.move('South', rooms, messages)
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    player.move('West', rooms, messages)
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    player.move('East', rooms, messages)
                elif event.key == pygame.K_SPACE:
                    player.clean_room(messages)

        # Check for win/lose condition
        condition = check_win_condition(player, rooms)
        if condition == 'win':
            messages.append("You have cleaned all the rooms and reached the Master Bedroom!")
            messages.append("Wife: Wow, the house looks awesome! Have fun with your friends!")
            render_messages(screen, messages)
            pygame.display.flip()
            pygame.time.delay(5000)
            running = False
            continue
        elif condition == 'lose':
            messages.append("Wife: I thought you were going to clean the house! I really need it cleaned!")
            messages.append("Game over.")
            render_messages(screen, messages)
            pygame.display.flip()
            pygame.time.delay(5000)
            running = False
            continue

        # Draw rooms
        for room in rooms.values():
            is_current_room = (room == player.current_room)
            room.draw(screen, is_current_room)

        # Render messages
        render_messages(screen, messages)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()