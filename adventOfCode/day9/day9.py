import math


def inputs(path):
    """
    create a grid representing depths
    :param path: path of inputs
    :return: list of lists of depths
    """
    # open file
    fl = open(path, 'r').readlines()

    # add padding line (for easy comparison)
    l = [[math.inf] * (len(fl[0].strip()) + 2)]

    for ln in fl:
        # add padding cols to left and right
        line = [math.inf] + list(map(int, ln.strip())) + [math.inf]
        l.append(line)

    # add padding line
    l.append([math.inf] * (len(fl[0].strip()) + 2))

    return l


def part1():
    # find all local mins and sum up depths +1
    low_points = find_local_mins()
    risk = 0
    for point in low_points:
        risk += cave_map[point[0]][point[1]] + 1
    print(risk, 'total risk of low points')


def part2():
    """
    essentially a modified DFS: find the "connected components" of the grid
    each cell is visited at most once, and constant time work in each cell, so O(mn) running time
    :return:
    """
    d = {}
    # for each cell
    for i in range(len(cave_map)):
        for j in range(len(cave_map[0])):
            # if not already visited
            if (i, j) not in d:
                # and is not height 9
                if cave_map[i][j] < 9:
                    # then is part of its own cc
                    d[(i, j)] = (i, j)
                    # visit all adjacent cells and label as being part of this cc
                    visit(i, j, d, (i, j))

    # get a dict of all basins by size
    basins = {}
    for key in d:
        basins[d[key]] = basins.get(d[key], 0) + 1

    # get the top 3 values, using a sorted list of size 3
    top3 = [1, 1, 1]
    for basin in basins:
        if basins[basin] > top3[0]:
            top3[0] = basins[basin]
            top3.sort()

    print('Product of largest basins:', top3[0] * top3[1] * top3[2])


def visit(r, c, d, parent):
    """
    recursively 'visit' a cell and all cells reachable from that cell
    :param r: row
    :param c: column
    :param d: grid dictionary
    :param parent: connected component value
    :return:
    """
    # base case, exit if outside grid
    if r < 0 or c < 0:
        return

    # add cell to dictionary and assign connected component value
    d[(r, c)] = parent

    # visit all of its adjacent cells
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 or j == 0:
                if (r + i, c + j) not in d and cave_map[r + i][c + j] < 9:
                    visit(r + i, c + j, d, parent)


def find_local_mins():
    # list of coordinates of local minima
    local_mins = []

    # for each cell
    for row in range(1, len(cave_map) - 1):
        for cell in range(1, len(cave_map[row]) - 1):
            # add if is min
            if is_min(row, cell):
                local_mins.append((row, cell))

    return local_mins


def is_min(r, c):
    # check all of adjacent cells
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                if cave_map[r][c] > cave_map[r + i][c + j]:
                    # if find something smaller, then not a local minimum
                    return False
    # else, is a local minimum
    return True


if __name__ == '__main__':
    cave_map = inputs('input.txt')
    part1()
    part2()
