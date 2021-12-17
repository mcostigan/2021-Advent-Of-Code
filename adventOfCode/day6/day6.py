def inputs(path):
    """

    :param path: path of input file
    :return: dictionary mapping time value of fish to frequncy
    """
    d = {i: 0 for i in range(10)}
    inpts = map(int, open(path).read().split(','))

    for i in inpts:
        d[i] += 1

    return d


if __name__ == '__main__':
    """
    Running time : O(10*days)=O(days)
    Space : O(10*days)=O(days)
    """
    # create initial state as frequency distribution
    initial_state = inputs('input.txt')

    # set number of days to model
    days = 256

    # create dp table with first row as base case (initial state)
    # dummy 10th row for easy recurrence -- always 0
    dp = [[initial_state[i] if j == 0 else 0 for j in range(days + 1)] for i in range(10)]

    # i := # of fish @ age i
    # j := # of days since initial state
    for j in range(1, days + 1):
        for i in range(9):
            # yesterday's count of fish of age = i+1
            dp[i][j] = dp[i + 1][j - 1]

            # if i is 6 or 8, add in fish that have spawned from yesterday's 0 age fish
            if i in (6, 8):
                dp[i][j] += dp[0][j - 1]

    # get sum of last column
    s = 0
    for i in range(9):
        s += dp[i][days]

    # print answer
    print(s,'lanternfish @ t=',days)
