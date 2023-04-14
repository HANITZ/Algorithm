import collections
import sys
from heapq import heappush, heappop


input=sys.stdin.readline
n=int(input())
arr=[]
dic=collections.defaultdict(list)
for _ in range(n):
    deadline, cup = map(int, input().split())
    heappush(dic[deadline], -cup)

time = 1
ans = []
cnt=0
while time <= n:

    if not dic[time]:
        time+=1
        cnt=0
        continue
    noodle=heappop(dic[time])
    if ans:
        if len(ans)==time:
            tmp = heappop(ans)
            if tmp >= -noodle:
                heappush(ans, tmp)
            else:
                heappush(ans, -noodle)
        else:
            heappush(ans, -noodle)
    else:
        heappush(ans, -noodle)

    
print(sum(ans))