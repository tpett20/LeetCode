// 344. Reverse String
// Write a function that reverses a string. The input string is given as an array of characters s.
// You must do this by modifying the input array in-place with O(1) extra memory.

var reverseString = function(s) {
    let frontIdx = 0
    let backIdx = s.length - 1
    while (frontIdx < backIdx) {
        let cachedChar = s[frontIdx]
        s[frontIdx] = s[backIdx]
        s[backIdx] = cachedChar
        frontIdx++
        backIdx--
    }
};

let testCase = ["h","e","l","l","o"]
console.log(`Before: ${testCase}`)
reverseString(testCase)
console.log(`After:  ${testCase}`)