bucket = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            bucket[i][j] += 1
    sum = 0
    sum_minus = 0
    for i in range(len(bucket)):
        for j in range(len(bucket[0])):
            if bucket[i][j] != 0:
                sum += 1

print(sum)
