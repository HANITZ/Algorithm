import sys
input = sys.stdin.readline
from collections import deque



def roll(h,cnt):
    global line
    cnt+=1
    lift = deque()
    for j in range(n):
        if line[h][j]!=0:
            for i in range(h,-1,-1):
                lift.append((i,j))
    tmpy,tmpx=lift.popleft()
    
    stx = tmpx-(h+1)
    if stx<0:
        return
    sty = 1
    line[sty][stx], line[tmpy][tmpx] = line[tmpy][tmpx], 0

    rotate = [] # x 값
    tmp=1
    while lift:
        y, x = lift.popleft()
        line[sty][stx+tmp], line[y][x] = line[y][x], 0
        tmp+=1
        
        if tmp>h:
            tmp=0
            sty+=1
    if cnt==2:
        roll(h+1,0)
    else:
        roll(h,cnt)
    
    

def bal():
    global line
    new_line = [[0]*n for _ in range(n)]
    dir = [(0, 1), (1, 0)]
    for i in range(n):
        for j in range(n):
            if line[i][j]==0: continue
            
            for diy, dix in dir:
                dy = i+diy
                dx = j+dix
                if dy<0 or dy>=n or dx<0 or dx>=n: continue
                if line[dy][dx]==0: continue
                dif = abs(line[dy][dx]-line[i][j])
                num = dif//5
                if line[i][j] < line[dy][dx]:
                    new_line[i][j] += num
                    new_line[dy][dx] -= num
                else:
                    new_line[i][j] -= num
                    new_line[dy][dx] += num
    for i in range(n):
        for j in range(n):
            if line[i][j]==0: continue
            line[i][j] += new_line[i][j]
    
            
            
            
            
def lalala(y, x): # 2, 3
    global line
    qqq = deque()
    for j in range(n - 1, -1, -1):
        if line[0][j] != 0:
            for i in range(n):
                if line[i][j] ==0: continue
                qqq.append(line[i][j])
                line[i][j] = 0
    for i in range(n-1,-1,-1):
        line[0][i]=qqq.popleft()
    

        

def half(kk):
    global line
    qq=deque()
    for j in range(kk,n):
        qq.append(line[0][j])
        line[0][j]=0
    
    for j in range(kk-1,-1,-1):
        num=qq.popleft()
        line[1][j]=num
    
def halfhalf(kkkk, kk): # 2 4
    global line
    qqqq = deque()
    for i in range(1,-1,-1):
        for j in range(kk-1, kkkk-1, -1):
            qqqq.append(line[i][j])
            line[i][j]=0
    
    for i in range(2, 4):
        for j in range(kkkk):
            num = qqqq.popleft()
            line[i][j] = num



def last():
    global line, arr
    lastq=deque()
    for j in range(n-1,-1,-1):
        if line[0][j] !=0:
            for i in range(4):
                lastq.append(line[i][j])
                line[i][j]=0
    arr=[]
    for j in range(n):
        arr.append(lastq.popleft())
        
        
            




n, K= map(int, input().split())
arr=list(map(int, input().split()))


CNT=0
while 1:
    CNT+=1
    Min = min(arr)
    for i in range(n):
        if arr[i]==Min:
            arr[i] = arr[i]+1
    
    
    line=[[0]*n for _ in range(n)]
    for i in range(n):
        line[0][i] = arr[n - 1 - i]
    line[1][n-2], line[0][n-1] = line[0][n-1], line[1][n-1]

    roll(1,0)
    bal() # 몫 나누기
    x=0
    for j in range(n):
        if line[0][j] !=0:
            x=j
    y=0
    for i in range(n):
        if line[i][x]!=0:
            y=i
    
    lalala(y,x)
    
    kk= n//2
    half(kk)
    kkkk=kk//2
    halfhalf(kkkk, kk)
    bal()
    last()
    if max(arr)-min(arr)<=K:
        break
print(CNT)