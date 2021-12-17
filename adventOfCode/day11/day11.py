def inputs(path):
    """
    read inputs into a list readings and results
    :param path: path of inputs
    :return: dictionary mapping readings to results
    """
    fl = open(path, 'r').readlines()
    d = {}
    for row in range(len(fl)):
        for cell in range(len(fl[row].strip())):
            d[(row, cell)] = int(fl[row][cell])
    return d



def part1and2():
    count = 0
    time = 0
    all_exploded = False
    while time < 100 or not all_exploded:
        exploded_set = set()
        for pos in grid:
            grid[pos] += 1
            if grid[pos] == 10:
                explode(pos, exploded_set)
        count += len(exploded_set)
        if len(exploded_set) == len(grid):
            all_exploded = True

        for point in exploded_set:
            grid[point] = 0

        time += 1
        if time == 100:
            print(count,'explosions in first 100 seconds')
    print('all exploded @',time)


def explode(point, exploded_set):
    exploded_set.add(point)
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                if (point[0] + i, point[1] + j) in grid:
                    grid[(point[0] + i, point[1] + j)] += 1
                    if grid[(point[0] + i, point[1] + j)] == 10:
                        explode((point[0] + i, point[1] + j), exploded_set)


if __name__ == '__main__':
    grid = inputs('input.txt')
    part1and2()
