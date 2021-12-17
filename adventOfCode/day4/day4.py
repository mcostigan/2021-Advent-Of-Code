def inputs(p):
    fl = open(p, 'r').readlines()

    l = fl[0].strip().split(',')

    board = {}
    numbers = {}

    ln = 2
    board_id = 0
    while ln < len(fl):
        board[board_id] = {(i, j): None for i in range(5) for j in range(5)}
        for i in range(5):
            tmp = fl[ln + i].split()
            for t in range(5):
                board[board_id][i, t] = tmp[t]
                numbers[tmp[t]] = numbers.get(tmp[t], []) + [(board_id, i, t)]
        ln += 6
        board_id += 1

    return l, board, numbers


def get_score(board_id, i):
    score = 0
    for key in board[board_id]:
        if board[board_id][key] not in number_set:
            score += int(board[board_id][key])
    print(score * int(i))


if __name__ == '__main__':
    l, board, numbers = inputs('input.txt')
    result = {b: {} for b in board}
    winning_boards = set()
    number_set = set()

    for b in range(len(board)):
        for i in range(5):
            result[b]['r' + str(i)] = set()
            result[b]['c' + str(i)] = set()

    bln_break = False
    for itm in l:
        number_set.add(itm)
        cells = numbers[itm]
        for cell in cells:
            result[cell[0]]['r' + str(cell[1])].add(cell[2])
            result[cell[0]]['c' + str(cell[2])].add(cell[1])
            if cell[0] not in winning_boards and (len(result[cell[0]]['r' + str(cell[1])]) == 5 or len(result[cell[0]]['c' + str(cell[2])]) == 5):
                print(cell[0])
                get_score(cell[0], itm)
                winning_boards.add(cell[0])
