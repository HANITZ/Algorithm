def check(x, y, n):
    for i in range(x):
        if y == arr[i] or abs(y - arr[i]) == x - i:
            return False
    return True

def dfs(x, n):
    if x == n:
        return 1
    count = 0
    
    for y in range(n):
        if check(x, y, n):
            arr[x] = y
            count += dfs(x+1, n)
    return count

def solution(n):
    global arr
    arr = [0] * n
    answer = dfs(0, n)
    return answer