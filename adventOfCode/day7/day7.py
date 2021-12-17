import math


def inputs(path):
    """
    read inputs into a list of integers
    :param path: path of inputs
    :return: list of integers and max integer in list
    """
    inpts = list(map(int, open(path).read().split(',')))
    return inpts, max(inpts)


def cost_to_move(src, dest, part=1):
    """

    :param src: move from src...
    :param dest: ... to dest
    :param part: part of problem currently solving
    :return: cost of move
    """
    # in part 1, the cost to move from a to b is abs(a-b)
    if part == 1:
        return abs(src - dest)

    # in part 2, the cost is an arithmetic series
    d = abs(src - dest)
    return d * (d + 1) / 2


def solve(initial_state, mx, n, part):
    """
    Running time : O(N*mx)
    Space : O(N*mx)
    :param initial_state: array of submarines horizontal positions
    :param mx: max horizontal position
    :param n: number of subs
    :param part: part of problem currently solving
    :return: print the min fuel cost and index @ which it occurs
    """
    # create dp table
    # subproblem: dp[i,j] := cost of aligning first j subs at position i
    dp = [[cost_to_move(initial_state[0], i, part) if j == 0 else None for j in range(n)] for i in range(mx + 1)]

    # cost of aligning first j-1 subs at position i + the cost of aligning sub j at position i
    for i in range(mx + 1):
        for j in range(1, n):
            dp[i][j] = dp[i][j - 1] + cost_to_move(initial_state[j], i, part)

    # answer is minimum of last column (where j==n-1)
    min_cost = math.inf
    mindex = None
    for i in range(mx + 1):
        if dp[i][n - 1] < min_cost:
            min_cost = dp[i][n - 1]
            mindex = i

    print('min cost:', min_cost, '@ index:', mindex)


if __name__ == '__main__':
    # read array and get max and min
    initial_state, mx = inputs('input.txt')
    n = len(initial_state)

    # in part 1, the cost to move from a to b is abs(a-b)
    solve(initial_state, mx, n, 1)

    # in part 2, the cost is an arithmetic series
    solve(initial_state, mx, n, 2)
