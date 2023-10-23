// 933. Number of Recent Calls
/*
You have a RecentCounter class which counts the number of recent requests within a certain time frame.
Implement the RecentCounter class:
- RecentCounter() Initializes the counter with zero recent requests.
- int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
*/

class RecentCounter {
    constructor() {
        this.reqs = new PingQueue()
    }
    
    ping(t) {
        const lowRange = t - 3000
        while (this.reqs.size && this.reqs.first.val < lowRange) {
            this.reqs.dequeue()
        }
        this.reqs.enqueue(t)
        return this.reqs.size
    }
}

class Node {
    constructor(val) {
        this.val = val
        this.next = null
    }
}

class PingQueue {
    constructor() {
        this.first = null
        this.last = null
        this.size = 0
    }
    
    enqueue(val) {
        const newNode = new Node(val)
        if (this.size === 0) {
            this.first = newNode
            this.last = newNode
        } else {
            this.last.next = newNode
            this.last = newNode
        }
        this.size++
    }
    
    dequeue() {
        if (this.size === 0) return null
        const removedNode = this.first
        if (this.size === 1) {
            this.last = null
        }
        this.first = removedNode.next
        removedNode.next = null
        this.size--
        return removedNode.val
    }
}

const testCase = new RecentCounter()
console.log(testCase.ping(1))
console.log(testCase.ping(100))
console.log(testCase.ping(3001))
console.log(testCase.ping(3002))