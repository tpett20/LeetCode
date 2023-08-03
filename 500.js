// 500. Keyboard Row
/*
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard.
In the American keyboard:
- the first row consists of the characters "qwertyuiop",
- the second row consists of the characters "asdfghjkl", and
- the third row consists of the characters "zxcvbnm".
*/

var findWords = function(words) {
    const firstRow = {
        q: true,
        w: true,
        e: true,
        r: true,
        t: true,
        y: true,
        u: true,
        i: true,
        o: true,
        p: true
    }
    const secondRow = {
        a: true,
        s: true,
        d: true,
        f: true,
        g: true,
        h: true,
        j: true,
        k: true,
        l: true
    }
    const lastRow = {
        z: true,
        x: true,
        c: true,
        v: true,
        b: true,
        n: true,
        m: true
    }
    for (let i = 0; i < words.length; i++) {
        let word = words[i]
        let row
        let firstChar = word[0].toLowerCase()
        if (firstRow[firstChar]) {
            row = 1
        } else if (secondRow[firstChar]) {
            row = 2
        } else {
            row = 3
        }
        for (let char of word) {
            char = char.toLowerCase()
            if (row === 1 && !firstRow[char]) {
                words.splice(i, 1)
                i--
                break
            } else if (row === 2 && !secondRow[char]) {
                words.splice(i, 1)
                i--
                break
            } else if (row === 3 && !lastRow[char]) {
                words.splice(i, 1)
                i--
                break
            }
        }
    }
    return words
};

console.log(findWords(["Hello","Alaska","Dad","Peace"]))