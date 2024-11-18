# player.py

class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move(self, direction, rooms, messages):
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

    def clean_room(self, messages):
        if not self.current_room.is_clean:
            self.current_room.is_clean = True
            message = f"You cleaned the {self.current_room.name} and took a picture."
            print(message)
            messages.append(message)
        else:
            message = f"You cleaned this room already. Let's move on!"
            print(message)
            messages.append(message)