from collections import defaultdict

def solution(cards):
    
    def define(x):
        if x == arr[x]:
            return x
        
        arr[x] = define(arr[x])
        return arr[x]
    
    
    
    def union(a, b):
        
        a = define(a)
        b = define(b)

        if a==b:
            return

        if a>b:
            for i in range(1, n+1):
                if arr[i] == a:
                    arr[i] = b
        elif b>a:
            for i in range(1, n+1):
                if arr[i] == b:
                    arr[i] = a
            
    
    
    answer = 1
    n = len(cards)
    cards = [0] + cards
    
    arr = [i for i in range(n+1)]
    
    
    for i in range(1, n+1):
        union(i, cards[i])
    num_dic = defaultdict(int)
    for i in range(1, n+1):
        num_dic[arr[i]] +=1
    if len(num_dic)==1:
        return 0
    
    max_val = 0
    for key1,val1 in num_dic.items():
        for key2,val2 in num_dic.items():
            if key1 != key2:
                max_val = max(max_val, val1*val2)
        
        
    
    return max_val

