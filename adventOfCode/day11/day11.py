def inputs(path):
    """
    read inputs into a grid dictionary
    :param path: path of inputs
    :return: dictionary mapping coordinates to energy level
    """
    # open file
    fl = open(path, 'r').readlines()

    # create dictionary of coordinates to energy level
    d = {}
    for row in range(len(fl)):
        for cell in range(len(fl[row].strip())):
            d[(row, cell)] = int(fl[row][cell])

    return d


def part1and2():
    # set count and time to 0
    count = 0
    time = 0
    # start @ false, becomes true when all flash @ same time
    all_flashd = False

    # find number of explosions in first 100 seconds and time at which all flash
    while time < 100 or not all_flashd:
        # create a set of flashd coordinates
        flashd_set = set()
        # loop through grid
        for pos in grid:
            # increment energy level
            grid[pos] += 1
            # if energy level is 10, then flash
            if grid[pos] == 10:
                flash(pos, flashd_set)
        # add number of flashes to count
        count += len(flashd_set)

        # if all flashed, switch boolean
        if len(flashd_set) == len(grid):
            all_flashd = True

        # set everything that flashed to 0
        for point in flashd_set:
            grid[point] = 0

        # increment time
        time += 1
        if time == 100:
            print(count, 'explosions in first 100 seconds')
    print('all flashed @', time)


def flash(point, flashd_set):
    # add point to set
    flashd_set.add(point)
    # for all adjacent cells...
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                if (point[0] + i, point[1] + j) in grid:
                    # ... increment energy level
                    grid[(point[0] + i, point[1] + j)] += 1
                    # if energy level is 10, flash
                    if grid[(point[0] + i, point[1] + j)] == 10:
                        flash((point[0] + i, point[1] + j), flashd_set)


if __name__ == '__main__':
    grid = inputs('input.txt')
    part1and2()
