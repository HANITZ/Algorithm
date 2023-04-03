def solution(tickets):
    global answer
    tickets.sort()
    answer = []
    visit = [0]*len(tickets)
    def dfs(arr, level):
        global answer
        
        if level == len(tickets):
            answer = arr
            return
        
        
        for i in range(len(tickets)):
            if visit[i]==1: continue
            if arr[level] == tickets[i][0]:
                visit[i]=1
                dfs(arr+[tickets[i][1]] , level+1)
                visit[i]=0
                if answer:
                    return
                        
        
    dfs(["ICN"], 0)
    return answer