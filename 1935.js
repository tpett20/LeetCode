// 1935. Maximum Number of Words You Can Type
// There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.
// Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

var canBeTypedWords = function(text, brokenLetters) {
    let count = 0
    const arr = text.split(' ')
    const map = {}
    for (let char of brokenLetters) {
        map[char] = 1
    }
    for (let word of arr) {
        let good = true
        for (let char of word) {
            if (map[char]) {
                good = false
                break
            }
        }
        if (good) count++
    }
    return count
};

console.log(canBeTypedWords('hello world', 'ad'))