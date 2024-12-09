# database.py

import sqlite3

DB_NAME = 'game.db'


def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create Players table
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Players (
                player_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                current_room TEXT NOT NULL
            )
        ''')

    # Create Rooms table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Rooms (
            room_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            x_coordinate INTEGER NOT NULL,
            y_coordinate INTEGER NOT NULL,
            is_clean INTEGER NOT NULL
        )
    ''')

    # Create Agent table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Agent (
            agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
            current_room TEXT NOT NULL,
            wait_counter INTEGER NOT NULL,
            wait_threshold INTEGER NOT NULL
        )
    ''')

    # Create RoomConnections table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS RoomConnections (
            from_room TEXT NOT NULL,
            direction TEXT NOT NULL,
            to_room TEXT NOT NULL,
            PRIMARY KEY (from_room, direction),
            FOREIGN KEY (from_room) REFERENCES Rooms(name),
            FOREIGN KEY (to_room) REFERENCES Rooms(name)
        )
    ''')

    # Create GameResults table
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS GameResults (
                result_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                time_taken INTEGER,
                rooms_cleaned INTEGER,
                result TEXT,  -- 'win' or 'lose'
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

    conn.commit()
    conn.close()


def get_connection():
    return sqlite3.connect(DB_NAME)