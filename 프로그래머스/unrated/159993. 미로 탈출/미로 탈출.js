class Node {
    constructor(data){
        this.data=data
        this.next=null
    }
}

class Queue{
    constructor(){
        this.front = null
        this.rear = null
        this.size = 0
    }
    
    add(data){
        const nNode = new Node(data)
        if(this.size === 0){
            this.front = nNode
        }else{
            this.rear.next = nNode
        }
        this.rear = nNode
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
    var answer = 0;
    let sy,sx

    for(let i=0; i<maps.length; i++){
        for(let j=0; j<maps[0].length; j++){
            if(maps[i][j]==='S'){
                sy= i
                sx= j
                break
            }
        }
        if(sy &&sx) break
    }
    if(!findPoint(maps,sy,sx,'L')){
        return -1
    }
    const [ly,lx,step] = findPoint(maps, sy, sx, 'L')
    if(!findPoint(maps,ly,lx, 'E')){
        return -1
    }
    const [ey,ex,step2] = findPoint(maps,ly,lx,'E')
    answer = step+step2
    
    return answer;
}




const findPoint = (maps,sy,sx, point) => {
    const visit = Array.from(Array(maps.length), ()=>Array(maps[0].length).fill(0))
    const q = new Queue()
    let dy, dx
    q.add([sy,sx,0])
    visit[sy][sx]=1
    const diy = [-1,1,0,0]
    const dix = [0,0,-1,1]
    while(q.size){
        const [nowy, nowx, cnt] = q.popleft()
        if(maps[nowy][nowx] === point) return [nowy, nowx, cnt]
        
        for(let l=0; l<4; l++){
            dy = nowy+diy[l]
            dx = nowx+dix[l]
            if( dy<0 || dy>= maps.length || dx<0 || dx>=maps[0].length)continue
            if(maps[dy][dx] === 'X') continue
            if(visit[dy][dx] === 1) continue
            visit[dy][dx]=1
            q.add([dy, dx, cnt+1])
        }
    }
    return false
}