function solution(s) {
    let st,ed,prior,left,cnt,tmp
    var answer = s.length
    const half = Math.floor(s.length/2)
    for(let l=half; l>0; l--){
        tmp=''
        for(let i=0; i<s.length; i+=l){

            prior = s.slice(i, i+l)
            cnt=1
            i+=l
            left = s.slice(i,i+l)
            while (prior === left){
                i+=l
                left = s.slice(i, i+l)
                cnt++
            }
            
            if(cnt>1){
                tmp += cnt+prior
            }else{
                tmp += prior
            }
            i-=l

        }
        answer = Math.min(answer, tmp.length)
        
    }


    return answer;
}