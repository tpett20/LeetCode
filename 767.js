// 767. Reorganize String
// Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
// Return any possible rearrangement of s or return "" if not possible.

var reorganizeString = function(s) {
    const map = {}
    for (let char of s) {
        if (map[char]) {
            map[char]++
            if (map[char] > (s.length - map[char]) + 1) {
                return ''
            }
        } else {
            map[char] = 1
        }
    }
    const arr = []
    for (let key in map) {
        arr.push({
            char: key,
            freq: map[key]
        })
    }
    arr.sort((a, b) => b.freq - a.freq)
    let i = 0
    let j = 1
    let newStr = ''
    let extraChars = ''
    while (i < arr.length) {
        if (arr[i].freq > 0) {
            if (newStr[newStr.length - 1] !== arr[i].char) {
                newStr += arr[i].char
                arr[i].freq--
            } else {
                extraChars += arr[i].char
                arr[i].freq--
            }
            while (arr[j]?.freq === 0) {
                j++
            }
            if (j < arr.length) {
                newStr += arr[j].char
                arr[j].freq--
            }
        } else {
            i++
            j = i + 1
        }
    }
    if (extraChars) {
        let finalStr = ''
        let j = 0
        for (let i = 0; i < newStr.length; i++) {
            if (j < extraChars.length && newStr[i] !== finalStr[j]) {
                finalStr += extraChars[j] + newStr[i]
                j++
            } else {
                finalStr += newStr[i]
            }
        }
        return finalStr
    }
    return newStr
};

console.log('appletree', '->', reorganizeString('appletree'))
console.log('aaabbbccc', '->', reorganizeString('aaabbbccc'))