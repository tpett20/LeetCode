// 1957. Delete Characters to Make Fancy String
/*
A fancy string is a string where no three consecutive characters are equal.
Given a string s, delete the minimum possible number of characters from s to make it fancy.
Return the final string after the deletion. It can be shown that the answer will always be unique.
*/

var makeFancyString = function(s) {
    if (s.length < 3) return s
    let output = s[0] + s[1]
    for (let i = 2; i < s.length; i++) {
        if (s[i] !== s[i - 1] || s[i] !== s[i - 2]) {
            output += s[i]
        }
    }
    return output
};

console.log(makeFancyString("mikepiazzza"))
console.log(makeFancyString("aaabaaaa"))
console.log(makeFancyString("a"))