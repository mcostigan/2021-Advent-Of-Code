import math
import networkx


def inputs(path):
    """
    read inputs into a graph, each cell has an _in and _out vertex, with weight equal to cell value
    all other edges have weight 0
    :param path: path of inputs
    :return: an undirected networkx graph
    """

    # open file
    fl = open(path, 'r').readlines()

    # create directed graph
    G = networkx.DiGraph()

    # get dimensions of grid
    x = len(fl)
    y = len(fl[0].strip())

    # add each cell as node
    for row in range(len(fl)):
        l = list(map(int, fl[row].strip()))
        for col in range(len(l)):
            # split node and weight edge to use dijkstra
            G.add_node((row, col, 'in'))
            G.add_node((row, col, 'out'))
            G.add_edge((row, col, 'in'), (row, col, 'out'), weight=l[col])

    # add edges connecting all nodes to adjacent nodes
    for node in G.nodes:
        add_adjacent_edges(node, G)

    return G, (x, y), fl


def part1(dimensions):
    # run dijkstra
    print('least risky path in grid:',
          networkx.dijkstra_path_length(G, (0, 0, 'out'), (dimensions[0] - 1, dimensions[1] - 1, 'out')))


def part2(dimensions, fl):
    # create copy of nodes
    nodes_copy = {node: G.nodes[node] for node in G.nodes()}

    # add 24 copies of each node
    for node in nodes_copy:
        for i in range(5):
            for j in range(5):
                if i != 0 or j != 0:
                    # increase weight by distance from original node
                    orig_weight = int(fl[node[0]][node[1]])
                    weight = orig_weight + i + j - 9 if orig_weight + i + j > 9 else orig_weight + i + j

                    # add in and out node
                    G.add_node((node[0] + (dimensions[0]) * i, node[1] + (dimensions[1]) * j, 'in'))
                    G.add_node((node[0] + (dimensions[0]) * i, node[1] + (dimensions[1]) * j, 'out'))

                    # and weighted edge
                    G.add_edge((node[0] + (dimensions[0]) * i, node[1] + (dimensions[1]) * j, 'in'),
                               (node[0] + (dimensions[0]) * i, node[1] + (dimensions[1]) * j, 'out'), weight=weight)

    # for all new nodes, add edges to adjacent nodes
    for node in G.nodes():
        if node[0] >= dimensions[0] or node[1] >= dimensions[1]:
            add_adjacent_edges(node, G)

    print('Least risky path in 25x grid:',networkx.dijkstra_path_length(G, (0, 0, 'out'), (dimensions[0] * 5 - 1, dimensions[1] * 5 - 1, 'out')))


def add_adjacent_edges(node, G):
    # for each adjacent cell, not including self and diagonal
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i == 0 or j == 0) and i != j and (node[0] + i, node[1] + j, 'out') in G.nodes:
                # create an edge to 'in' nodes
                if 'in' in node:
                    G.add_edge((node[0] + i, node[1] + j, 'out'), node, weight=0)
                else:
                # and from 'out' nodes
                    G.add_edge(node, (node[0] + i, node[1] + j, 'in'), weight=0)


if __name__ == '__main__':
    G, dimensions, fl = inputs('input.txt')

    part1(dimensions)
    part2(dimensions, fl)
