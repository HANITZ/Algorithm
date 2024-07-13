class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(y, x):

            q = collections.deque()
            q.append((y,x))
            visit[y][x]=1
            diy, dix = [-1,1,0,0], [0,0,-1,1]
            while q:
                nowy, nowx = q.popleft()
                
                for l in range(4):
                    dy = nowy+diy[l]
                    dx = nowx+dix[l]
                    if dy<0 or dy>=len(grid) or dx<0 or dx>=len(grid[0]): continue
                    if visit[dy][dx]==1: continue
                    if grid[dy][dx] == '0': continue
                    q.append((dy,dx))
                    visit[dy][dx]=1
        answer=0
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    if visit[i][j] == 1: continue
                    bfs(i,j)
                    answer+=1
        return answer
        



