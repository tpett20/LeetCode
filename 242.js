// 242. Valid Anagram
// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

var isAnagram = function(s, t) {
    if (s.length !== t.length) return false
    const map = {}
    for (let char of s) {
        map[char] = map[char] ? ++map[char] : 1
    }
    for (let char of t) {
        if (!map[char]) return false
        else map[char]--
    }
    return true
};

console.log(isAnagram("anagram", "nagaram"))
console.log(isAnagram("cat", "car"))