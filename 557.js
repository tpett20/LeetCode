// 557. Reverse Words in a String III
// Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

var reverseWords = function(s) {
    const arr = s.split(' ')
    let output = ''
    for (let i = 0; i < arr.length; i++) {
        let word = arr[i]
        output += rev(word)
        if (i !== arr.length - 1) {
            output += ' '
        }
    }
    return output
    
    function rev(str) {
        let newStr = ''
        for (let char of str) {
            newStr = char + newStr
        }
        return newStr
    }
};

console.log(reverseWords("Let's Go Mets!"))