class Node {
    constructor(data){
        this.data = data
        this.next = null
    }
}

class Queue{
    constructor(){
        this.front=null
        this.rear = null
        this.size=0
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
        this.size--
    }
}

function solution(sequence, k) {
    var answer = [];
    const q = new Queue()
    q.add(sequence[0])
    const arr = []
    let Sum = sequence[0]
    let st = 0
    let ed = 0
    while(st<sequence.length ){
        if(Sum === k){
            arr.push([st, ed])
            Sum= Sum-sequence[st]
            st= st+1
        }else if(Sum > k){
            Sum = Sum - sequence[st]
            st=st+1
        }else{
            ed = ed+1
            if(ed === sequence.length)break
            Sum = Sum + sequence[ed]
        }
    }
    arr.sort((a,b)=>(a[1]-a[0]) - (b[1]-b[0]))
    
    
    
    return arr[0];
}