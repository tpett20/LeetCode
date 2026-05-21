// 3043. Find the Length of the Longest Common Prefix
// You are given two arrays with positive integers arr1 and arr2.
// A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, while 234 is not.
// A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. For example, 5655359 and 56554 have common prefixes 565 and 5655 while 1223 and 43456 do not have a common prefix.
// You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.
// Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.

var longestCommonPrefix = function(arr1, arr2) {
    let maxLen = 0
    let ceil = 0
    const trie1 = {}
    for (const num of arr1) {
        const strNum = num.toString()
        ceil = Math.max(ceil, strNum.length)
        let level = trie1
        for (const digit of strNum) {
            if (!level[digit]) {
                level[digit] = {}
            }
            level = level[digit]
        }
    }
    for (const num of arr2) {
        let strNum = num.toString()
        if (strNum.length < maxLen) continue
        let len = 0
        let level = trie1
        while (level[strNum[len]]) {
            level = level[strNum[len]]
            len++
        }
        maxLen = Math.max(len, maxLen)
        if (maxLen === ceil) return maxLen
    }
    return maxLen
};

const testCase1 = [554, 553, 210]
const testCase2 = [550, 523, 211]
console.log(longestCommonPrefix(testCase1, testCase2))