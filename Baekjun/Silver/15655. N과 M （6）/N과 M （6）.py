n, m = map(int, input().split())
arr = list(map(int, input().split()))
path = [0]*m
used = [0]*n
arr.sort()
def abc(level):
    if level == m:
        for i in range(m):
            print(path[i], end=' ')
        print()
        return

    for i in range(n):
        if used[i] == 1:
            continue
        path[level] = arr[i]
        if level>0:
            if path[level-1] > path[level]:
                continue
        used[i] = 1
        abc(level+1)
        used[i] = 0


abc(0)