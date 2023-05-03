from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for fr, to, price in flights:
            graph[fr].append((to, price))
        
        
        heap = []
        heappush(heap, (0,src,0))
        visited = set()
        while heap:
            price, st, stop = heappop(heap)

            if st == dst:
                return price
            if stop > k:continue
            if (st, stop) in visited: continue
            visited.add((st, stop))
            for to, weight in graph[st]:
                alt = price+weight
                heappush(heap, (alt, to, stop+1))
        return -1
        