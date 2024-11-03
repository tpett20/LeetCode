// 796. Rotate String
/*
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
- For example, if s = "abcde", then it will be "bcdea" after one shift.
*/

var rotateString = function(s, goal) {
    if (s.length !== goal.length) return false
    if (s === goal) return true
    const idxs = []
    for (let i = 0; i < goal.length; i++) {
        let j = 0
        let k = i
        while (j < s.length && s[j] === goal[k]) {
            j++
            k++
            if (k === goal.length) {
                k = 0
            }
        }
        if (j === s.length) return true
    }
    return false
};

console.log(rotateString("abcde", "cdeab")) 
console.log(rotateString("abcde", "abced")) 