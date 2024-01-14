// 1657. Determine if Two Strings Are Close
/*
Two strings are considered close if you can attain one from the other using the following operations:
- Operation 1: Swap any two existing characters.
    - For example, abcde -> aecdb
- Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    - For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.
Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
*/

var closeStrings = function(word1, word2) {
    if (word1.length !== word2.length) return false
    const map1 = buildMap(word1)
    const map2 = buildMap(word2)
    const countMap = {}
    for (let char in map1) {
        let count = map1[char]
        countMap[count] = countMap[count] ? ++countMap[count] : 1
    }
    for (let char in map2) {
        let count = map2[char]
        if (countMap[count]) {
            countMap[count]--
        } else {
            return false
        }
        if (map1[char] === undefined) {
            return false
        }
    }
    return true
    
    function buildMap(s) {
        const map = {}
        for (let char of s) {
            map[char] = map[char] ? ++map[char] : 1
        }
        return map
    }
};

console.log(closeStrings("abc", "bca"))
console.log(closeStrings("a", "aa"))
console.log(closeStrings("cabbba", "abbccc"))
console.log(closeStrings("tackle", "nickel"))