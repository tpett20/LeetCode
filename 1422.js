// 1422. Maximum Score After Splitting a String
// Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
// The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

var maxScore = function(s) {
    let zeros = 0, ones = 0
    for (const bit of s) {
        if (bit === "1") {
            ones++
        }
    }
    let score = 0
    for (let i = 0; i < s.length - 1; i++) {
        if (s[i] === "0") {
            zeros++
        } else {
            ones--
        }
        score = Math.max(score, zeros + ones)
    }
    return score
};

console.log(maxScore("011101"))
console.log(maxScore("10"))
console.log(maxScore("01"))