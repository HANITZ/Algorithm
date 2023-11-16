from heapq import heappush,heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        for st, ed, weight in times:
            graph[st][ed] = weight
        roots = [21e8]*(n+1)
        roots[0] = 0
        roots[k] = 0
        heap = [(0, k)]
        while heap:
            time, st =heappop(heap)
            roots[st] = min(roots[st], time)

            for ed in range(1, n+1):
                if graph[st][ed] != -1:
                    if roots[ed] > graph[st][ed]+time:
                        print(graph[st][ed], time, st, ed)
                        heappush(heap, (graph[st][ed]+ time, ed))
        print(roots)
        if 21e8 in roots:
            return -1
        else:
            return max(roots)


        
        