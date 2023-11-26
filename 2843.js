// 2843. Count Symmetric Integers
/*
You are given two positive integers low and high.
An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.
Return the number of symmetric integers in the range [low, high].
*/

var countSymmetricIntegers = function(low, high) {
    let count = 0
    while (low <= high) {
        let x = low.toString()
        if (x.length % 2 !== 0) {
            let jump = '1' + '0'.repeat(x.length)
            low = parseInt(jump)
            continue
        }
        let n = x.length / 2
        let frontSum = getSum(x.slice(0, n))
        let backSum = getSum(x.slice(n))
        let diff = frontSum - backSum
        if (diff === 0) {
            count++
        } else if (diff > 0) {
            low += diff
        } 
        if (diff <= 0) {
            let jump = 10 - parseInt(x[x.length - 1])
            low += jump
        }
    }
    return count

    function getSum(str) {
        let sum = 0
        for (let digit of str) {
            sum += parseInt(digit)
        }
        return sum
    }
};

console.log(countSymmetricIntegers(1, 100))
console.log(countSymmetricIntegers(1200, 1230))