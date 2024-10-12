// 2309. Greatest English Letter in Upper and Lower Case
// Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.
// An English letter b is greater than another letter a if b appears after a in the English alphabet.

var greatestLetter = function(s) {
    const uniqueLtrs = new Set(s)
    for (let i = 0; i < 26; i++) {
        const uprLtr = String.fromCharCode(26 - i + 64)
        const lwrLtr = String.fromCharCode(26 - i + 96)
        if (uniqueLtrs.has(uprLtr) && uniqueLtrs.has(lwrLtr)) {
            return uprLtr
        }
    }
    return ""
};

console.log(greatestLetter("MIKEpiazzA"))