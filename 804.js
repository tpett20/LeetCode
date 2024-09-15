// 804. Unique Morse Code Words
/*
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
    'a' maps to ".-",
    'b' maps to "-...",
    'c' maps to "-.-.", and so on.
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
    For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.
*/

var uniqueMorseRepresentations = function (words) {
    const morseTable = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", 
        "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", 
        "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", 
        "-.--", "--.."
    ]
    const uniqueReps = new Set()
    for (const word of words) {
        let rep = ""
        for (const ltr of word) {
            const idx = ltr.charCodeAt() - 97
            rep += morseTable[idx]
        }
        uniqueReps.add(rep)
    }
    return uniqueReps.size
};

console.log(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
console.log(uniqueMorseRepresentations(["lets", "go", "mets"]))