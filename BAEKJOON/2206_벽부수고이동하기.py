def bfs(x, y, chance, move):
    global min_move
    if move >= min_move:
        return
    if x > n-1 or y > m-1:
        return
    if x == n-1 and y == m-1:
        min_move = min(move+1, min_move)
        return


    for i in range(len(dx)):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
            if chance == 1 and maps[x+dx[i]][y+dy[i]] == 1 and visited[x+dx[i]][y+dy[i]] == False:
                visited[x+dx[i]][y+dy[i]] = True
                bfs(x+dx[i], y+dy[i], 0, move+1)
                visited[x+dx[i]][y+dy[i]] = False
            elif maps[x+dx[i]][y+dy[i]] == 0 and visited[x+dx[i]][y+dy[i]] == False:
                visited[x+dx[i]][y+dy[i]] = True
                bfs(x+dx[i], y+dy[i], chance, move+1)
                visited[x+dx[i]][y+dy[i]] = False


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
visited = []
for i in range(n):
    temp = [False] * m
    visited.append(temp)
print(visited)
min_move = 1000*1000
bfs(0, 0, 1, 0)
if min_move == 1000*1000:
    print(-1)
else:
    print(min_move)

    # 2
    # 4
    #
    # 0111
    # 0010

'''
4 4
0101
0101
0001
1110


'''