import math


def inputs():
    fl = open('input.txt')
    return [ln.strip() for ln in fl]


def bin_to_dec(s):
    res = 0
    for i in range(len(s)):
        if s[i] == '1':
            res += 2 ** (len(s) - 1 - i)
    return res


def part1():
    for i in range(len(l)):
        for j in range(len(l[i])):
            char = int(l[i][j])
            d[j][char] += 1

    gamma = ''.join(['0' if d[i][0] > d[i][1] else '1' for i in range(len(l[0]))])
    g_val = bin_to_dec(gamma)
    return gamma


def part2():
    tmp = l[:]
    i = 0

    while len(tmp) > 1:
        d_prime = {'0': 0, '1': 0}
        for t in tmp:
            d_prime[t[i]] += 1

        val = '0' if d_prime['0'] > d_prime['1'] else '1'
        tmp = [t for t in tmp if t[i] == val]

        i += 1
    print(tmp[0])
    g = bin_to_dec(tmp[0])

    tmp = l[:]
    i = 0
    while len(tmp) > 1:
        d_prime = {'0': 0, '1': 0}
        for t in tmp:
            d_prime[t[i]] += 1

        val = '0' if d_prime['0'] <= d_prime['1'] else '1'
        tmp = [t for t in tmp if t[i] == val]

        i += 1

    print(tmp[0])
    e = bin_to_dec(tmp[0])

    print(g*e)




if __name__ == '__main__':
    l = inputs()
    d = {i: {0: 0, 1: 0} for i in range(len(l[0]))}
    part1()
    print(d)
    part2()
