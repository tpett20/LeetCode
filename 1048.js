// 1048. Longest String Chain
/*
You are given an array of words where each word consists of lowercase English letters.
wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.
    For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
Return the length of the longest possible word chain with words chosen from the given list of words.
*/

var longestStrChain = function(words) {
    function checkPredecessor(wordA, wordB) {
        if (wordB.length - wordA.length !== 1) return false
        let diff = 0
        let i = 0, j = 0
        while (i < wordA.length) {
            if (wordA[i] !== wordB[j]) {
                diff++
                if (diff > 1) return false
            } else {
                i++
            }
            j++
        }
        return true
    }

    function dfs(str) {
        if (cache[str]) return cache[str]
        const nextIdx = str.length
        const nextOptions = wordsArr[nextIdx]
        let maxDepth = 0
        for (const nextStr of nextOptions) {
            if (checkPredecessor(str, nextStr)) {
                maxDepth = Math.max(maxDepth, dfs(nextStr))
            }
        }
        cache[str] = maxDepth + 1
        return cache[str]
    }

    const MAX_WORD_LEN = 16
    const wordsArr = []
    const cache = {}
    for (let i = 0; i <= MAX_WORD_LEN; i++) {
        wordsArr.push(new Set())
    }
    for (const word of words) {
        const idx = word.length - 1
        wordsArr[idx].add(word)
    }
    let maxChainLen = 0
    for (const wordsSet of wordsArr) {
        for (const word of wordsSet) {
            maxChainLen = Math.max(maxChainLen, dfs(word))
        }
    }
    return maxChainLen
};

console.log(longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
console.log(longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
console.log(longestStrChain(["abcd", "dbqca"]))
console.log(longestStrChain(["abcdefghijklmno", "abcdefghijklmnop"]))