// 1930. Unique Length-3 Palindromic Subsequences
/*
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
A palindrome is a string that reads the same forwards and backwards.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
- For example, "ace" is a subsequence of "abcde".
*/

var countPalindromicSubsequence = function(s) {
    let count = 0
    const map = {}
    for (let i = 0; i < s.length; i++) {
        let char = s[i]
        if (map[char]) {
            map[char]['last'] = i
        } else {
            map[char] = {
                first: i, 
                last: null,
            }
        }
    }
    for (let key in map) {
        if (map[key]['last']) {
            const set = new Set(
                s.slice(map[key]['first'] + 1, map[key]['last'])
            )
            count += set.size
        }
    }
    return count
};

console.log(countPalindromicSubsequence("aabca"))
console.log(countPalindromicSubsequence("adc"))
console.log(countPalindromicSubsequence("bbcbaba"))