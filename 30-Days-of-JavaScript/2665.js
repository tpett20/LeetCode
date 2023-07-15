// 2665. Counter II
/*
Write a function createCounter. It should accept an initial integer init. It should return an object with three functions.
The three functions are:
- increment() increases the current value by 1 and then returns it.
- decrement() reduces the current value by 1 and then returns it.
- reset() sets the current value to init and then returns it.
*/

var createCounter = function(init) {
    let val = init
    return {
        increment: () => val += 1,
        decrement: () => val -= 1,
        reset: () => val = init
    }
};

const counter = createCounter(5)
console.log(counter.increment())
console.log(counter.reset())
console.log(counter.decrement())