// 2745. Construct the Longest New String
// 🏆 Biweekly Contest 107 
/*
You are given three integers x, y, and z.
You have x strings equal to "AA", y strings equal to "BB", and z strings equal to "AB". You want to choose some (possibly all or none) of these strings and concactenate them in some order to form a new string. This new string must not contain "AAA" or "BBB" as a substring.
Return the maximum possible length of the new string.
A substring is a contiguous non-empty sequence of characters within a string.
*/

var longestString = function (x, y, z) {
    if (x > y) {
        return (y + y + 1 + z) * 2
    } else if (y > x) {
        return (x + x + 1 + z) * 2
    } else {
        return (x + y + z) * 2
    }
};

console.log(longestString(2, 5, 1))
console.log(longestString(3, 2, 2))
console.log(longestString(0, 0, 2))
console.log(longestString(3, 2, 1))