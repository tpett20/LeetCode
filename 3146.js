// 3146. Permutation Difference between Two Strings
/*
You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.
The permutation difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of each character in s and the index of the occurrence of the same character in t.
Return the permutation difference between s and t.
*/

var findPermutationDifference = function(s, t) {
    const sIdxs = {}
    for (let i = 0; i < s.length; i++) {
        sIdxs[s[i]] = i
    }
    let diff = 0
    for (let i = 0; i < t.length; i++) {
        diff += Math.abs(sIdxs[t[i]] - i)
    }
    return diff
};

console.log(findPermutationDifference("abc", "bac"))
console.log(findPermutationDifference("abcde", "edbac"))