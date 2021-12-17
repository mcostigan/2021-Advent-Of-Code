import math
import networkx


def inputs(path):
    """
    read inputs into a list readings and results
    :param path: path of inputs
    :return: dictionary mapping readings to results
    """
    fl = open(path, 'r').readlines()
    l = []
    for ln in fl:
        l.append(list(ln.strip()))
    return l


def part1():
    score = 0
    for status in statuses:
        if status[0] != 'Incomplete':
            score += cls[status[1]]['points']
    print(score)


def part2():
    scores = []
    for status in statuses:
        if status[0] == 'Incomplete':
            score = 0
            for char in status[1][::-1]:
                score *= 5
                score += opn[char]['points']
            scores.append(score)

    scores.sort()
    print(scores[len(scores)//2])


def process_lines():
    status = []
    for syn in syntax:
        err = False
        start = []
        for char in syn:
            if char in opn:
                start.append(char)
            if char in cls:
                if start[-1] == cls[char]['start']:
                    start.pop()
                else:
                    err = True
                    break
        if err:
            status.append(('Corrupted', char))
        else:
            status.append(('Incomplete', start))
    return status


if __name__ == '__main__':
    syntax = inputs('input.txt')
    opn = {'{': {'end': '}', 'points': 3},
           '(': {'end': ')', 'points': 1},
           '[': {'end': ']', 'points': 2},
           '<': {'end': '>', 'points': 4}}
    cls = {'}': {'start': '{', 'points': 1197},
           ')': {'start': '(', 'points': 3},
           ']': {'start': '[', 'points': 57},
           '>': {'start': '<', 'points': 25137}}
    statuses = process_lines()
    part1()
    part2()
