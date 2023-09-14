// 509. Fibonacci Number
/*
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
*/

var fib = function(n) {
    if (n === 0) return 0
    if (n <= 2) return 1
    let sum
    function addition(num1, num2, count) {
        if (count === n) return
        sum = num1 + num2
        addition(num2, sum, ++count)
    }
    addition(1, 1, 2)
    return sum
};

for (let n = 0; n <= 10; n++) {
    console.log(`fib(${n}) = ${fib(n)}`)
}