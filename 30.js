// 30. Substring with Concatenation of All Words
// 🚫 INCOMPLETE - Passes 160 / 179 Testcases
/*
You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
- For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.
*/

var findSubstring = function(s, words) {
    const output = []
    let wordLen = words[0].length
    if (wordLen * words.length > s.length) return output
    const map = {}
    let checker = { i: 0, len: words.length }
    for (let word of words) {
        map[word] = map[word] ? map[word] + 1 : 1
        checker[word] = map[word]
    }
    let resetChecker = true
    for (let i = 0; i <= s.length - wordLen; i++) {
        let str = s.slice(i, i + wordLen)
        if (map[str]) {
            while (!checker[str]) {
                let oldStr = s.slice(checker.i, checker.i + wordLen)
                checker[oldStr]++
                checker.len++
                checker.i += wordLen
            }
            checker[str]--
            checker.len--
            i += (wordLen - 1)
            resetChecker = false
        } else {
            if (!resetChecker) {
                checker = { ...map, i: i + 1, len: words.length }
                resetChecker = true
            } else checker.i = i + 1
        }
        if (checker.len === 0) output.push(checker.i)
    }
    return output
};

console.log(findSubstring('barfoothefoobarman', ['foo', 'bar']))
console.log('INCORRECT', findSubstring('aaaaaaaaaaaaaa', ['aa', 'aa']))