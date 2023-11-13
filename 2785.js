// 2785. Sort Vowels in a String
/*
Given a 0-indexed string s, permute s to get a new string t such that:
- All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
- The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
Return the resulting string.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.
*/

var sortVowels = function(s) {
    const vowelMap = {
        'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0,
        'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0
    }
    for (let char of s) {
        if (vowelMap[char] !== undefined) vowelMap[char]++ 
    }
    let sortedVowels = ''
    for (let vowel in vowelMap) {
        if (vowelMap[vowel]) {
            sortedVowels += vowel.repeat(vowelMap[vowel])
        }
    }
    let newStr = ''
    let i = 0
    for (let char of s) {
        if (vowelMap[char]) newStr += sortedVowels[i++]
        else newStr += char
    }
    return newStr
};

console.log(sortVowels("lEetcOde"))
console.log(sortVowels("sYntH"))