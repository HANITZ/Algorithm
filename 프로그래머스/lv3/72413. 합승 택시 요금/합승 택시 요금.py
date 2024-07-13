from heapq import heappush, heappop


def solution(n, s, a, b, fares):
    answer = 0
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for st, ed, fare in fares:
        graph[st][ed] = fare
        graph[ed][st] = fare
    s_opti = search_min_dis(s, graph, n)
    a_opti = search_min_dis(a, graph, n)
    b_opti = search_min_dis(b, graph, n)
    
    min_opti = 21e8
    for i in range(1, n+1):
        if s_opti[i]+a_opti[i]+b_opti[i] < min_opti:
            min_opti = s_opti[i]+a_opti[i]+b_opti[i]
        
    return min_opti 

def search_min_dis(st, graph, n):
    arr = [21e8]*(n+1)
    visit = [0]*(n+1)
    q = []
    
    heappush(q, (0, st))
    arr[st] = 0
    while q:
        dis, node = heappop(q)
        visit[node]=1
        
        if dis < arr[node]:
            arr[node] = dis
        
        for j in range(1,n+1):
            if graph[node][j] >0:
                if visit[j] : continue
                heappush(q, (dis+graph[node][j], j))
    return arr
        
    
    
    
    
    