// 2506. Count Pairs Of Similar Strings
/*
You are given a 0-indexed string array words.
Two strings are similar if they consist of the same characters.
- For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
- However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.
*/

var similarPairs = function(words) {
    let pairs = 0
    const map = {}
    for (let word of words) {
        const alphaLtrs = word.split('').sort()
        let key = alphaLtrs[0]
        for (let char of alphaLtrs) {
            if (key[key.length - 1] !== char) {
                key += char
            }
        }
        if (!map[key]) {
            map[key] = 1
        } else {
            pairs += map[key]
            map[key]++
        }
    }
    return pairs
};

console.log(similarPairs(["aba","aabb","abcd","bac","aabc"]))