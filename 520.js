// 520. Detect Capital
/*
We define the usage of capitals in a word to be right when one of the following cases holds:
- All letters in this word are capitals, like "USA".
- All letters in this word are not capitals, like "leetcode".
- Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
*/

var detectCapitalUse = function(word) {
    if (word.length === 1) return true
    let allLower = true
    let allUpper = true
    for (let i = 1; i < word.length; i++) {
        let code = word[i].charCodeAt()
        if (code >= 97 && code <= 122) {
            allUpper = false
        } else {
            allLower = false
        }
        if (!allLower && !allUpper) return false
    }
    if (allLower) return true
    let firstCode = word[0].charCodeAt()
    if (allUpper && firstCode >= 65 && firstCode <= 90) {
        return true
    }
    return false
};

console.log(detectCapitalUse('USA'))
console.log(detectCapitalUse('FlaG'))