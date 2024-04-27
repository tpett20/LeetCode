// 507. Perfect Number
// A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
// Given an integer n, return true if n is a perfect number, otherwise return false.

var checkPerfectNumber = function(num) {
    let sum = 0
    for (let dvr = 1; dvr <= num / 2; dvr++) {
        if (num % dvr === 0) {
            sum += dvr
        }
    }
    return num === sum
};

console.log(checkPerfectNumber(28))
console.log(checkPerfectNumber(7))
console.log(checkPerfectNumber(100000000))