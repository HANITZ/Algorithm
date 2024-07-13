class Node{
	constructor(val){
		this.data = val;
		this.next = null;
	}
}
class Queue{
	constructor(){
		this.front = null;
		this.rear = null;
		this.size = 0
	}


	add(val){
		const newNode = new Node(val);
		if(this.size === 0){
			this.front = newNode;
		}else{
			this.rear.next = newNode
		}
		this.rear = newNode
		this.size++
	}
    
	popleft(){
		let tmp
		if(this.size === 0) return -404;
		tmp = this.front.data
		this.front = this.front.next;
		if(!this.front) this.rear = null
		this.size--
		return tmp
        
	}
}

function solution(maps) {
    var answer = [];
    const visit = Array.from(Array(maps.length), ()=>Array(maps[0].length).fill(false))
    const rowSize = maps.length
    const colSize = maps[0].length
    for(let i=0; i<rowSize; i++){
        for(let j=0; j<colSize; j++){
            if(maps[i][j] !== 'X'){
                if(visit[i][j])continue
                answer.push(findDays(i, j, maps, visit)) 
            }
        }
    }
    if(answer.length===0)return[-1]
    answer.sort((a,b)=>a-b)
    
    return answer;
}

const findDays = (y, x, maps, visit) => {
    const diy = [-1,1,0,0]
    const dix = [0,0,-1,1]
    
    let cnt = 0
    const q = new Queue()
    q.add([y, x])

    visit[y][x]=true
    while(q.size){
        const [nowy, nowx] = q.popleft()
        cnt+=parseInt(maps[nowy][nowx])
        for(let l=0; l<4; l++){
            const dy = nowy+diy[l]
            const dx = nowx+dix[l]
            if(dy<0 || dx<0 || dy>=maps.length || dx>=maps[0].length) continue
            if(visit[dy][dx]) continue
            if(maps[dy][dx]==='X')continue
            q.add([dy,dx])
            visit[dy][dx]=true
        }
    }
    return cnt
    
}