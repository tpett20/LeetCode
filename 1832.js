// 1832. Check if the Sentence Is Pangram
// A pangram is a sentence where every letter of the English alphabet appears at least once.
// Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

var checkIfPangram = function(sentence) {
    const set = new Set()
    for (let char of sentence) {
        set.add(char)
    }
    return set.size === 26 ? true : false
};

console.log(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
console.log(checkIfPangram("letsgomets"))