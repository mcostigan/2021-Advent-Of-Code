import math


def inputs(path):
    """
    read inputs into a set of dots and list of instructions
    :param path: path of inputs
    :return: set of dot coordinates and list of lists, representing commands
    """

    # open file
    fl = open(path, 'r').readlines()

    # add each dot to set
    d = set()
    for ln in range(len(fl)):
        # if blank line, then move on to instructions
        if fl[ln].strip() == '':
            break

        x, y = map(int, fl[ln].strip().split(','))
        d.add((x, y))

    # create a list of instructions by extracting everything on or after position 11 and splitting on '='
    l = [fl[command].strip()[11:].split('=') for command in range(ln + 1, len(fl))]

    return d, l


def part1and2(dots):
    # store grid size
    grid_x = math.inf
    grid_y = math.inf

    # for each command
    for command in commands:
        # fold vertically or horizontally, update grid size
        if command[0] == 'y':
            grid_y = int(command[1])
            fold_horizontal(int(command[1]))
        else:
            grid_x = int(command[1])
            fold_vertical(int(command[1]))
        # print # of visible dots after each fold
        print('# of dots visible after fold @','='.join(command),':',len(dots))

    # print secret message
    print()
    for x in range(grid_y):
        # star if coordinates exist in dots, else empty
        print(''.join(["* " if (y,x) in dots else "  " for y in range(grid_x)]))



def fold_horizontal(y):
    # store coordinates to add and delete
    changes = {}

    # for each dot in dots
    for cell in dots:
        # check if it is under the fold
        if cell[1] >= y:
            # calculate "mirror" position and add that cell to dots
            diff = cell[1] - y
            changes[(cell[0], cell[1] - 2 * diff)] = 'add'
            # remove current cell
            changes[cell] = 'remove'

    # for each change, add or delete a dot
    for change in changes:
        if changes[change] == 'add':
            dots.add(change)
        else:
            dots.remove(change)


def fold_vertical(x):
    # store coordinates to add and delete
    changes = {}

    # for each dot in dots
    for cell in dots:
        # check if it is right of the fold
        if cell[0] >= x:
            # calculate "mirror" position and add that cell to dots
            diff = cell[0] - x
            changes[(cell[0] - 2 * diff, cell[1])] = 'add'
            # remove current cell
            changes[cell] = 'remove'

    # for each change, add or delete a dot
    for change in changes:
        if changes[change] == 'add':
            dots.add(change)
        else:
            dots.remove(change)


if __name__ == '__main__':
    dots, commands = inputs('input.txt')
    part1and2(dots)
