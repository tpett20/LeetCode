// 14. Longest Common Prefix
// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".

var longestCommonPrefix = function(strs) {
    let prefix = ''
    for (let i = 0; i < strs[0].length; i++) {
        let count = 0
        for (let j = 0; j < strs.length; j++) {
            if (strs[0][i] === strs[j][i]) {
                count += 1
            } else {
                return prefix
            }
            if (count === strs.length) {
                prefix += strs[0][i]
            }
        }
    }
    return prefix
};

console.log(longestCommonPrefix(["a", "b", 'C']))