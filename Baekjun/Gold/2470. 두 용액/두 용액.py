import sys
input=sys.stdin.readline
n= int(input())
arr=list(map(int, input().split()))
arr.sort()
length=len(arr)
ans=21e8
i=0
j=len(arr)-1
while i < j:
    mid = (arr[i]+arr[j])/2
    if ans >= abs(mid):
        ans=abs(mid)
        st, ed = i, j
    if mid >= 0 :
        j -= 1
    else:
        i += 1
print(arr[st], arr[ed])