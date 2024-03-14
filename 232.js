// 232. Implement Queue using Stacks
/*
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.
Notes:
- You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
*/

class MyQueue {
    constructor() {
        this.stack = []
        this.extraStack = []
    }
};

MyQueue.prototype.push = function(x) {
    this.stack.push(x)
};

MyQueue.prototype.pop = function() {
    while (this.stack.length) {
        this.extraStack.push(this.stack.pop())
    }
    const firstEl = this.extraStack.pop()
    while (this.extraStack.length) {
        this.stack.push(this.extraStack.pop())
    }
    return firstEl
};

MyQueue.prototype.peek = function() {
    return this.stack[0]
};

MyQueue.prototype.empty = function() {
    return !this.stack.length
};

const testObj = new MyQueue()
testObj.push(1)
testObj.push(2)
console.log(testObj.peek())
console.log(testObj.pop())
console.log(testObj.empty())