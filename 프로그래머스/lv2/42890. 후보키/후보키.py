from itertools import combinations
from collections import defaultdict

def solution(relation):
    global answer
    def check_unique():
        flag = 1
        for i in range(len(relation)):
            tmp = []
            for j in range(len(relation[0])):
                if arr[j] == 1:
                    tmp.append(relation[i][j])
                else:
                    tmp.append(0)
            if val_dic[tuple(tmp)] == 1:
                tu_dic[tuple(arr)] = 0
                return False
            val_dic[tuple(tmp)] = 1
        tu_dic[tuple(arr)] = 1
        return True
    
    def check_minimality():
        for i in range(len(relation[0])):
            if arr[i] == 1:
                print(arr)
                arr[i] = 0
                if tu_dic[tuple(arr)] == 1:
                    arr[i]=1
                    return 0
                arr[i] = 1
        return 1
                
    
    def dfs(cnt, level, pre):
        global answer
         
        if level == cnt:

            if check_unique(): # 유일성
                answer+=check_minimality() # 최소성
            return


        for i in range(pre, len(relation[0])):
            arr[i] = 1
            dfs(cnt, level+1, i+1)
            arr[i]= 0
    
    answer = 0
    arr = [0]*len(relation[0])

    val_dic = defaultdict(int)
    tu_dic = defaultdict(int)
    tt = [0]*len(relation[0])
    for k in range(len(relation[0])):
        arr[k]=1
        flag = 1
        for i in range(len(relation)):
            aa = []
            for j in range(len(relation[0])):
                if arr[j]==1:
                    aa.append(relation[i][j])
                else:
                    aa.append(0)
            if val_dic[tuple(aa)]==1:
                flag=0
            else:
                val_dic[tuple(aa)]=1
                
        if flag:
            answer+=1
            tu_dic[tuple(arr)] = 1
        else:
            tu_dic[tuple(arr)] = 0
        arr[k]=0
            
        
    for i in range(2, len(relation[0])+1):
        # dfs 시작
        dfs(i, 0, 0)
        

    return answer


        