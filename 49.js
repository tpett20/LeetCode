// 49. Group Anagrams
/*
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
*/

var groupAnagrams = function(strs) {
    function alphabetize(s) {
        return s.split('').sort().join('')
    }
    const map = {}
    for (let str of strs) {
        code = alphabetize(str)
        if (map[code]) {
            map[code].push(str)
        } else {
            map[code] = [str]
        }
    }
    const arr = []
    for (let key in map) {
        arr.push(map[key])
    }
    return arr
};

console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
console.log(groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))