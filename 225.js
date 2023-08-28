// 225. Implement Stack using Queues
/*
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
Implement the MyStack class:
- void push(int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.
Notes:
- You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
*/

var MyStack = function() {
    this.arr = []
};

MyStack.prototype.push = function(x) {
    this.arr.push(x)
};

MyStack.prototype.pop = function() {
    return this.arr.pop()
};

MyStack.prototype.top = function() {
    return this.arr[this.arr.length - 1]
};

MyStack.prototype.empty = function() {
    for (let val of this.arr) {
        if (val !== undefined) {
            return false
        }
    }
    return true
};


var myStack = new MyStack()
myStack.push(0)
myStack.push(1)
myStack.push(2)
console.log(myStack.top())
console.log(myStack.pop())
console.log(myStack.empty())
console.log(myStack)