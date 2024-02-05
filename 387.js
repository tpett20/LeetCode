// 387. First Unique Character in a String
// Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

var firstUniqChar = function(s) {
    const seen = {}
    for (let i = 0; i < s.length; i++) {
        let char = s[i]
        seen[char] = (seen[char] === undefined) ? i : false
    }
    for (let char in seen) {
        if (seen[char] !== false) {
            return seen[char]
        }
    }
    return -1
};

console.log(firstUniqChar("leetcode"))
console.log(firstUniqChar("loveleetcode"))
console.log(firstUniqChar("aabb"))