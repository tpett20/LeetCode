// 451. Sort Characters By Frequency
// Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
// Return the sorted string. If there are multiple answers, return any of them.

var frequencySort = function(s) {
    const map = {}
    for (let char of s) {
        map[char] = map[char] ? map[char] + char : char
    }
    const arr = Object.values(map)
    arr.sort((a, b) => b.length - a.length)
    return arr.join("")
};

console.log(frequencySort("tree"))
console.log(frequencySort("cccaaa"))
console.log(frequencySort("Aabb"))