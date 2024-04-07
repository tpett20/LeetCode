// 678. Valid Parenthesis String
/*
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
*/

var checkValidString = function(s) {
    const arr = s.split("")
    const left = []
    const wild = []
    for (let i = 0; i < arr.length; i++) {
        const char = arr[i]
        if (char === ")") {
            if (left.length) {
                const lIdx = left.pop()
                arr[i] = ""
                arr[lIdx] = ""
            } else if (wild.length) {
                const wIdx = wild.pop()
                arr[i] = ""
                arr[wIdx] = ""
            } else {
                return false
            } 
        } else if (char === "(") {
            left.push(i)
        } else if (char === "*") {
            wild.push(i)
        }
    }
    if (!left.length) return true
    else if (left.length > wild.length) return false
    let wildCount = 0
    for (let i = arr.length - 1; i >= 0; i--) {
        const char = arr[i]
        if (char === "(") {
            if (!wildCount) {
                return false
            } else {
                wildCount--
            }
        } else if (char === "*") {
            wildCount++
        }
    }
    return true
};

console.log(checkValidString("()"))
console.log(checkValidString("(*)"))
console.log(checkValidString("(*))"))