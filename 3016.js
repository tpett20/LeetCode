// 3016. Minimum Number of Pushes to Type Word II
/*
You are given a string word containing lowercase English letters.
Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .
It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.
Return the minimum number of pushes needed to type word after remapping the keys.
An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.
*/

var minimumPushes = function(word) {
    const btnLengths = [4, 4]
    for (let i = 3; i > 0; i--) {
        for (let j = 0; j < 8; j++) {
            btnLengths.push(i)
        }
    }
    const freq = {}
    for (const char of word) {
        freq[char] = freq[char] ? ++freq[char] : 1
    }
    const freqArr = []
    for (const char in freq) {
        freqArr.push(freq[char])
    }
    freqArr.sort((a, b) => a - b)
    let count = 0
    while (freqArr.length) {
        const charCount = freqArr.pop()
        const pushCount = btnLengths.pop()
        count += (charCount * pushCount)
    }
    return count
};

console.log(minimumPushes("abcde"))
console.log(minimumPushes("aabbccddeeffgghhiiiiii"))