// 2278. Percentage of Letter in String
// Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

var percentageLetter = function(s, letter) {
    let count = 0
    for (let char of s) {
        if (char === letter) {
            count += 1
        }
    }
    return Math.floor(count / s.length * 100)
};

console.log(percentageLetter("foobar", "o"))
console.log(percentageLetter("jjjj", "k"))