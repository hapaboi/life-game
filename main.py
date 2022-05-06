import random


def dead_board(width, height):
    empty = []
    for i in range(height):
        empty.append([])
        for j in range(width):
            empty[i].append(0)
    return empty


def rand_board(width, height):
    rand = dead_board(width, height)
    for i in range(height):
        for j in range(width):
            rand[i][j] = random.randint(0, 1)
    return rand


def render(board):
    print(" ", end="")
    for i in range(len(board[0])):
        print("-", end="")

    print("")

    for x in range(len(board)):
        print("|", end="")
        for y in range(len(board[0])):
            if board[x][y] == 0:
                print(" ", end="")
            else:
                print("#", end="")
        print("|")

    print(" ",end="")
    for j in range(len(board[0])):
        print("-", end="")


def main():
    width = 5
    height = 5
    rand = rand_board(width, height)
    render(rand)


if __name__ == '__main__':
    main()

