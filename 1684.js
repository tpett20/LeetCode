// 1684. Count the Number of Consistent Strings
// You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
// Return the number of consistent strings in the array words.

var countConsistentStrings = function(allowed, words) {
    let count = 0
    const ref = new Set(allowed)
    for (const word of words) {
        let i = 0
        while (ref.has(word[i])) {
            i++
        }
        if (i === word.length) {
            count++
        }
    }
    return count
};

console.log(countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))