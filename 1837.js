// 1837. Sum of Digits in Base K
// Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.
// After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.

var sumBase = function(n, k) {
    const convNum = n.toString(k)
    let sum = 0
    for (const digit of convNum) {
        sum += parseInt(digit)
    }
    return sum
};

console.log(sumBase(34, 6))