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
    results = 0
    for reading in readings:
        for result in readings[reading]:
            if len(result) in (2, 4, 3, 7):
                results += 1
    print(results, 'instances of 1,4,7, or 8')


def part2():
    answer = 0
    for reading in readings:
        solution = {}
        freq, uniq_freq = frequency_analysis(reading)
        for key in freq:
            if len(frequency[freq[key]]) == 1:
                solution[key] = frequency[freq[key]][0]
            else:
                if frequency[freq[key]] == ['g', 'd']:
                    if uniq_freq[key] == 2:
                        solution[key] = 'd'
                    else:
                        solution[key] = 'g'
                else:
                    if uniq_freq[key] == 2:
                        solution[key] = 'a'
                    else:
                        solution[key] = 'c'
        result = 0
        for i in range(4):
            digit = readings[reading][i]
            s = ''
            for char in digit:
                s += solution[char]
            number = numbers[''.join(sorted(s))]
            result += number * 10**(3-i)
        answer += result
    print(answer,'sum of all readings')



def frequency_analysis(t):
    freq = {}
    uniq_freq = {}
    for reading in t:
        for char in reading:
            freq[char] = freq.get(char, 0) + 1
            if len(reading) in (2, 3, 4, 7):
                uniq_freq[char] = uniq_freq.get(char, 0) + 1
    return freq, uniq_freq


if __name__ == '__main__':
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
    frequency = {8: ['a', 'c'], 7: ['g', 'd'], 9: ['f'], 4: ['e'], 6: ['b']}
    readings = inputs('input.txt')
    part1()
    part2()
