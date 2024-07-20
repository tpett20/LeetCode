// 2942. Find Words Containing Character
/*
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.
*/

var findWordsContaining = function(words, x) {
    const output = []
    for (let i = 0; i < words.length; i++) {
        if (words[i].includes(x)) {
            output.push(i)
        }
    }
    return output
};

console.log(findWordsContaining(["leet","code"], x = "t"))
console.log(findWordsContaining(["abc", "bcd", "aaaa", "cbc"], x = "a"))