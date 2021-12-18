import math


def inputs(path):
    """
    read inputs into a dictionary of pairs to rules
    :param path: path of inputs
    :return: a dictionary mapping pairs to insertion character and the initial template string
    """

    # open file
    fl = open(path, 'r').readlines()

    # extract template
    s = fl[0].strip()

    # add each pair and rule to dictionary
    d = {}
    for ln in fl[2:]:
        x, y = ln.strip().split(' -> ')
        d[x] = y

    return d, s


def part1(template):
    # get initial frequency of individual chars
    frequency = histogram(template)

    # maintain two histograms of pairs
    # current_frequency to track the frequency of pairs in the current iteration
    # tmp_frequency to track the frequency of pairs in the next iteration
    # at the end of each iterations current -< tmp and tmp<-{}
    current_frequency = {}
    tmp_frequency = {}
    for i in range(len(template) - 1):
        current_frequency[template[i:i + 2]] = current_frequency.get(template[i:i + 2], 0) + 1

    # for each step
    for step in range(1, 41):
        # for each pair of chars
        for pair in current_frequency:
            # find the insertion char
            rule = pairs[pair]
            # add an occurrence of the first char in the pair and the rule to the tmp histogram for each time the pair appears
            tmp_frequency[pair[0] + rule] = tmp_frequency.get(pair[0] + rule, 0) + current_frequency[pair]
            # add an occurrence of the rule and the second char to the tmp histogram for each time the pair appears
            tmp_frequency[rule + pair[1]] = tmp_frequency.get(rule + pair[1], 0) + current_frequency[pair]
            # add to the frequency of the rule
            frequency[rule] = frequency.get(rule, 0) + current_frequency[pair]

        # assign the tmp dict to current
        current_frequency = {key: tmp_frequency[key] for key in tmp_frequency}
        # reset tmp frequency
        tmp_frequency = {}

    # print result
    print(hist_min_max(frequency), 'after', step, 'iterations')


def histogram(s):
    """

    :param s: string of characters
    :return: histogram mapping each distinct character to its frequency
    """
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def hist_min_max(h):
    """

    :param h: histogram of characters and frequencies
    :return: the max frequency less the min frequency
    """
    min_hist = math.inf
    max_hist = -math.inf
    for key in h:
        max_hist = max(max_hist, h[key])
        min_hist = min(min_hist, h[key])
    return max_hist - min_hist


if __name__ == '__main__':
    pairs, template_string = inputs('input.txt')
    part1(template_string)
