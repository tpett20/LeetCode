// 2785. Sort Vowels in a String
// 🏆 Biweekly Contest 109
/*
Given a 0-indexed string s, permute s to get a new string t such that:
All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
Return the resulting string.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.
*/

var sortVowels = function(s) {
    let t = ''
    let vowels = ['a', 'e', 'i', 'o', 'u']
    let sVowels = []
    for (let i = 0; i < s.length; i++) {
        if (vowels.includes(s[i].toLowerCase())) {
            sVowels.push(s[i].charCodeAt())
        }
    }
    sVowels.sort((a, b) => a - b)
    let j = 0
    for (let i = 0; i < s.length; i++) {
        if (vowels.includes(s[i].toLowerCase())) {
            t += String.fromCharCode(sVowels[j])
            j++
        } else {
            t += s[i]
        }
    }
    return t
};

console.log(sortVowels('lEetcOde'))
console.log(sortVowels('lYmpH'))