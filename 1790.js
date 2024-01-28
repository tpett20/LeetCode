// 1790. Check if One String Swap Can Make Strings Equal
// You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
// Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

var areAlmostEqual = function(s1, s2) {
    if (s1 === s2) return true
    let d1 = "", d2 = ""
    for (let i = 0; i < s1.length; i++) {
        if (s1[i] !== s2[i]) {
            d1 += s1[i]
            d2 += s2[i]
            if (d1.length > 2) {
                return false
            }
        }
    }
    if (d1.length === 1) return false
    if (d1[0] === d2[1] && d1[1] === d2[0]) {
        return true
    } else {
        return false
    }
};

console.log(areAlmostEqual("bank", "kanb"))
console.log(areAlmostEqual("bank", "band"))