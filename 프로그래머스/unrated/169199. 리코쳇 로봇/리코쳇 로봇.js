class Node{
    constructor(data){
        this.data = data
        this.next = null
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
        if(!this.size){
            this.front = nNode
        }else{
            this.rear.next=nNode
        }
        this.rear = nNode
        this.size++
    }
    popleft(){
        const pNode = this.front.data
        this.front = this.front.next
        if(!this.front){
            this.rear = null
        }
        this.size = this.size -1
        return pNode
    }
}

function solution(board) {
    var answer = 0;
    let sty,stx,nowy,nowx,dy,dx,cnt,edy,edx
    for(let i=0; i<board.length; i++){
        for(var j=0; j<board[0].length; j++){
            if(board[i][j] === 'R'){
                sty = i
                stx = j
                
            }else if(board[i][j] === 'G'){
                edy = i
                edx = j
            }
        }

    }
    const visit = Array.from(Array(board.length), ()=>Array(board[0].length).fill(0))
    
    
    const q = new Queue()
    q.add([sty,stx,0])
    visit[sty][stx]=1
    const diy = [-1,1,0,0]
    const dix = [0,0,-1,1]
    
    while(q.size){
        [nowy,nowx,cnt] = q.popleft()
        
        if(nowy===edy && nowx === edx){
            return cnt
        }
        
        
        for(let l=0; l<4; l++){
            for(let k=1; k<100; k++){
                dy = nowy+diy[l]*k
                dx = nowx+dix[l]*k
                if(dy<0 || dx<0||dy>=board.length||dx>=board[0].length) break
                
                // D 에 도착했을 때
                if(board[dy][dx] === 'D'){
                    const ty = nowy + diy[l]*(k-1)
                    const tx = nowx + dix[l]*(k-1)
                    if(visit[ty][tx] === 1) break
                    visit[ty][tx] = 1
                    q.add([ty, tx, cnt+1])
                    break
                }

                // 배열 끝일 때
                const cy = nowy + diy[l]*(k+1)
                const cx = nowx + dix[l]*(k+1)
                if(cy<0 || cx<0 || cy === board.length|| cx ===board[0].length){
                    if(visit[dy][dx] === 1) break
                    visit[dy][dx] = 1
                    q.add([dy, dx, cnt+1])
                }                
                
                
            }
        }
    }
    
    return -1
}