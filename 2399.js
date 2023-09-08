// 2399. Check Distances Between Same Letters
/*
You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.
Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.
Return true if s is a well-spaced string, otherwise return false.
*/

var checkDistances = function (s, distance) {
    const map = {}
    for (let i = 0; i < s.length; i++) {
        let char = s[i]
        if (map[char] === undefined) {
            map[char] = i + 1
        } else {
            map[char] = i - map[char]
            let code = char.charCodeAt() - 97
            if (map[char] !== distance[code]) {
                return false
            }
        }
    }
    return true
};

console.log(checkDistances(
    'abaccb',
    [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
))

console.log(checkDistances(
    'aa', 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
))