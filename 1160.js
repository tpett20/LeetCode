// 1160. Find Words That Can Be Formed by Characters
/*
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.
*/

var countCharacters = function(words, chars) {
    const map = {}
    for (let char of chars) {
        map[char] = map[char] ? ++map[char] : 1
    }
    let sum = 0
    for (let word of words) {
        sum += checkWord(word, {...map})
    }
    return sum
    
    function checkWord(w, m) {
        for (let char of w) {
            if (m[char]) m[char]--
            else return 0
        }
        return w.length
    }
};

console.log(countCharacters(["cat","bt","hat","tree"], "atach"))
console.log(countCharacters(["hello","world","leetcode"], "welldonehoneyr"))