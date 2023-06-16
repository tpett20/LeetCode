// 290. Word Pattern
/*
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
*/

var wordPattern = function (pattern, s) {
    const map = new Map()
    const arr = s.split(' ')
    if (pattern.length !== arr.length) return false
    for (let i = 0; i < pattern.length; i++) {
        if (map.get(pattern[i]) === undefined) {
            map.set(pattern[i], arr[i])
        } else if (map.get(pattern[i]) !== arr[i]) {
            return false
        }
    }
    map.clear()
    for (let i = 0; i < arr.length; i++) {
        if (map.get(arr[i]) === undefined) {
            map.set(arr[i], pattern[i])
        } else if (map.get(arr[i]) !== pattern[i]) {
            return false
        }
    }
    return true
};

console.log(wordPattern('abba', 'dog cat cat dog'))