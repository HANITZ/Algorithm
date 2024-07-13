function solution(n) {
    var answer = [];
    
    answer = answer.concat(dfs(n,1,3,2))


    return answer;
}

const dfs = (n, from , to, mid) => {
    if (n===1)return[[from,to]]
    var result = []
    result = result.concat(dfs(n-1,from,mid,to))
    result.push([from,to])
    result = result.concat(dfs(n-1,mid,to,from))
    return result
}