import random


def board_width(board):
    return len(board[0])


def board_height(board):
    return len(board)


def dead_board(height, width):
    empty = []
    for i in range(height):
        empty.append([])
        for j in range(width):
            empty[i].append(0)
    return empty


def set_board(board, x, y):
    board[x][y] = 1


def rand_board(height, width):
    rand = dead_board(width, height)
    for i in range(height):
        for j in range(width):
            rand[i][j] = random.randint(0, 1)
    return rand


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


def next_board_state(board):
    counter_board = dead_board(board_width(board), board_height(board))
    counter = 0
    for i in range(board_height(board)):
        for j in range(board_width(board)):
            if board[i][j] == 1:
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

                counter_board[i][j] = counter
                counter = 0

    return counter_board

    # board[i - 1][j - 1]
    # board[i - 1][j]
    # board[i - 1][j + 1]

    # board[i][j - 1]
    # board[i][j + 1]

    # board[i + 1][j - 1]
    # board[i + 1][j]
    # board[i + 1][j + 1]


def main():
    width = 5
    height = 5
    # rand = rand_board(width, height)
    rand = dead_board(height, width)
    set_board(rand, 2, 2)
    set_board(rand, 0, 0)
    set_board(rand, 1, 0)
    render(rand)
    counter_board = next_board_state(rand)
    print(counter_board)


if __name__ == '__main__':
    main()

