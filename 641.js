// 641. Design Circular Deque
/*
Design your implementation of the circular double-ended queue (deque).
Implement the MyCircularDeque class:
MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
*/

class ListNode {
    constructor(val, next, prev) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
        this.prev = (prev === undefined ? null : prev)
    }
}

class MyCircularDeque {
    constructor(k) {
        this.k = k
        this.size = 0
        this.head = null
        this.tail = null
    }

    insertFront(value) {
        if (this.size === this.k) {
            return false
        }
        const newNode = new ListNode(value)
        if (!this.size) {
            this.head = newNode
            this.tail = newNode
        } else {
            const nxt = this.head
            this.head = newNode
            newNode.next = nxt
            nxt.prev = newNode
        }
        this.size++
        return true
    }

    insertLast(value) {
        if (this.size === this.k) {
            return false
        }
        const newNode = new ListNode(value)
        if (!this.size) {
            this.head = newNode
            this.tail = newNode
        } else {
            newNode.prev = this.tail
            this.tail.next = newNode
            this.tail = newNode
        }
        this.size++
        return true
    }

    deleteFront() {
        if (!this.size) {
            return false
        }
        this.head = this.head.next
        if (this.head) {
            this.head.prev = null
        } else {
            this.tail = null
        }
        this.size--
        return true
    }

    deleteLast() {
        if (!this.size) {
            return false
        }
        this.tail = this.tail.prev
        if (this.tail) {
            this.tail.next = null
        } else {
            this.head = null
        }
        this.size--
        return true
    }

    getFront() {
        if (!this.size) {
            return -1
        } 
        return this.head.val
    }

    getRear() {
        if (!this.size) {
            return -1
        }
        return this.tail.val
    }

    isEmpty() {
        return this.size === 0
    }

    isFull() {
        return this.size === this.k
    }
}