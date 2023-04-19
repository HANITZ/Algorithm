from heapq import heappush, heappop


def solution(n, k, enemy):
    if len(enemy) <= k:
        return len(enemy)
    
    # priorityQ
    q = []
    idx = 0
    while idx<len(enemy) :
        
        if n >= enemy[idx]:
            n -= enemy[idx]
            heappush(q, -enemy[idx])
            idx+=1
        else:
            if k <= 0 : return idx      
            k-=1
            if q:           
                num = -heappop(q)
                if num > enemy[idx]:
                    n+=num
                else:
                    idx+=1
                    heappush(q, -num)
            else:
                idx+=1
    return len(enemy)