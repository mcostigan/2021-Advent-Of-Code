def inputs():
    fl = open('input.txt')
    return [int(ln.strip()) for ln in fl]


def part1(depths):
    """

    :param depths: list of depths
    :return: number of times the depth increases
    """
    cnt = 0
    for depth in range(1, len(depths)):
        cnt += 1 if depths[depth] > depths[depth - 1] else 0
    return cnt


def part2(depths):
    """

    :param depths: list of depths
    :return: number of times a sliding window of 3 depths increases
    """
    cnt = 0
    for depth in range(3, len(depths)):
        cnt += 1 if depths[depth] > depths[depth - 3] else 0
    return cnt


if __name__ == '__main__':
    input_depths = inputs()
    print(part1(input_depths))
    print(part2(input_depths))
