// 2486. Append Characters to String to Make Subsequence
/*
You are given two strings s and t consisting of only lowercase English letters.
Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
*/

var appendCharacters = function(s, t) {
    let i = 0
    for (const char of s) {
        if (char === t[i]) {
            i += 1
            if (i === t.length) return 0
        }
    }
    return t.length - i
};

console.log(appendCharacters("coaching", "coding"))
console.log(appendCharacters("abcde", "a"))
console.log(appendCharacters("z", "abcde"))