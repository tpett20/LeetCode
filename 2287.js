// 2287. Rearrange Characters to Make Target String
// You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new strings.
// Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.

var rearrangeCharacters = function(s, target) {
    const map = {}
    for (let char of s) {
        map[char] = map[char] ? map[char] + 1 : 1
    }
    let i = 0
    let count = 0
    while (i < target.length) {
        let char = target[i]
        if (map[char]) {
            map[char]--
            i++
        } else {
            break
        }
        if (i === target.length) {
            count++
            i = 0
        }
    }
    return count
};

console.log(rearrangeCharacters('ilovecodingonleetcode', 'code'))
console.log(rearrangeCharacters('abcba', 'abc'))
console.log(rearrangeCharacters('abbaccaddaeea', 'aaaaa'))