// 459. Repeated Substring Pattern
// Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

var repeatedSubstringPattern = function(s) {
    let divisor = 1
    const divisors = []
    while (divisor <= (s.length / 2)) {
        if (s.length % divisor === 0) {
            divisors.push(divisor)
        }
        divisor++
    }
    for (let divisor of divisors) {
        let valid = true
        let str = s.slice(0, divisor)
        const testArr = s.split(str)
        for (let remainder of testArr) {
            if (remainder !== '') {
                valid = false
                break
            }
        }
        if (valid) return true
    }
    return false
};

console.log(repeatedSubstringPattern('abcabc'))
console.log(repeatedSubstringPattern('abc'))