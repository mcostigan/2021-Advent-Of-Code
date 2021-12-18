class Node():
    """
    node class of tree representing each possible path
    """

    def __init__(self, value, part=1, parent=None):
        """

        :param value: name of cave
        :param part: in part 1, can visit each small cave once. In part 2, can visit ONE small cave twice
                        once a small cave has been explored twice, part 2 becomes equivalent to part 1
        :param parent: parent cave
        """
        # update node variables
        self.parent = parent
        self.value = value
        self.children = []
        self.small_caves = {}

        # determine if large or small cave
        is_small = value == value.lower()

        # has visited same small caves as parent
        if parent is not None:
            self.small_caves = {key: parent.small_caves[key] for key in parent.small_caves}

        # if self is small, increment visited amount
        if is_small:
            self.small_caves[value] = self.small_caves.get(value, 0) + 1

        # if part 2...
        if part == 2:
            # ... check if current node is a small cave and has been visited twice
            if is_small:
                if self.small_caves[value] == 2:
                    # ... if so, change to part 1
                    part = 1

        # if part 1...
        if part == 1:
            # for each adjacent cave
            for v in adj[value]:
                # check if is in small_caves hash
                if v not in self.small_caves:
                    # if not, create a new node and add to child list
                    child = Node(v, 1, self)
                    self.children.append(child)
        else:
            # if part 2...
            for v in adj[value]:
                # add adjacent node and add to children list
                child = Node(v, 2, self)
                self.children.append(child)


def inputs(path):
    """
    read inputs into an adjacency dictionary
    :param path: path of inputs
    :return: dictionary caves to adjacent caves
    """

    # open file
    fl = open(path, 'r').readlines()

    # create dictionary of adjacent caves
    d = {}
    # loop through "edges"
    for row in fl:
        # split into two points and add to adjacency lists
        u, v = row.strip().split('-')
        if 'start' not in (u, v) and 'end' not in (u, v):
            d[u] = d.get(u, []) + [v]
            d[v] = d.get(v, []) + [u]

        # nothing goes "to" start or "from" end
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
    print('Paths w/ @ most one visit to each small cave:', walk_tree(start))


def part2():
    start = Node('start', 2)
    print('Paths visiting at most one small cave twice:', walk_tree(start))


def walk_tree(node):
    # base case
    if node.value == 'end':
        return 1

    # get count of number of paths in tree rooted @ node
    count = 0
    # equal to sum of paths in children
    for child in node.children:
        count += walk_tree(child)

    return count


if __name__ == '__main__':
    adj = inputs('testinput.txt')
    part1()
    part2()
