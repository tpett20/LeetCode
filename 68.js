// 68. Text Justification
/*
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
*/

var fullJustify = function (words, maxWidth) {
    let i = 0
    let line = ''
    let space = ' '
    let output = []
    while (i < words.length) {
        if (words[i].length === maxWidth) {
            if (line) output.push(line)
            line = ''
            output.push(words[i])
            i++
        } else if (line.length + words[i].length + 1 > maxWidth) {
            output.push(line)
            line = ''
        } else if (line === '') {
            line = words[i]
            i++
        } else {
            line += " " + words[i]
            i++
        }
    }
    if (line) output.push(line)
    for (let i = 0; i < output.length - 1; i++) {
        let difference = maxWidth - output[i].length
        if (difference) {
            output[i] = fillLine(difference, output[i])
        }
    }
    let lastDiff = maxWidth - output[output.length - 1].length
    if (lastDiff) {
        output[output.length - 1] += space.repeat(lastDiff)
    }
    function fillLine(diff, ln) {
        let count = 0
        for (let i = 0; i < ln.length; i++) {
            if (ln[i] === ' ') count++
        }
        if (count === 0) return ln += space.repeat(diff)
        let spacesEach = Math.floor(diff / count)
        let extraSpaces = diff % count
        let string = ln[0]
        let i = 1
        while (i < ln.length) {
            string += ln[i]
            if (ln[i] === ' ' && ln[i - 1] !== ' ') {
                if (spacesEach) {
                    string += space.repeat(spacesEach)
                }
                if (extraSpaces) {
                    string += ' '
                    extraSpaces--
                }
            }
            i++
        }
        return string
    }
    return output
};

console.log(fullJustify(["The", "important", "thing", "is", "not", "to", "stop", "questioning.", "Curiosity", "has", "its", "own", "reason", "for", "existing."], 17))
console.log(fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6))
console.log(fullJustify(["A"], 1))