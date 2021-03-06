def sort_and_tuple(arr):
    return tuple(sorted(arr))


def check(coor_1, coor_2, board, flag):
    n = len(board)

    move_list = [[(0, -1), (0, 1)], [(-1, 0), (1, 0)]]
    if flag == 'horizontal':
        move_list.reverse()
    move_ver, move_hor = move_list[0], move_list[1]

    result = []
    for move in move_ver: #
        dx, dy = move[0], move[1]
        for x, y in coor_1, coor_2:
            if not 0 <= x + dx < n or not 0 <= y + dy < n or board[x+dx][y+dy]:
                break
        else:
            new_coor1 = (coor_1[0]+dx, coor_1[1]+dy)
            new_coor2 = (coor_2[0]+dx, coor_2[1]+dy)

            for coor in [[coor_1, new_coor1], [new_coor2, coor_2], [new_coor1, new_coor2]]:
                result.append(sort_and_tuple(coor))

    for move in move_hor:
        dx, dy = move[0], move[1]
        x_1, y_1, x_2, y_2 = coor_1[0], coor_1[1], coor_2[0], coor_2[1]
        if 0 <= x_1+dx < n and 0 <= y_1+dy < n and 0 <= x_2+dx < n and 0 <= y_2+dy < n and \
            not board[x_1+dx][y_1+dy] and not board[x_2+dx][y_2+dy]:
            new_coor1 = (x_1+dx, y_1+dy)
            new_coor2 = (x_2+dx, y_2+dy)
            result.append((new_coor1, new_coor2))

    return result


def solution(board):
    n = len(board)
    dist_dict = {}

    for i in range(n):
        for j in range(n-1):
            if 0 <= i < n and 0 <= j < n:
                dist_dict[((i, j), (i, j + 1))] = 0xffffff
    for i in range(n - 1):
        for j in range(n):
            if 0 <= i < n and 0 <= j < n:
                dist_dict[((i, j), (i + 1, j))] = 0xffffff

    key = tuple(sorted([(0, 0), (0, 1)]))
    dist_dict[key] = 0
    robot = [((0, 0), (0, 1))]

    while robot:
        direction = robot.pop(0)
        x1, y1, x2, y2 = direction[0][0], direction[0][1], direction[1][0], direction[1][1]
        if x1 == x2:
            result = check((x1, y1), (x2, y2), board, 'horizontal')
        else:
            result = check((x1, y1), (x2, y2), board, 'vertical')

        if result:
            for r1, r2 in result:
                if dist_dict.get((r1, r2)) > dist_dict.get(direction)+1:
                    dist_dict[(r1, r2)] = dist_dict.get(direction)+1
                    robot.append((r1, r2))


    return min(dist_dict.get(((n-1, n-2), (n-1, n-1))), dist_dict.get(((n-2, n-1), (n-1, n-1))))


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
