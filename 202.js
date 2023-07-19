// 202. Happy Number
/*
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
*/

var isHappy = function (n) {
    let cache = [n]
    while (n !== 1) {
        let str = n.toString()
        let nums = []
        for (let i = 0; i < str.length; i++) {
            nums.push(parseInt(str[i]))
        }
        n = 0
        for (let i = 0; i < nums.length; i++) {
            n += nums[i] ** 2
        }
        if (cache.includes(n)) {
            return false
        } else {
            cache.push(n)
        }
    }
    return true
};

console.log(isHappy(13), 'Expected: true')
console.log(isHappy(2), 'Expected: false')