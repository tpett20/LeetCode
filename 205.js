// 205. Isomorphic Strings
/*
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
*/

var isIsomorphic = function(s, t) {
    const sToT = {}
    const tToS = {}
    for (let i = 0; i < s.length; i++) {
        if (sToT[s[i]] === undefined) {
            sToT[s[i]] = t[i]
        } else if (sToT[s[i]] !== t[i]) {
            return false
        }
        if (tToS[t[i]] === undefined) {
            tToS[t[i]] = s[i]
        } else if (tToS[t[i]] !== s[i]) {
            return false
        }
    }
    return true
};

console.log(isIsomorphic("egg", "add"))
console.log(isIsomorphic("foo", "bar"))