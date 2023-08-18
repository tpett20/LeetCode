// 263. Ugly Number
// An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
// Given an integer n, return true if n is an ugly number.

var isUgly = function(n) {
    if (n < 1) return false
    let i = 2
    while (n !== 1) {
        if (n % i === 0) {
            n = n / i
        }
        else i++
        if (i > 5) return false
    }
    return true
};

console.log(isUgly(6))
console.log(isUgly(14))