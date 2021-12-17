def inputs():
    """

    :return: a list of commands (tuples): (direction, distance)
    """
    fl = open('input.txt')
    return [ln.strip().split(' ') for ln in fl]


def part1():
    """

    :return: product of horizontal and vertical coordinates
    """
    for command in commands:
        if command[0] == 'forward':
            coordinates['horizontal'] += int(command[1])
        else:
            coordinates['depth'] += int(command[1]) * (1 if command[0] == 'down' else -1)

    return coordinates['horizontal'] * coordinates['depth']


def part2():
    """

    :return: product of horizontal and vertical coordinates
    """
    aim = 0
    for command in commands:
        if command[0] == 'forward':
            coordinates['horizontal'] += int(command[1])
            coordinates['depth'] += int(command[1]) * aim
        else:
            aim += int(command[1]) * (1 if command[0] == 'down' else -1)

    return coordinates['horizontal'] * coordinates['depth']


if __name__ == '__main__':
    commands = inputs()

    coordinates = {'horizontal': 0, 'depth': 0}
    print(part1())

    coordinates = {'horizontal': 0, 'depth': 0}
    print(part2())
