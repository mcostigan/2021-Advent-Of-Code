import networkx


def inputs(path):
    """
    read inputs into a list readings and results
    :param path: path of inputs
    :return: dictionary mapping readings to results
    """
    fl = open(path, 'r').readlines()
    d = {}
    for ln in fl:
        key_value = ln.strip().split(' | ')
        d[tuple(key_value[0].split())] = key_value[1].strip().split()
    return d


def part1():
    # get count of unique readings in input
    results = 0
    for reading in readings:
        for result in readings[reading]:
            if len(result) in (2, 4, 3, 7):
                results += 1
    print(results, 'instances of 1,4,7, or 8')


def part2():
    # create running sum
    answer = 0

    # for each reading in input
    for reading in readings:
        # map chars to correct chars {chars: correctchar}
        solution = {}

        # get frequency analysis
        freq, uniq_freq = frequency_analysis(reading)

        # loop through keys in freq
        for key in freq:
            # if char is of unique frequency
            if len(frequency[freq[key]]) == 1:
                # map solution
                solution[key] = frequency[freq[key]][0]
            else:
                # key is of a unique frequency among 1,4,7,8
                if frequency[freq[key]] == ['g', 'd']:
                    # if either g or d, d appears twice in 1,4,7,8
                    if uniq_freq[key] == 2:
                        solution[key] = 'd'
                    else:
                        solution[key] = 'g'
                else:
                    # and a appears twice in 1,4,7,8
                    if uniq_freq[key] == 2:
                        solution[key] = 'a'
                    else:
                        solution[key] = 'c'

        # use solution to get resulting four digit display value
        result = 0
        # for each digit
        for i in range(4):
            digit = readings[reading][i]
            s = ''
            # for each letter in digit
            for char in digit:
                # lookup in solution
                s += solution[char]
            # sort for consistency and lookup in mapping
            number = numbers[''.join(sorted(s))]

            # add digit to result
            result += number * 10 ** (3 - i)
        # add result to final answer
        answer += result
    print(answer, 'sum of all readings')


def frequency_analysis(t):
    # find the frequency of each letter in all 10 readings and the frequency of each letter in readings of unique length
    freq = {}
    uniq_freq = {}

    # for each reading
    for reading in t:
        # for each letter in reading
        for char in reading:
            # increment count
            freq[char] = freq.get(char, 0) + 1

            # if reading is a unique length
            if len(reading) in (2, 3, 4, 7):
                # increment count
                uniq_freq[char] = uniq_freq.get(char, 0) + 1

    return freq, uniq_freq


if __name__ == '__main__':
    # map sorted chars to numbers
    numbers = {
        'abcdefg': 8,
        'abdfg': 5,
        'acdeg': 2,
        'acdfg': 3,
        'acf': 7,
        'abcdfg': 9,
        'abdefg': 6,
        'bcdf': 4,
        'abcefg': 0,
        'cf': 1
    }
    # frequency of each letter
    frequency = {8: ['a', 'c'],
                 7: ['g', 'd'],
                 9: ['f'],
                 4: ['e'],
                 6: ['b']
                 }
    readings = inputs('input.txt')
    part1()
    part2()
