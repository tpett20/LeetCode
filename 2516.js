// 2516. Take K of Each Character From Left and Right
// You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.
// Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

var takeCharacters = function(s, k) {
    let a = 0, b = 0, c = 0
    for (const char of s) {
        if (char === "a") a++
        else if (char === "b") b++
        else c++
    }
    if (a < k || b < k || c < k) return -1
    let maxLen = 0
    let lt = 0
    for (let rt = 0; rt < s.length; rt++) {
        if (s[rt] === "a") a--
        else if (s[rt] === "b") b--
        else c--

        while (a < k || b < k || c < k) {
            if (s[lt] === "a") a++
            else if (s[lt] === "b") b++
            else c++
            lt++
        }
        maxLen = Math.max(maxLen, rt - lt + 1) 
    }
    return s.length - maxLen
};

console.log(takeCharacters("aabaaaacaabc", 2))