class Node():
    def __init__(self, value, part=1, parent=None):
        self.parent = parent
        self.value = value
        self.children = []
        is_small = value == value.lower()
        self.small_caves = {}

        if parent is not None:
            self.small_caves = {key: parent.small_caves[key] for key in parent.small_caves}

        if is_small:
            self.small_caves[value] = self.small_caves.get(value, 0) + 1

        if part == 2:
            self.visited_twice = sum([self.small_caves[key] == 2 for key in self.small_caves])
            if self.visited_twice:
                part = 1

        if value == 'end':
            return

        if part == 1:
            for v in adj[value]:
                if v not in self.small_caves:
                    child = Node(v, 1, self)
                    self.children.append(child)
        else:
            for v in adj[value]:
                child = Node(v, 2, self)
                self.children.append(child)

    def add_child(self, value, is_small):
        self.children.append(value)


def inputs(path):
    """
    read inputs into a list readings and results
    :param path: path of inputs
    :return: dictionary mapping readings to results
    """
    fl = open(path, 'r').readlines()
    d = {}
    for row in fl:
        u, v = row.strip().split('-')
        if 'start' not in (u, v) and 'end' not in (u, v):
            d[u] = d.get(u, []) + [v]
            d[v] = d.get(v, []) + [u]
        elif 'start' in (u, v):
            e = v if v != 'start' else u
            d['start'] = d.get('start', []) + [e]
        elif 'end' in (u, v):
            s = v if v != 'end' else u
            d[s] = d.get(s, []) + ['end']
            d['end'] = []
    return d


def part1():
    start = Node('start')
    print(walk_tree(start))

def part2():
    start = Node('start',2)
    print(walk_tree(start))


def walk_tree(node):
    if node == None:
        return 0
    if node.value == 'end':
        return 1
    count = 0
    for child in node.children:
        count += walk_tree(child)
    return count


if __name__ == '__main__':
    adj = inputs('input.txt')
    part1()
    part2()
