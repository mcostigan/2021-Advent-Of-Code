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
    # get score of corrupted lines
    score = 0

    # for each corrupted line
    for status in statuses:
        if status[0] != 'Incomplete':
            # add points associated with character
            score += cls[status[1]]['points']
    print('Corrupted score:',score)


def part2():
    # create an array of scores
    scores = []

    # for each incomplete record
    for status in statuses:
        if status[0] == 'Incomplete':
            # calculate score of every unprocessed start record
            score = 0
            for char in status[1][::-1]:
                score *= 5
                score += opn[char]['points']

            # add to list
            scores.append(score)

    # sort to find median
    scores.sort()
    print('Median incomplete score:',scores[len(scores)//2])


def process_lines():
    # create output list
    status = []

    # for each input
    for syn in syntax:
        # check if incomplete or corrupted
        err = False
        start = []

        # for each char in line
        for char in syn:
            # if an opening, append
            if char in opn:
                start.append(char)
            # else check if it matches the last added opening
            if char in cls:
                if start[-1] == cls[char]['start']:
                    # if yes, pop
                    start.pop()
                else:
                    # else, corrupted
                    err = True
                    break

        # add status and either (first noticed corruption) OR (list of unclosed opens)
        if err:
            status.append(('Corrupted', char))
        else:
            status.append(('Incomplete', start))

    return status


if __name__ == '__main__':
    syntax = inputs('input.txt')
    # create mapping of openings to closings and points
    opn = {'{': {'end': '}', 'points': 3},
           '(': {'end': ')', 'points': 1},
           '[': {'end': ']', 'points': 2},
           '<': {'end': '>', 'points': 4}}
    # create mapping of closings to openings and points
    cls = {'}': {'start': '{', 'points': 1197},
           ')': {'start': '(', 'points': 3},
           ']': {'start': '[', 'points': 57},
           '>': {'start': '<', 'points': 25137}}
    # process each line
    statuses = process_lines()
    part1()
    part2()
