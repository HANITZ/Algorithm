from heapq import heappush, heappop
def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    answer = 0
    cnt = 0
    for st, ed, cost in costs:
        if(union(st, ed, parent)):
            answer+= cost
            cnt+=1
        if cnt == n-1:
            break

    return answer
def find_parent(x, parent):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union(st, ed, parent):
    pst = find_parent(st, parent)
    ped = find_parent(ed, parent)
    
    if pst == ped:
        return False
    if pst > ped:
        parent[pst] = ped
    else:
        parent[ped] = pst
    for i in range(len(parent)):
        parent[i] = find_parent(i, parent)
    return True

        
        
        
    