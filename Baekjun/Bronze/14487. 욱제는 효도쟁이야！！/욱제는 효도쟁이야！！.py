n = int(input())
arr = list(map(int, input().split()))
sum_cost = 0
max_arr = arr[0]

for i in range(len(arr)):
    if max_arr < arr[i]:
        max_arr = arr[i]
    sum_cost += arr[i]

print(sum_cost-max_arr)