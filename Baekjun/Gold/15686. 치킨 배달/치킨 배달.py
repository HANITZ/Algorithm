N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
pick = [0]*M
ans = 1e9

for y in range(N):
    for x in range(N):
        if board[y][x] == 2:
            chicken.append((y, x))
        elif board[y][x] == 1:
            house.append((y, x))

count = len(chicken)
check = [0]*count

def DFS(level, now):
    global ans
    if level == M:
        res = 0
        for h in house:
            temp = 1e9
            for p in pick:
                temp = min(temp, abs(p[0]-h[0])+abs(p[1]-h[1]))
            res += temp
        ans = min(ans, res)
        return
    for idx in range(now+1, count):
        if check[idx] == 1:continue
        check[idx] = 1
        pick[level] = chicken[idx]
        DFS(level+1, idx)
        check[idx] = 0
        pick[level] = 0

DFS(0, -1)
print(ans)