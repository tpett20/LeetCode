// 2744. Find Maximum Number of String Pairs
// 🏆 Biweekly Contest 107
/*
You are given a 0-indexed array words consisting of distinct strings.
The string words[i] can be paired with the string words[j] if:
The string words[i] is equal to the reversed string of words[j].
0 <= i < j < words.length.
Return the maximum number of pairs that can be formed from the array words.
Note that each string can belong in at most one pair.
*/

var maximumNumberOfStringPairs = function (words) {
    let count = 0
    let i = 0
    let j = 1
    while (words.length > 1) {
        if (words[i] === words[j].split('').reverse().join('')) {
            count++
            words.splice(i, 1)
            words.splice(j - 1, 1)
            i = 0
            j = 1
        } else if (j < words.length - 1) {
            j++
        } else {
            words.splice(i, 1)
            i = 0
            j = 1
        }
    }
    return count
};

console.log(maximumNumberOfStringPairs(["cd", "ac", "dc", "ca", "zz"]))
console.log(maximumNumberOfStringPairs(["ab", "ba", "cc"]))
console.log(maximumNumberOfStringPairs(["aa", "ab"]))