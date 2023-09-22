// 696. Count Binary Substrings
// Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
// Substrings that occur multiple times are counted the number of times they occur.

var countBinarySubstrings = function(s) {
    if (s.length === 1) return 0
    let substrings = 0
    let prevCount = 1
    let i = 1
    while (s[i] === s[i - 1]) {
        prevCount++
        i++
    }
    if (i === s.length) return 0
    let count = 1
    i++
    for (i; i < s.length; i++) {
        if (s[i] !== s[i - 1]) {
            substrings += Math.min(count, prevCount)
            prevCount = count
            count = 1
        } else {
            count++
        }
    }
    substrings += Math.min(count, prevCount)
    return substrings
};

console.log(countBinarySubstrings('00110011'))
console.log(countBinarySubstrings('10101'))
console.log(countBinarySubstrings('00'))