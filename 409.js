// 409. Longest Palindrome
// Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
// Letters are case sensitive, for example, "Aa" is not considered a palindrome.

var longestPalindrome = function(s) {
    const obj = {}
    for (const char of s) {
        obj[char] = obj[char] ? ++obj[char] : 1
    }
    let count = 0, extra = false
    for (const char in obj) {
        const freq = obj[char]
        if (freq % 2 === 0) {
            count += freq
        } else {
            count += (freq - 1)
            extra = true
        }
    }
    return extra ? count + 1 : count
};

console.log(longestPalindrome("abccccdd"))
console.log(longestPalindrome("a"))