from collections import defaultdict

def solution(weights):
    answer = 0
    dic = defaultdict(int)
    for i in range(len(weights)):
        dic[weights[i]]+=1
    for key, val in dic.items():
        answer += dic[key]*(dic[key]-1)*(1/2)
        if 2*key in dic:
            answer += dic[key]*dic[2*key]
        if (3/2)*key in dic:
            answer += dic[key]*dic[(3/2)*key]
        if (4/3)*key in dic:
            answer += dic[key]*dic[(4/3)*key]
    
    return answer