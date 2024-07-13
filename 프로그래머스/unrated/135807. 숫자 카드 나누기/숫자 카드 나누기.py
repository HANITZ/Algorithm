def solution(arrayA, arrayB):
    answer = 0
    
    a_can = can_div(arrayA)
    b_can = can_div(arrayB)
    if a_can != 1:
        answer = max(cant_div(arrayB, a_can), answer)
    if b_can != 1:
        answer = max(cant_div(arrayA, b_can), answer)   
    return answer


def cant_div(arr, div):
    for num in arr:
        if num % div == 0:
            return 0
    return div

def find(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def can_div(arr):
    mini = min(arr)
    sta = arr[0]
    for i in range(1, len(arr)):
        sta = find(sta, arr[i])
    return sta
    
            
    