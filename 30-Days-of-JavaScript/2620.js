var createCounter = function(n) {
    n--
    return function() {
        return n += 1
    };
};

const counter = createCounter(10)
console.log(counter())
console.log(counter())
console.log(counter())