// 2085. Count Common Words With One Occurrence
// Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

var countWords = function(words1, words2) {
    const map1 = {}
    for (const word of words1) {
        map1[word] = map1[word] ? ++map1[word] : 1
    }
    const map2 = {}
    for (const word of words2) {
        map2[word] = map2[word] ? ++map2[word] : 1
    }
    const shortMap = map1.length < map2.length ? map1 : map2
    const longMap = map1.length < map2.length ? map2 : map1
    let count = 0
    for (const word in shortMap) {
        if (shortMap[word] === 1 && longMap[word] === 1) {
            count += 1
        }
    }
    return count
};

console.log(countWords(["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]))
console.log(countWords(["b", "bb", "bbb"], ["a", "aa", "aaa"]))
console.log(countWords(["a", "ab"], ["a", "a", "a", "ab"]))