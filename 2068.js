// 2068. Check Whether Two Strings are Almost Equivalent
/*
Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.
Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.
The frequency of a letter x is the number of times it occurs in the string.
*/

var checkAlmostEquivalent = function(word1, word2) {
    const map1 = {}
    const map2 = {}
    for (let char of word1) {
        map1[char] = map1[char] ? map1[char] + 1 : 1
    }
    for (let char of word2) {
        map2[char] = map2[char] ? map2[char] + 1 : 1
    }
    for (let key in map1) {
        if (map2[key]) {
            if (Math.abs(map2[key] - map1[key]) > 3) {
                return false
            }
            delete map2[key]
        } else if (map1[key] > 3) {
            return false
        }
    }
    for (let key in map2) {
        if (map2[key] > 3) {
            return false
        }
    }
    return true
};

console.log(checkAlmostEquivalent('cccddabba', 'babababab'))