// 2914. Minimum Number of Changes to Make Binary String Beautiful
/*
You are given a 0-indexed binary string s having an even length.
A string is beautiful if it's possible to partition it into one or more substrings such that:
- Each substring has an even length.
- Each substring contains only 1's or only 0's.
You can change any character in s to 0 or 1.
Return the minimum number of changes required to make the string s beautiful.
*/

var minChanges = function(s) {
    if (s.length === 2) {
        if (s[0] === s[1]) return 0
        else return 1
    }
    let changes = 0
    for (let i = 0; i < s.length - 1; i += 2) {
        if (s[i] !== s[i + 1]){
            changes++
        }
    }
    return changes
};

console.log(minChanges("1001"))
console.log(minChanges("10"))
console.log(minChanges("0000"))