def dead_board(width, height):
    empty = []
    for i in range(height):
        empty.append([])
        for j in range(width):
            empty[i].append(0)
    return empty


def main():
    width = 5
    height = 5
    dead = dead_board(width, height)
    print(dead)


if __name__ == '__main__':
    main()

