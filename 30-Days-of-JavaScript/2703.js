// 2703. Return Length of Arguments Passed
// Write a function argumentsLength that returns the count of arguments passed to it.

var argumentsLength = function(...args) {
    return arguments.length
};

console.log(argumentsLength(1, 2, 3))