// 2515. Shortest Distance to Target String in a Circular Array
/*
You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.
- Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.
Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.
*/

var closetTarget = function(words, target, startIndex) {
    let dist = 0
    let l = startIndex, r = startIndex
    while (dist < words.length / 2 + 1) {
        if (words[l] === target || words[r] === target) {
            return dist
        }
        dist++
        l--
        if (l === -1) l = words.length - 1
        r++
        if (r === words.length) r = 0
    }
    return -1
};

console.log(closetTarget(["hello", "i", "am", "leetcode", "hello"], "hello", 1))
console.log(closetTarget(["a", "b", "leetcode"], "leetcode", 0))
console.log(closetTarget(["i", "eat", "leetcode"], "ate", 0))