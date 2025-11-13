player_ley = 0
player_macho = 0
treasure_x = 15
treasure_y = 3
game_running = True
print("Welcome to Calbo's Maze!")
print(f"Find the treasure at ({treasure_x}, {treasure_y})!")
while game_running:
    move = input("Enter move (up/down/left/right): ").lower()

    if move == "up":
        player_y += 1
    elif move == "down":
        player_y -= 1
    elif move == "left":
        player_x -= 1
    elif move == "right":
        player_x += 1
    elif move == "q":
        print("see you next time!")
    else:
        print("Invalid move! Try again.")
        continue

    print(f"Player position: ({player_ley}, {player_macho})")

    if player_ley == treasure_x and player_macho == treasure_y:
        print("Congratulations! You found the treasure!")
        game_running = False

