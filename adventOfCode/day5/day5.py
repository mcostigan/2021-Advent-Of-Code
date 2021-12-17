def inputs(p):
    d = {}
    fl = open(p, 'r')
    for ln in fl:
        ln = ln.split(' -> ')
        left = tuple(map(int, ln[0].split(',')))
        right = tuple(map(int, ln[1].split(',')))

        if left[0] == right[0]:
            start = min(left[1], right[1])
            end = max(left[1], right[1]) + 1
            # then horizontal
            for i in range(start, end):
                d[left[0], i] = d.get((left[0], i), 0) + 1
        elif left[1] == right[1]:
            start = min(left[0], right[0])
            end = max(left[0], right[0]) + 1
            for i in range(start, end):
                d[i, left[1]] = d.get((i, left[1]), 0) + 1
        else:
            start = min(left,right)
            end = max(left,right)
            print(start)
            for i in range(abs(left[0]-right[0])+1):
                if start[0]<end[0]:
                    x_dir = +1
                else:
                    x_dir = -1
                if start[1]<end[1]:
                    y_dir = +1
                else:
                    y_dir = -1

                d[start[0]+i*x_dir, start[1]+i*y_dir] = d.get((start[0]+i*x_dir, start[1]+i*y_dir),0)+1

    return d


if __name__ == '__main__':
    d = inputs('input.txt')
    print(len([1 for key in d if d[key] > 1]))
