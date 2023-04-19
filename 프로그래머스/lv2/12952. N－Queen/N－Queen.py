def check(x, y, n, col):
    for i in range(x):
        if y == col[i] or abs(y - col[i]) == x - i:
            return False
    return True

def dfs(x, n, col):
    if x == n:
        return 1
    count = 0
    
    for y in range(n):
        if check(x, y, n, col):
            col[x] = y
            count += dfs(x+1, n, col)
    return count

def solution(n):
    col = [0] * n
    answer = dfs(0, n, col)
    return answer