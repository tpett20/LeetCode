// 3121. Count the Number of Special Characters II
// You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
// Return the number of special letters in word.

var numberOfSpecialChars = function(word) {
    const occs = []
    for (let i = 0; i < 26; i++) {
        occs.push([])
    }
    for (let i = 0; i < word.length; i++) {
        let code = word.charCodeAt(i)
        if (code >= 65 && code <= 90) {
            code -= 65
            if (occs[code][1] === undefined) {
                occs[code][1] = i
            }
        } else {
            code -= 97
            occs[code][0] = i
        }
    }
    let count = 0
    for (const occ of occs) {
        if (occ.length === 2 && occ[0] < occ[1]) {
            count += 1
        }
    }
    return count
};

console.log(numberOfSpecialChars("aaAbcBC"))
console.log(numberOfSpecialChars("abc"))
console.log(numberOfSpecialChars("AbBCab"))
console.log(numberOfSpecialChars("AaA"))