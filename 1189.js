// 1189. Maximum Number of Balloons
// Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
// You can use each character in text at most once. Return the maximum number of instances that can be formed.

var maxNumberOfBalloons = function(text) {
    const map = {
        b: 0,
        a: 0,
        l: 0,
        o: 0,
        n: 0
    }
    for (let char of text) {
        if (map[char] !== undefined) {
            if (char === 'l' || char === 'o') {
                map[char] += 0.5
            } else {
                map[char]++
            }
        }
    }
    let balloonCount = map['b']
    for (let ltr in map) {
        if (map[ltr] < balloonCount) {
            balloonCount = Math.floor(map[ltr])
        }
    }
    return balloonCount
};

console.log(maxNumberOfBalloons('loonbalxballpoon'))