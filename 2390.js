// 2390. Removing Stars From a String
/*
You are given a string s, which contains stars *.
In one operation, you can: 
- Choose a star in s.
- Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.
Note:
- The input will be generated such that the operation is always possible.
- It can be shown that the resulting string will always be unique.
*/

var removeStars = function(s) {
    let newStr = ''
    let remove = 0
    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] === '*') {
            remove++
        } else if (remove > 0) {
            remove--
        } else {
            newStr = s[i] + newStr
        }
    }
    return newStr
};

console.log(removeStars('leet**cod*e'))
console.log(removeStars('erase*****'))