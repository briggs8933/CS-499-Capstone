# main.py

"""
Main module for the House Cleaning Adventure game.

This module initializes the game, handles the main game loop,
and coordinates interactions between the player, agent, and rooms.
"""

import pygame
import sys
import time
import hashlib
from constants import *
from room import Room
from player import Player
from utils import render_messages
from agent import Agent
from database import initialize_database, get_connection

def hash_password(password):
    """
    Hashes the password using SHA-256.

    Args:
        password (str): The plaintext password.

    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def validate_username(username):
    """
    Validates the username based on predefined criteria.

    Args:
        username (str): The username input by the player.

    Returns:
        tuple: A tuple containing a boolean indicating validity and an error message if invalid.
    """
    if not username:
        return False, "Username cannot be empty."
    if len(username) < 3 or len(username) > 15:
        return False, "Username must be between 3 and 15 characters."
    if not username.isalnum():
        return False, "Username must contain only letters and numbers."
    return True, ""

def display_error_message(screen, message):
    """
    Display an error message on the screen.

    Args:
        screen (pygame.Surface): The game screen where the message will be displayed.
        message (str): The error message to display.
    """
    screen.fill(BLACK)
    font = pygame.font.Font(None, 32)
    error_surface = font.render(message, True, WHITE)
    screen.blit(error_surface, (SCREEN_WIDTH // 2 - error_surface.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

def title_screen(screen):
    """
    Display the title screen with "New Game" and "Log in" options.

    Args:
        screen (pygame.Surface): The game screen where the title screen will be displayed.

    Returns:
        str: 'new' for New Game, 'login' for Log in.
    """
    pygame.font.init()
    font_title = pygame.font.Font(None, 64)
    font_option = pygame.font.Font(None, 48)
    clock = pygame.time.Clock()
    selected_option = None

    while selected_option is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_option = 'new'
                elif event.key == pygame.K_2:
                    selected_option = 'login'

        screen.fill(BLACK)
        # Render the title
        title_surface = font_title.render("House Cleaning Adventure", True, WHITE)
        subtitle_surface = font_option.render("It's a fight to stay Clean!", True, WHITE)
        option_new = font_option.render("1. New User", True, WHITE)
        option_login = font_option.render("2. Log in", True, WHITE)

        screen.blit(title_surface, (SCREEN_WIDTH // 2 - title_surface.get_width() // 2, 150))
        screen.blit(subtitle_surface, (SCREEN_WIDTH // 2 - subtitle_surface.get_width() // 2, 220))
        screen.blit(option_new, (SCREEN_WIDTH // 2 - option_new.get_width() // 2, 300))
        screen.blit(option_login, (SCREEN_WIDTH // 2 - option_login.get_width() // 2, 350))

        pygame.display.flip()
        clock.tick(30)
    return selected_option

def get_player_credentials(screen, is_new_game=True):
    """
    Display input boxes to get the player's username and password.

    Args:
        screen (pygame.Surface): The game screen where the input boxes will be displayed.
        is_new_game (bool): True if creating a new account, False if logging in.

    Returns:
        tuple: A tuple containing the username and hashed password.
    """
    pygame.font.init()
    font = pygame.font.Font(None, 32)
    input_box_username = pygame.Rect(350, 300, 140, 32)
    input_box_password = pygame.Rect(350, 350, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color_username = color_inactive
    color_password = color_inactive
    active_username = False
    active_password = False
    username = ''
    password = ''
    done = False
    clock = pygame.time.Clock()
    error_message = ""

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_username.collidepoint(event.pos):
                    active_username = not active_username
                    active_password = False
                elif input_box_password.collidepoint(event.pos):
                    active_password = not active_password
                    active_username = False
                else:
                    active_username = False
                    active_password = False
                color_username = color_active if active_username else color_inactive
                color_password = color_active if active_password else color_inactive
            if event.type == pygame.KEYDOWN:
                if active_username:
                    if event.key == pygame.K_RETURN:
                        active_username = False
                        color_username = color_inactive
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif active_password:
                    if event.key == pygame.K_RETURN:
                        active_password = False
                        color_password = color_inactive
                    elif event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode
                if event.key == pygame.K_TAB:
                    # Switch between input boxes
                    if active_username:
                        active_username = False
                        active_password = True
                        color_username = color_inactive
                        color_password = color_active
                    elif active_password:
                        active_password = False
                        active_username = True
                        color_password = color_inactive
                        color_username = color_active
                if event.key == pygame.K_RETURN and not (active_username or active_password):
                    is_valid, error_message = validate_username(username.strip())
                    if is_valid and password.strip():
                        done = True
                    else:
                        error_message = "Please enter valid credentials."
                        username = ''
                        password = ''

        screen.fill(BLACK)
        # Center the prompt text
        prompt_text = "Create New Account" if is_new_game else "Log In"
        if error_message:
            prompt_text = error_message
        prompt_surface = font.render(prompt_text, True, WHITE)
        screen.blit(prompt_surface, (SCREEN_WIDTH // 2 - prompt_surface.get_width() // 2, input_box_username.y - 60))
        # Adjusted label positions
        username_label = font.render("Username:", True, WHITE)
        screen.blit(username_label, (input_box_username.x - 150, input_box_username.y + 5))
        password_label = font.render("Password:", True, WHITE)
        screen.blit(password_label, (input_box_password.x - 150, input_box_password.y + 5))
        # Render the username and password inputs
        txt_surface_username = font.render(username, True, color_username)
        txt_surface_password = font.render('*' * len(password), True, color_password)
        # Adjust input box widths if necessary
        width_username = max(200, txt_surface_username.get_width() + 10)
        width_password = max(200, txt_surface_password.get_width() + 10)
        input_box_username.w = width_username
        input_box_password.w = width_password
        # Blit the input texts
        screen.blit(txt_surface_username, (input_box_username.x + 5, input_box_username.y + 5))
        screen.blit(txt_surface_password, (input_box_password.x + 5, input_box_password.y + 5))
        # Draw the input boxes
        pygame.draw.rect(screen, color_username, input_box_username, 2)
        pygame.draw.rect(screen, color_password, input_box_password, 2)

        pygame.display.flip()
        clock.tick(30)
    return username.strip(), hash_password(password.strip())

def record_game_result(conn, username, time_taken, rooms_cleaned, result):
    """
    Record the result of the game into the GameResults table in the database.

    Args:
        conn (sqlite3.Connection): The database connection.
        username (str): The name of the player.
        time_taken (int): The total time taken by the player to finish the game.
        rooms_cleaned (int): The number of rooms cleaned by the player.
        result (str): The result of the game ('win' or 'lose').
    """
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO GameResults (username, time_taken, rooms_cleaned, result)
        VALUES (?, ?, ?, ?)
    ''', (username, time_taken, rooms_cleaned, result))
    conn.commit()

def display_high_scores(screen, conn):
    """
    Retrieve and display the top high scores on the screen.

    Args:
        screen (pygame.Surface): The game screen where the high scores will be displayed.
        conn (sqlite3.Connection): The database connection.
    """
    scores = get_top_scores(conn)
    messages = ["Top Scores:"]
    for idx, (username, time_taken, rooms_cleaned, result, timestamp) in enumerate(scores, 1):
        minutes, seconds = divmod(time_taken, 60)
        time_str = f"{minutes}m {seconds}s"
        messages.append(f"{idx}. {username} - Time: {time_str}, Rooms Cleaned: {rooms_cleaned}")

    # Clear the screen and display messages
    screen.fill(BLACK)
    render_messages(screen, messages)
    pygame.display.flip()
    pygame.time.delay(5000)

def get_top_scores(conn, limit=5):
    """
    Retrieve the top high scores from the database.

    Args:
        conn (sqlite3.Connection): The database connection.
        limit (int, optional): The maximum number of top scores to retrieve. Defaults to 5.

    Returns:
        list: A list of tuples containing high score information.
    """
    cursor = conn.cursor()
    cursor.execute('''
        SELECT username, time_taken, rooms_cleaned, result, timestamp
        FROM GameResults
        WHERE result = 'win'
        ORDER BY time_taken ASC
        LIMIT ?
    ''', (limit,))
    return cursor.fetchall()

def reset_game_state(conn, username):
    """
    Reset the game state in the database to start a new game.

    Args:
        conn (sqlite3.Connection): The database connection.
        username (str): The name of the player whose game state is to be reset.
    """
    cursor = conn.cursor()
    # Reset player's current room to the starting room
    cursor.execute('UPDATE Players SET current_room = ? WHERE username = ?', ('The Foyer', username))

    # Reset rooms to dirty (set is_clean to 0)
    cursor.execute('UPDATE Rooms SET is_clean = 0')

    # Reset agent's state
    cursor.execute('''
        UPDATE Agent SET
        current_room = ?,
        wait_counter = 0,
        wait_threshold = 2
    ''', ('Kitchen',))  # Starting room for the agent

    conn.commit()

def check_win_condition(player: Player, rooms: dict) -> str | None:
    """
    Check if the player has met the win or lose conditions.

    Args:
        player (Player): The player object.
        rooms (dict): Dictionary of all room objects.

    Returns:
        str: 'win' if the player wins, 'lose' if the player loses, or None if the game should continue.
    """
    # Exclude the Master Bedroom from rooms to clean
    rooms_to_clean = [room for room in rooms.values() if room.name != 'Master Bedroom']
    all_clean = all(room.is_clean for room in rooms_to_clean)

    if all_clean and player.current_room.name == 'Master Bedroom':
        # Player wins if all rooms are clean, and they are in the Master Bedroom
        return 'win'
    elif player.current_room.name == 'Master Bedroom' and not all_clean:
        # Player loses if they go to the Master Bedroom before cleaning all rooms
        return 'lose'
    else:
        # Game continues
        return None

def main() -> None:
    """
    The main function that initializes and runs the game loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("House Cleaning Adventure")
    clock = pygame.time.Clock()

    # Initialize database outside the loop
    initialize_database()
    conn = get_connection()
    conn.execute('PRAGMA foreign_keys = ON')  # Enable foreign key constraints
    cursor = conn.cursor()

    while True:
        # Display title screen and get user choice
        game_mode = title_screen(screen)

        authenticated = False
        while not authenticated:
            # Get player's username and password
            is_new_game = (game_mode == 'new')
            username, hashed_password = get_player_credentials(screen, is_new_game)

            if is_new_game:
                # Check if username already exists
                cursor.execute('SELECT username FROM Players WHERE username = ?', (username,))
                if cursor.fetchone():
                    # Username already exists
                    error_message = "Username already exists. Please choose a different username."
                    display_error_message(screen, error_message)
                    continue  # Loop back to get credentials
                else:
                    # Create new player
                    cursor.execute('''
                        INSERT INTO Players (username, password, current_room)
                        VALUES (?, ?, ?)
                    ''', (username, hashed_password, 'The Foyer'))
                    conn.commit()
                    authenticated = True
            else:
                # Load existing player
                cursor.execute('SELECT password FROM Players WHERE username = ?', (username,))
                row = cursor.fetchone()
                if row and row[0] == hashed_password:
                    # Password matches, proceed
                    authenticated = True
                else:
                    # Authentication failed
                    error_message = "Username or Password incorrect. Please try again."
                    display_error_message(screen, error_message)
                    continue  # Loop back to get credentials

        # Initialize message queue
        messages = [
            f"Welcome, {username}!",
            "Your goal is to clean all 6 rooms and show proof to your Wife in the Master Bedroom!",
            "Move using Arrow keys. Clean a room with the Spacebar."
        ]

        # Check if rooms exist in the database
        cursor.execute('SELECT COUNT(*) FROM Rooms')
        rooms_count = cursor.fetchone()[0]

        if rooms_count == 0:
            # Define the rooms and their positions
            rooms = {
                'The Foyer': Room('The Foyer', 325, 250),
                'Kitchen': Room('Kitchen', 325, 375),
                'Bedroom': Room('Bedroom', 500, 375),
                'Bathroom': Room('Bathroom', 325, 0),
                'Living Room': Room('Living Room', 500, 250),
                'Master Bedroom': Room('Master Bedroom', 500, 125),
                'Backyard': Room('Backyard', 150, 250),
                'Garage': Room('Garage', 500, 0),
            }

            # Define the room connections
            room_connections = [
                ('The Foyer', 'South', 'Kitchen'),
                ('The Foyer', 'North', 'Bathroom'),
                ('The Foyer', 'East', 'Living Room'),
                ('The Foyer', 'West', 'Backyard'),
                ('Kitchen', 'North', 'The Foyer'),
                ('Kitchen', 'East', 'Bedroom'),
                ('Bedroom', 'West', 'Kitchen'),
                ('Bathroom', 'South', 'The Foyer'),
                ('Bathroom', 'East', 'Garage'),
                ('Living Room', 'West', 'The Foyer'),
                ('Living Room', 'North', 'Master Bedroom'),
                ('Master Bedroom', 'South', 'Living Room'),
                ('Backyard', 'East', 'The Foyer'),
                ('Garage', 'West', 'Bathroom'),
            ]

            # Save rooms to the database
            for room in rooms.values():
                room.save_to_db(conn)

            # Save room connections to the database and assign to Room objects
            for from_room, direction, to_room in room_connections:
                cursor.execute('''
                    INSERT INTO RoomConnections (from_room, direction, to_room)
                    VALUES (?, ?, ?)
                ''', (from_room, direction, to_room))
                # Assign connections to Room objects
                rooms[from_room].connections[direction] = to_room
            conn.commit()
        else:
            # Load rooms from the database
            rooms = Room.load_rooms_from_db(conn)

            # Load room connections from the database
            cursor.execute('SELECT from_room, direction, to_room FROM RoomConnections')
            connections = cursor.fetchall()
            for from_room_name, direction, to_room_name in connections:
                if from_room_name in rooms and to_room_name in rooms:
                    rooms[from_room_name].connections[direction] = to_room_name

        # Build the graph representation of the house
        graph = {}
        for room in rooms.values():
            room_name = room.name
            graph[room_name] = []
            for direction, connected_room_name in room.connections.items():
                graph[room_name].append(connected_room_name)

        # Initialize the player
        player = Player.load_from_db(conn, rooms, username)

        # Initialize the agent
        agent = Agent.load_from_db(conn, rooms)

        # Start the game timer
        start_time = time.time()

        # Main game loop
        running = True
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
                        # Attempt to clean the room
                        room_cleaned = player.clean_room(messages)
                        if room_cleaned:
                            # Agent will wait longer if player cleans a room
                            agent.increment_wait_counter()

            # Agent's turn
            agent.move(rooms, graph)
            agent.dirty_room(messages)

            # Check for win/lose condition
            condition = check_win_condition(player, rooms)

            if condition == 'win':
                messages.append("You have cleaned all the rooms and reached the Master Bedroom!")
                messages.append("Wife: Wow, the house looks awesome! Have fun with your friends!")
                render_messages(screen, messages)
                pygame.display.flip()
                pygame.time.delay(5000)

                # Record game result
                end_time = time.time()
                time_taken = int(end_time - start_time)
                rooms_cleaned = sum(1 for room in rooms.values() if room.is_clean)
                record_game_result(conn, username, time_taken, rooms_cleaned, 'win')

                # Reset the game state
                reset_game_state(conn, username)

                # Display high scores
                display_high_scores(screen, conn)

                running = False
                continue
            elif condition == 'lose':
                messages.append("Wife: I thought you were going to clean the house! I really need it cleaned!")
                messages.append("Game over.")
                render_messages(screen, messages)
                pygame.display.flip()
                pygame.time.delay(5000)

                # Record game result
                end_time = time.time()
                time_taken = int(end_time - start_time)
                rooms_cleaned = sum(1 for room in rooms.values() if room.is_clean)
                record_game_result(conn, username, time_taken, rooms_cleaned, 'lose')

                # Reset the game state
                reset_game_state(conn, username)

                # Display high scores
                display_high_scores(screen, conn)

                running = False
                continue

            # Draw rooms
            for room in rooms.values():
                is_current_room = (room == player.current_room)
                has_agent = (room == agent.current_room)
                room.draw(screen, is_current_room, has_agent)

            # Render messages
            render_messages(screen, messages)

            pygame.display.flip()
            clock.tick(FPS)

            # Save game state after each turn
            player.save_to_db(conn, username)
            agent.save_to_db(conn)
            for room in rooms.values():
                room.save_to_db(conn)

        continue  # Go back to the start of the main while loop

    pygame.quit()
    conn.close()

if __name__ == '__main__':
    main()