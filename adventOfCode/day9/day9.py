import math
import networkx


def inputs(path):
    """
    read inputs into a list readings and results
    :param path: path of inputs
    :return: dictionary mapping readings to results
    """
    fl = open(path, 'r').readlines()
    l = [[math.inf] * (len(fl[0].strip()) + 2)]
    for ln in fl:
        line = [math.inf] + list(map(int, ln.strip())) + [math.inf]
        l.append(line)
    l.append([math.inf] * (len(fl[0].strip()) + 2))
    return l


def part1():
    low_points = find_local_mins()
    risk = 0
    for point in low_points:
        risk += cave_map[point[0]][point[1]] + 1
    print(risk, 'total risk of low points')


def part2():
    d = {}
    for i in range(len(cave_map)):
        for j in range(len(cave_map[0])):
            if (i, j) not in d:
                if cave_map[i][j] < 9:
                    d[(i,j)] = (i,j)
                    visit(i, j, d, (i,j))

    basins = {}
    for key in d:
        basins[d[key]] = basins.get(d[key],0) + 1

    top3 = [1,1,1]
    for basin in basins:
        if basins[basin]>top3[0]:
            top3[0] = basins[basin]
            top3.sort()
    print(top3[0]*top3[1]*top3[2])


def visit(r, c, d, parent):
    if r < 0 or c < 0:
        return

    d[(r, c)] = parent
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 or j == 0:
                if (r+i, c+j) not in d and cave_map[r+i][c+j]<9:
                    visit(r+i, c+j, d,parent)


def find_local_mins():
    local_mins = []

    for row in range(1, len(cave_map) - 1):
        for cell in range(1, len(cave_map[row]) - 1):
            if is_min(row, cell):
                local_mins.append((row, cell))

    return local_mins


def is_min(r, c):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                if cave_map[r][c] > cave_map[r + i][c + j]:
                    return False
    return True


if __name__ == '__main__':
    cave_map = inputs('input.txt')
    part1()
    part2()
