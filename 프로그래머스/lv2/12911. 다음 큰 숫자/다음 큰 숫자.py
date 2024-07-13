def solution(n):
    orn = list(bin(n)[2:])
    ans = 0
    for num in orn:
        if num =='1':
            ans+=1
        
    for num in range(n+1, 1000001):
        number = list(bin(num)[2:])
        cnt = 0
        for num2 in number:
            if num2 == '1':
                cnt+=1
        if cnt == ans:
            answer = num
            break
        
    return answer