class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        def dfs(level, arr):

            if level == len(tickets):
                answer.extend(arr[:])
                return
            
            for i in range(len(tickets)):
                if visit[i] == 1: continue
                if tickets[i][0] == arr[-1]:
                    visit[i]=1
                    arr.append(tickets[i][1])
                    dfs(level+1, arr)
                    arr.pop()
                    visit[i]=0
                if answer:
                    return
            


        answer = []

        
        tickets.sort(key = lambda x : x[1])
        visit = [0]*len(tickets)
        dfs(0, ["JFK"])

        return answer