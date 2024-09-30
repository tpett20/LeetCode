// 1381. Design a Stack With Increment Operation
/*
Design a stack that supports increment operations on its elements.
Implement the CustomStack class:
    CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
    void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
    int pop() Pops and returns the top of the stack or -1 if the stack is empty.
    void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
*/

class CustomStack {
    constructor(maxSize) {
        this.maxSize = maxSize
        this.arr = []
    }

    push(x) {
        if (this.arr.length < this.maxSize) {
            this.arr.push(x)
        }
    }

    pop() {
        if (!this.arr.length) {
            return -1
        } else {
            return this.arr.pop()
        }
    }

    increment(k, val) {
        for (let i = 0; i < k && i < this.arr.length; i++) {
            this.arr[i] += val
        }
    }
}

const testCase = new CustomStack(3)
testCase.push(1)
testCase.push(2)
testCase.push(3)
testCase.push(4)
testCase.increment(2, 2)
console.log(testCase.pop())
console.log(testCase.pop())
console.log(testCase.pop())
console.log(testCase.pop())