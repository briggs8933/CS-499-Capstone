# Brian Riggins

import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Displays starting menu
def show_instructions():
    # print a main menu and the commands
    print('-' * 120)
    print('Welcome to the House Cleaning Adventure'.center(120))
    print('-' * 120)
    print('It is Friday night, and you want to go hang out with the friends but the house is stopping you.')
    print('Your goal is to clean/take a picture of all 6 rooms in the house and show proof to your Wife in the Master '
          'Bedroom!'.center(120))
    print('-' * 120)
    print('Do not miss any rooms or it is game over.'.center(120))
    print('-' * 120)
    print('Move through the rooms using the commands: "North", "South", "East", "West", or "Exit"'.center(120))
    print('-' * 120)
    print('Each room needs cleaning, enter "clean" to clean the room and take a picture.'.center(120))
    print('-' * 120)
    print('Good Luck!'.center(120))


# Shows User Room and Pictures Taken
def show_status():
    global room, rooms, pic_list
    print('-' * 120)
    print('-' * 120)
    print('-' * 120)
    print('You are in the {}'.format(room))
    # checks how many items and that play is not in Master Bedroom
    if 'item' in rooms[room] and room != 'Master Bedroom':
        # Give player a status update to head to Master Bedroom
        if len(pic_list) == 6:
            print('-' * 120)
            print('You have collected all the pictures. Go hand them over to your wife in the Master Bedroom.')
            print('-' * 120)
        # Prompts user to clean room if item is not in room and also not in the pic_list
        elif 'item' in rooms[room] and rooms[room]['item'] not in pic_list:
            print('-' * 120)
            print('-' * 120)
            print('It is a mess "clean" it up and take a {}'.format(rooms[room]['item']))
            print('-' * 120)
        else:
            # Status update if there is nothing left to do in room.
            print('-' * 120)
            print('-' * 120)
            print("All clean here. Let's move to the next room.")
            print('-' * 120)
    # Trying to get it to not print a status when entering Master Bedroom
    elif room != 'Master Bedroom':
        print('-' * 120)
        print("This room is clean.")
    # Prints item list for player to see what they have so far
    print('-' * 120)
    print('Cleaned Rooms:', pic_list)
    print('-' * 120)


# Lets user know there is no room in that direction
def invalid_move():
    clear()
    print('*' * 120)
    print('*' * 120)
    print('*' * 120)
    print('*' * 20 + "Trying to escape!?! There is no escape!, please try your move again.".center(80) + '*' * 20)
    print('*' * 120)
    print('*' * 120)
    print('*' * 120)


# Lets user know they have already cleaned that current room
def invalid_item():
    print('*' * 120)
    print('*' * 120)
    print('*' * 120)
    print('*' * 20 + "You cleaned this room already, lets move on!".center(80) + '*' * 20)
    print('*' * 120)
    print('*' * 120)
    print('*' * 120)


# Empty dict for items in game
pic_list = []
# dict for all rooms and items used in game
rooms = {
    'The Foyer': {'South': 'Kitchen', 'North': 'Bathroom', 'East': 'Living Room', 'West': 'Backyard'},
    'Kitchen': {'North': 'The Foyer', 'East': 'Bedroom', 'item': 'Picture of kitchen'},
    'Bedroom': {'West': 'Kitchen', 'item': 'Picture of bedroom'},
    'Master Bedroom': {'South': 'Living Room', 'item': 'Wife'},  # boss of the house
    'Living Room': {'West': 'The Foyer', 'North': 'Master Bedroom', 'item': 'Picture of living room'},
    'Backyard': {'East': 'The Foyer', 'item': 'Picture of flowers'},
    'Bathroom': {'South': 'The Foyer', 'East': 'Garage', 'item': 'Picture of bathroom'},
    'Garage': {'West': 'Bathroom', 'item': 'Picture of garage'}
}
# Starting room for player
room = 'The Foyer'


# main function
def main():
    global room, pic_list

    show_instructions()

    while True:
        #  Clears console for player
        clear()

        # Prompt the player for input
        command = input('Enter a command ("North", "South", "East", "West", or "Exit" , if room needs cleaning '
                        '"clean"): ')

        # Check if the command is to move
        if command in rooms[room]:
            room = rooms[room][command]
            show_status()  # Prints fresh status
        # Checks if player enters clean calls invalid_item()
        elif command.lower() == 'clean':
            if 'item' in pic_list:
                invalid_item()
            # If the room does not have an Item in dict this will print
            elif 'item' not in rooms[room]:
                print('*' * 120)
                print('*' * 120)
                print('*' * 120)
                print('*' * 20 + "This room doesn't need cleaning. Try moving to another room.".center(80) + '*' * 20)
                print('*' * 120)
                print('*' * 120)
                print('*' * 120)
            # Calls invalid_item() if item in room is already in pic_list
            elif rooms[room]['item'] in pic_list:
                invalid_item()
            # Adds item to list
            else:
                pic_list.append(rooms[room]['item'])
                print('You cleaned the room and took a', rooms[room]['item'])
                show_status()

        # Check if the command is to exit
        elif command.lower() == 'exit':
            clear()
            print('*' * 120)
            print('*' * 120)
            print('*' * 120)
            print('*' * 20 + "Aww leaving so soon, see you next time!".center(80) + '*' * 20)
            print('*' * 120)
            print('*' * 120)
            print('*' * 120)
            break

        # Handle invalid commands
        else:
            invalid_move()

        # Check for lose condition
        if room == 'Master Bedroom' and len(pic_list) < 6:
            print('*' * 120)
            print('*' * 120)
            print('*' * 120)
            print('*' * 120)
            print('*' * 5 + "Wife: I thought you were going to clean the house,I really need it cleaned!".center(110) +
                  '*' * 5)
            print('*' * 120)
            print('*' * 20 + "Game over.".center(80) + '*' * 20)
            print('*' * 120)
            print('*' * 120)
            break

        # Check for win condition
        else:
            if room == 'Master Bedroom' and len(pic_list) == 6:
                print('*' * 120)
                print('*' * 120)
                print('*' * 120)
                print('*' * 20 + "Wife: Wow the house looks awesome! Have fun with your friends!".center(80) + '*' * 20)
                print('*' * 120)
                print('*' * 20 + "You won the Game!!".center(80) + '*' * 20)
                print('*' * 120)
                print('*' * 120)
                break


if __name__ == '__main__':
    main()
