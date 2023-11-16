function solution(plans) {
    var answer = [];
    const newPlans =plans.map((plan)=>{
        const [h, m] = plan[1].split(':')

        return [plan[0],parseInt(h)*60+parseInt(m), +plan[2]]
    }).sort((a, b)=>{
        return a[1]-b[1]
    })

    const stack = []
    const tmp = newPlans[0]
    answer.push(newPlans.slice(1).reduce((prior,now)=>{
        const ptime = prior[1]+prior[2]
        if(ptime>now[1]){
            stack.push([prior[0], ptime-now[1]])
        }else if(ptime === now[1]){
            answer.push(prior[0])
        }else{
            answer.push(prior[0])
            let leftTime = now[1]-ptime
            while(leftTime>0 && stack.length){
                const last = stack.pop()
                leftTime -= last[1]
                if(leftTime>=0){
                    answer.push(last[0])
                }else {
                    stack.push([last[0], -leftTime])
                }
            }
        }
        return now
    },tmp)[0])
    while(stack.length){
        answer.push(stack.pop()[0])
    }
    return answer;
}