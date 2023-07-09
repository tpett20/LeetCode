// 345. Reverse Vowels of a String
/*
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
*/

var reverseVowels = function(s) {
    vowels = {
        'a': true,
        'e': true,
        'i': true,
        'o': true,
        'u': true
    }
    sVowels = ''
    for (let char of s) {
        if (vowels[char.toLowerCase()]) {
            sVowels = char + sVowels
        }
    }
    if (!sVowels) return s
    newString = ''
    let i = 0
    for (let char of s) {
        if (vowels[char.toLowerCase()]) {
            newString += sVowels[i]
            i++
        } else {
            newString += char
        }
    }
    return newString
};

console.log(reverseVowels('hello'))
console.log(reverseVowels('aA'))