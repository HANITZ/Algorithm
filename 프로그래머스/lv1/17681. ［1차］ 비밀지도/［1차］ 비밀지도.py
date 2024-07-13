def solution(n, arr1, arr2):
    answer = []
    
    
    for i in range(n):
        a1 = to_bin(arr1[i], n)
                
        a2 = to_bin(arr2[i], n)
        tmp_arr = ''
        for j in range(n):
            if a1[j] == '1' or a2[j] == '1':
                tmp_arr+= '#'
            else: 
                tmp_arr+= ' '
        answer.append(tmp_arr)

    return answer

def to_bin(num, n):
    bin_num = bin(num)[2:]
    if len(bin_num) != n:
        for _ in range(n-len(bin_num)):
            bin_num = '0'+bin_num
    return list(bin_num)