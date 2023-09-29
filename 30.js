// 30. Substring with Concatenation of All Words
/*
You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
- For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.
*/

var findSubstring = function(s, words) {
    const output = []
    let wordLen = words[0].length
    let totalWordsLen = wordLen * words.length
    if (totalWordsLen > s.length) return output
    const wordsMap = { len: words.length }
    let checker = { len: words.length }
    for (let word of words) {
        wordsMap[word] = wordsMap[word] ? wordsMap[word] + 1 : 1
        checker[word] = wordsMap[word]
    }
    for (let i = 0; i <= s.length - totalWordsLen; i++) {
        let str = s.slice(i, i + wordLen)
        let j = i
        while (checker[str]) {
            checker[str]--
            checker.len--
            j += wordLen
            str = s.slice(j, j + wordLen)
            if (checker.len === 0) output.push(i)
        }
        checker = { ...wordsMap }
    }
    return output
};

console.log(findSubstring('barfoofoobarthefoobarman', ['foo', 'bar', 'the']))
console.log(findSubstring('aaaaaaaaaaaaaa', ['aa', 'aa']))