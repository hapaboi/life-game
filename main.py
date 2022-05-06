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


def main():
    width = 6
    height = 5
    rand = rand_board(width, height)
    print(rand)


if __name__ == '__main__':
    main()

