import random
import time


# This function returns board width
def board_width(board):
    return len(board[0])


# This function returns board height
def board_height(board):
    return len(board)


# This function creates a dead board
def dead_board(height, width):
    empty = []
    for i in range(height):
        empty.append([])
        for j in range(width):
            empty[i].append(0)
    return empty


# This function sets a specific board spot to alive
def set_board(board, x, y):
    board[x][y] = 1


# This function creates a board in a random state
def rand_board(height, width):
    rand = dead_board(width, height)
    for i in range(height):
        for j in range(width):
            rand[i][j] = random.randint(0, 1)
    return rand


# This function renders a board
def render(board):
    print(" ", end="")
    for i in range(board_width(board)):
        print("-", end="")

    print("")

    for x in range(board_height(board)):
        print("|", end="")
        for y in range(board_width(board)):
            if board[x][y] == 0:
                print(" ", end="")
            else:
                print("#", end="")
        print("|")

    print(" ", end="")
    for j in range(board_width(board)):
        print("-", end="")

    print("")


# This function up alive neighbors of each spot on a board
def count_board_state(board):
    counter_board = dead_board(board_width(board), board_height(board))
    counter = 0
    # Check each board for its neighbors
    for i in range(board_height(board)):
        for j in range(board_width(board)):
            # Covers all i - 1 neighbors
            if 0 <= i - 1 < board_height(board):
                if board[i - 1][j] == 1:
                    counter += 1
                if 0 <= j - 1 < board_width(board):
                    if board[i - 1][j - 1] == 1:
                        counter += 1
                if 0 <= j + 1 < board_width(board):
                    if board[i - 1][j + 1] == 1:
                        counter += 1

            # Covers all i neighbors
            if 0 <= j - 1 < board_width(board):
                if board[i][j - 1] == 1:
                    counter += 1
            if 0 <= j + 1 < board_width(board):
                if board[i][j + 1] == 1:
                    counter += 1

            # Covers all i + 1 neighbors
            if 0 <= i + 1 < board_height(board):
                if board[i + 1][j] == 1:
                    counter += 1
                if 0 <= j - 1 < board_width(board):
                    if board[i + 1][j - 1] == 1:
                        counter += 1
                if 0 <= j + 1 < board_width(board):
                    if board[i + 1][j + 1] == 1:
                        counter += 1

            # Set each board spot to its # of alive neighbors
            counter_board[i][j] = counter
            counter = 0

    return counter_board


# Function changes a board to its next state
def next_board_state(board):
    # Create counter board
    counter_board = count_board_state(board)

    # Check the counter_boards values to assign next state
    for i in range(board_height(board)):
        for j in range(board_width(board)):
            if board[i][j] == 1:
                if counter_board[i][j] <= 1:
                    board[i][j] = 0
                elif counter_board[i][j] > 3:
                    board[i][j] = 0
            elif counter_board[i][j] == 3:
                board[i][j] = 1


# Function returns false when board is alive, true otherwise
def is_dead(board):
    for i in range(board_height(board)):
        for j in range(board_width(board)):
            if board[i][j] == 1:
                return False

    return True


# Main Function
def main():
    # Asking for input
    height = int(input("Enter a height: "))
    while height < 1:
        print("Invalid height")
        height = int(input("Enter a height: "))
    width = int(input("Enter a width: "))
    while width < 1:
        print("Invalid width")
        width = int(input("Enter a width: "))

    # Produce random board
    rand = rand_board(height, width)
    render(rand)

    # Keep rendering until board dies (which it might not)
    while not is_dead(rand):
        next_board_state(rand)
        time.sleep(0.5)
        render(rand)


# Main
if __name__ == '__main__':
    main()

